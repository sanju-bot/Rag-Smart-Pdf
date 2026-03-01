# Changelog

All notable changes to this project will be documented in this file.

## [2.0.0] - 2026-03-01

### Added
- 💬 **Chat History Management** - Persistent conversation history with timestamps
  - `session_manager.py` - New module for session and chat history tracking
  - Display conversation history in main chat area
  - Clear chat history with one click
  - Export chat conversations as text files
  
- 📋 **Document Management** - Better control over uploaded documents
  - `document_manager.py` - New module for document tracking
  - List all uploaded documents with metadata
  - View document statistics (chunks, file size)
  - Delete documents from the system
  - Track document upload timestamps
  - Store metadata in JSON format
  
- ⚙️ **Settings Panel** - Real-time status information
  - Vector store availability indicator
  - Document count display
  - Total chunks counter
  - Upload status badges
  
- 📍 **Enhanced Source Display** - Better citation formatting
  - Expandable sources section in chat
  - Numbered source list
  - Source links in exported chats
  
- 🔧 **Improved Error Handling**
  - User-friendly error messages with guidance
  - Better exception handling in query processing
  - Validation checks before processing
  
- 📥 **Chat Export Feature**
  - Download conversations as formatted text files
  - Includes timestamps and sources
  - One-click export button

### Changed
- Enhanced `app.py` with new UI components
  - Sidebar reorganization with document management
  - Settings panel on main page
  - Chat history display area
  - Better layout using columns
  
- Improved `chat.py`
  - Better source display with expander
  - Enhanced error handling
  - Cleaner output formatting
  
- Enhanced `query_handler.py`
  - Integration with session manager
  - Better error messages
  - Session tracking for all queries

### Fixed
- Better handling of missing vector stores
- Improved error messages for better user guidance
- Fixed metadata tracking for documents

### Files Added
- `session_manager.py` - Chat history and session management
- `document_manager.py` - Document and metadata management
- `README.md` - Comprehensive documentation
- `.gitignore` - Git exclusion rules
- `CHANGELOG.md` - This file

## [1.0.0] - Initial Release

### Features
- Multi-PDF upload capability
- PDF text extraction with page tracking
- Text chunking with configurable parameters
- FAISS vector store for semantic search
- Groq API integration for LLM responses
- Streamlit web interface
- Source attribution for answers
