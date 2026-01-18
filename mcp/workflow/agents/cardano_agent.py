from typing import TypedDict, Annotated, Literal
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from workflow.tools.blockfrost_tool import get_address_details, get_transactions_for_address, get_single_transaction_details
from workflow.tools.knowledge_base_tool import search_cardano_knowledge, get_cardano_faq
from app.core.config import GEMINI_MODEL, TEMPERATURE, GOOGLE_API_KEY

import logging
logger = logging.getLogger(__name__)

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
    user_query: str
    context: str
    response: str

class CardanoAgent:
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(
            model=GEMINI_MODEL,  # Using gemini-1.5-flash
            temperature=TEMPERATURE,
            google_api_key=GOOGLE_API_KEY
        )
        self.tools = [
            get_address_details,
            search_cardano_knowledge,
            get_transactions_for_address,
            get_single_transaction_details
        ]
        self.llm_with_tools = self.model.bind_tools(self.tools)
        self.tool_node = ToolNode(self.tools)
        self.system_prompt = """
        You are a helpful Cardano blockchain assistant. You can help users with:

        1. **Blockchain Queries**: Retrieve and explain transaction data, address information, and analyze transaction flows using Blockfrost API
        2. **Knowledge Base**: Answer questions about Cardano concepts, protocols, and general blockchain information

        **Guidelines:**
        - For transaction hashes, addresses, or specific blockchain data requests, use the appropriate Blockfrost tools
        - For general questions about Cardano, staking, smart contracts, etc., use the knowledge base tools
        - Always provide clear, detailed explanations
        - If you need to use tools, explain what you're doing
        - Present data in a user-friendly format
        - If a transaction address seems invalid, guide the user on the correct format

        **Tool Usage:**
        - Only use tools when necessary
        """

        self.graph = self._build_graph()

    def _build_graph(self) -> StateGraph:
        def should_continue(state: AgentState) -> Literal["tools", "end"]:
            last_message = state["messages"][-1]
            if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
                return "tools"
            return "end"

        def call_model(state: AgentState) -> AgentState:
            messages = state["messages"]
            response = self.llm_with_tools.invoke(messages)
            return {"messages": [response]}

        def call_tools(state: AgentState) -> AgentState:
            last_message = state["messages"][-1]
            tool_results = self.tool_node.invoke({"messages": [last_message]})
            return {"messages": state["messages"] + tool_results["messages"]}

        workflow = StateGraph(AgentState)
        workflow.add_node("agent", call_model)
        workflow.add_node("tools", self.tool_node)
        workflow.add_edge(START, "agent")
        workflow.add_conditional_edges(
            "agent",
            should_continue,
            {
                "tools": "tools",
                "end": END
            }
        )
        workflow.add_edge("tools", "agent")

        checkpointer = MemorySaver()
        graph = workflow.compile(checkpointer=checkpointer)
        return graph
    
    def is_new_thread(self, thread_id: int) -> bool:
        """
        Checks if this is a new thread by querying the graph's state.
        Returns True if there is no history for this thread_id.
        """
        config = {"configurable": {"thread_id": str(thread_id)}}
        state = self.graph.get_state(config=config)
        if state.values == {}:
            return True
        else:
            return False

def chat(graph: StateGraph, thread_id: int, user_input: str) -> str:
    try:
         # Detect if this is a new thread by checking existing state
        is_new = agent.is_new_thread(thread_id)

        messages = []
        if is_new:
            print("Starting a new thread.")
            messages.append(SystemMessage(content=agent.system_prompt))
            
        messages.append(HumanMessage(content=user_input))

        initial_state = {
            "messages": messages,
            "user_query": user_input,
            "context": "",
            "response": ""
        }
        config = {"configurable": {"thread_id": thread_id}}
        result = graph.invoke(initial_state, config)
        final_message = result["messages"][-1]
        if hasattr(final_message, 'content'):
            content = final_message.content
            # Handle Gemini's list format response
            if isinstance(content, list):
                # Extract text from list of content blocks
                text_parts = [block.get('text', '') if isinstance(block, dict) else str(block) for block in content]
                return ''.join(text_parts)
            return content
        else:
            return str(final_message)
    except Exception as e:
        return f"I encountered an error while processing your request: {str(e)}"

# Initialize agent and graph once for reuse
agent = CardanoAgent()
graph = agent.graph

class CardanoChatbot:
    def __init__(self, thread_id: int = 0):
        self.thread_id = thread_id

    def chat(self, user_input: str) -> str:
        return chat(graph, self.thread_id, user_input)

def kickoff_cardanoAgent(thread_id: int, user_input: str):
    chatbot = CardanoChatbot(thread_id=thread_id)
    response = chatbot.chat(user_input)
    return response

if __name__ == "__main__":
    # Example usage
    thread_id = 1
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "bye"]:
            break
        response = kickoff_cardanoAgent(thread_id, user_input)
        print(f"Bot: {response}")
