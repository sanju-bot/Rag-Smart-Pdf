# 📚 RAG PDF Chatbot

An intelligent chatbot application that allows users to upload PDF documents and ask questions about them using Retrieval-Augmented Generation (RAG) with the Groq API.

**Current Version**: v2.0.1 ✨ (Bug fixes & UI improvements)

## ✨ Features

### Core Features
- 📄 **Multi-PDF Upload**: Upload and process multiple PDF files simultaneously
- 🤖 **AI-Powered Q&A**: Ask questions about your documents using Groq's Llama model
- 🔍 **Semantic Search**: Intelligent document retrieval using embeddings
- 📍 **Source Tracking**: See which documents were used to answer your questions

### Enhanced Features (v2.0+)
- 💬 **Chat History**: Persistent conversation history with timestamps
- 📋 **Document Management**: List, view details, and remove uploaded documents
- 📊 **Vector Store Stats**: Monitor total documents and chunks processed
- 📥 **Export Chat**: Download entire chat conversations as text files
- 🔄 **Clear History**: Reset conversations with one click
- ⚠️ **Better Error Handling**: User-friendly error messages with guidance

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- GROQ API Key (get one at [console.groq.com](https://console.groq.com))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/rag-pdf-chatbot.git
cd rag-pdf-chatbot
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
Create a `.env` file in the project root:
```
GROQ_API_KEY=your_actual_api_key_here
```

### Running the Application

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 📖 How to Use

1. **Upload PDFs**: Click "Select PDF files" in the sidebar to choose your documents
2. **Process PDFs**: Click "🚀 Process PDFs" to extract text and build the vector store
3. **Ask Questions**: Type your question in the chat input field
4. **View Results**: See the AI-generated answer with source citations
5. **Manage Documents**: Remove documents from the list if needed
6. **Export Chat**: Download your conversation as a text file

## 📁 Project Structure

```
rag_chatbot/
├── app.py                  # Main Streamlit application
├── chat.py                 # Groq API interaction & answer generation
├── pdf_processing.py       # PDF text extraction & chunking
├── vectorstore.py          # FAISS vector store management
├── query_handler.py        # Query processing & retrieval
├── session_manager.py      # Chat history & session management (NEW)
├── document_manager.py     # Document tracking & metadata (NEW)
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not in git)
└── faiss_index/           # Vector store storage
    ├── index.faiss        # FAISS index file
    └── documents_metadata.json  # Document tracking
```

## 🔧 Key Components

### Session Manager (`session_manager.py`)
Handles chat history and conversation management:
- Add/retrieve messages with timestamps
- Export conversations to text format
- Clear chat history
- Store sources with each message

### Document Manager (`document_manager.py`)
Manages uploaded documents and metadata:
- Track document information (chunks, size, upload time)
- List all uploaded documents
- Remove document metadata
- Store metadata persistently

### Enhanced App (`app.py`)
Improved UI with:
- Settings panel showing vector store status
- Document management interface
- Chat history display
- Export functionality

## 🔌 Configuration

### Model Settings
Edit `chat.py` to change:
```python
model="llama-3.1-8b-instant"    # Change model
temperature=0.2                  # Adjust creativity (0.0-1.0)
```

### Chunking Parameters
Edit `pdf_processing.py`:
```python
chunk_size=2000        # Size of text chunks
chunk_overlap=200      # Overlap between chunks
```

### Retrieval Settings
Edit `query_handler.py`:
```python
top_k=10              # Number of documents to retrieve
```

## 📊 Performance Tips

- **Large PDFs**: Split into smaller files for better processing
- **Search Speed**: Adjust `top_k` parameter to balance quality vs speed
- **Memory Usage**: Process documents in batches if you have many PDFs

## 🐛 Troubleshooting

### "Vector index not found"
- Ensure you've uploaded and processed PDFs before asking questions
- Check that `faiss_index/` directory exists

### "Invalid API Key"
- Verify your GROQ_API_KEY in the `.env` file
- Generate a new key at [console.groq.com](https://console.groq.com)

### Poor Answer Quality
- Try adjusting the question phrasing
- Ensure PDFs contain relevant content
- Reduce `top_k` for more focused results

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the web framework
- [Groq](https://groq.com/) for the LLM API
- [LangChain](https://python.langchain.com/) for document processing
- [FAISS](https://github.com/facebookresearch/faiss) for vector search
