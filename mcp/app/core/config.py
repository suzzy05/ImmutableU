import os
from dotenv import load_dotenv
from blockfrost import ApiUrls

# Load environment variables from .env file
load_dotenv()

# Google Gemini Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Blockfrost API Configuration
BLOCKFROST_PROJECT_ID  = os.getenv("BLOCKFROST_PROJECT_ID")
BLOCKFROST_BASE_URL = os.getenv("BLOCKFROST_BASE_URL", ApiUrls.preview.value)

# ChromaDB Configuration
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "./chroma_data")

# LLM Configuration
GEMINI_MODEL = "models/gemini-2.5-flash"  # Latest fast model
GEMINI_EMBEDDING_MODEL = "models/embedding-001"  # Compatible with existing vector DBs
TEMPERATURE = 0.1