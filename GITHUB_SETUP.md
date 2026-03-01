# GitHub Setup Guide

## Steps to Upload Your Project to GitHub

### 1. Create a New GitHub Repository
- Go to [github.com/new](https://github.com/new)
- **Repository name**: `rag-pdf-chatbot` (or your preferred name)
- **Description**: Multi-PDF RAG Chatbot - Ask questions about your PDFs using AI
- **Visibility**: Public (or Private)
- **Do NOT initialize** with README, .gitignore, or license (we have them)
- Click "Create repository"

### 2. Initialize Git Locally

Open PowerShell in your project directory:

```powershell
cd "c:\Users\srisa\Downloads\Rag chatbot\rag_chatbot"

# Initialize git repo
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: RAG PDF Chatbot v2.0 with chat history and document management"

# Rename branch to main (if needed)
git branch -M main

# Add remote repository (replace YOUR_USERNAME and your-repo-name)
git remote add origin https://github.com/YOUR_USERNAME/rag-pdf-chatbot.git

# Push to GitHub
git push -u origin main
```

### 3. Alternative: Using GitHub Desktop
1. Download [GitHub Desktop](https://desktop.github.com/)
2. Click "File" → "Clone Repository"
3. Go back to GitHub and copy your repo URL
4. Paste it in GitHub Desktop
5. Make your first commit with the message above
6. Click "Publish repository"

## Files Included

✅ **Core Application Files**
- `app.py` - Main Streamlit application (ENHANCED)
- `chat.py` - Groq API integration (ENHANCED)
- `pdf_processing.py` - PDF text extraction
- `vectorstore.py` - FAISS vector store
- `query_handler.py` - Query processing (ENHANCED)

✅ **NEW FEATURES**
- `session_manager.py` - Chat history management
- `document_manager.py` - Document tracking
- `README.md` - Comprehensive documentation
- `CHANGELOG.md` - Version history

✅ **Configuration**
- `requirements.txt` - Python dependencies
- `.env` - Environment variables (DON'T commit this!)
- `.gitignore` - Git exclusion rules

## After Uploading

1. **Add a Badge to Markdown** (optional):
```markdown
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-deployment-url.streamlit.app/)
```

2. **Enable Issues**: Click Settings → enable Issues (for bug reports)

3. **Add Topics**: Click Settings → Topics and add:
   - `rag` `chatbot` `pdf` `groq` `streamlit` `llm`

4. **Deploy on Streamlit Cloud** (optional):
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Connect your repo
   - Streamlit will automatically deploy it

## What's New in v2.0

✨ **Chat History** - Persistent conversations with timestamps
📋 **Document Management** - View, track, and manage all uploaded PDFs
⚙️ **Settings Panel** - Real-time vector store and document statistics
💬 **Export Chats** - Download conversations as text files
🔍 **Better Errors** - User-friendly error messages with guidance
📍 **Enhanced Sources** - Improved source citations and tracking

## Important Notes

⚠️ **Never commit `.env` file** - It contains your API key!
- The `.gitignore` already excludes it
- Users will need to create their own `.env` file

📦 **Large Files** - `faiss_index/` is excluded from Git
- Users can regenerate it by processing PDFs

## File Summary

```
rag-pdf-chatbot/
├── app.py (106 lines) - Main UI with chat history & document management
├── chat.py (42 lines) - Enhanced LLM responses with better formatting
├── pdf_processing.py (25 lines) - PDF extraction & chunking
├── vectorstore.py (10 lines) - FAISS vector store management
├── query_handler.py (43 lines) - Query processing with session tracking
├── session_manager.py (62 lines) - NEW: Chat history management
├── document_manager.py (65 lines) - NEW: Document tracking
├── requirements.txt - Python dependencies
├── README.md - Complete documentation
├── CHANGELOG.md - Version history
├── .gitignore - Git exclusion rules
└── .env (not tracked) - Your API key here
```

Total: **~350 lines of Python code**

## Getting Started After Clone

Users who clone your repo will:
1. Install dependencies: `pip install -r requirements.txt`
2. Create `.env` file with: `GROQ_API_KEY=your_key_here`
3. Run: `streamlit run app.py`

Done! 🚀
