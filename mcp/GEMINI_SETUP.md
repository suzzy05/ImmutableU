# 🚀 Gemini API Setup Guide

This project has been configured to use **Google Gemini API** instead of OpenAI.

## 📋 Prerequisites

1. Google Cloud Account
2. Gemini API Key

## 🔑 Getting Your Gemini API Key

### Step 1: Visit Google AI Studio
Go to: https://makersuite.google.com/app/apikey

### Step 2: Create API Key
1. Click on "Get API Key"
2. Select or create a Google Cloud project
3. Click "Create API Key"
4. Copy your API key

### Step 3: Configure Environment
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Add your Gemini API key:
   ```env
   GOOGLE_API_KEY=your_actual_gemini_api_key_here
   ```

## 📦 Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Setup vector databases (one-time):
   ```bash
   uvicorn app.main:app --reload
   
   # Then call the setup endpoint
   curl -X GET "http://localhost:8000/training/setup_all_vector_dbs" \
        -H "Secret-token: unihack25"
   ```

## 🤖 Models Used

- **Chat Model**: `gemini-1.5-flash` (Fast and cost-effective)
- **Embeddings**: `models/embedding-001` (For vector database)

## 💰 Pricing

Gemini 1.5 Flash is **FREE** up to:
- 15 requests per minute
- 1 million tokens per minute
- 1,500 requests per day

Perfect for development and small-scale production!

## ✅ Benefits of Gemini

✅ **Free Tier** - No credit card required  
✅ **Fast** - Lower latency than GPT-4  
✅ **Multilingual** - Excellent support for multiple languages  
✅ **Long Context** - Up to 1M tokens context window  
✅ **Multimodal** - Can handle text, images, and more  

## 🧪 Testing

Test the legal assistant:
```bash
curl -X POST "http://localhost:8000/legalquery/" \
  -H "Content-Type: application/json" \
  -H "Secret-token: unihack25" \
  -d '{
    "thread_id": 1,
    "domain": "property",
    "user_input": "What are property rights in Sri Lanka?",
    "lang": "en"
  }'
```

Test the Cardano assistant:
```bash
curl -X POST "http://localhost:8000/query/" \
  -H "Content-Type: application/json" \
  -H "Secret-token: unihack25" \
  -d '{
    "thread_id": 1,
    "user_input": "Explain Cardano blockchain",
    "lang": "en"
  }'
```

## 🔧 Configuration

All settings are in `app/core/config.py`:
- `GEMINI_MODEL`: The chat model to use
- `GEMINI_EMBEDDING_MODEL`: For document embeddings
- `TEMPERATURE`: Controls response randomness (0.1 = focused)

## 📚 Documentation

- Gemini API Docs: https://ai.google.dev/docs
- LangChain Gemini: https://python.langchain.com/docs/integrations/chat/google_generative_ai

## 🆘 Troubleshooting

**API Key Error:**
- Verify your API key is correct
- Check if API is enabled in Google Cloud Console

**Rate Limit:**
- Free tier has limits (15 req/min)
- Upgrade to paid tier if needed

**Import Error:**
- Run: `pip install -U langchain-google-genai`

---

**Ready to go!** 🎉 Your AI assistant now runs on Google Gemini!
