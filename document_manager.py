import streamlit as st
import os
import json
from pathlib import Path

class DocumentManager:
    """Manage uploaded documents and vector store"""
    
    def __init__(self, index_path="faiss_index"):
        self.index_path = index_path
        self.metadata_file = os.path.join(index_path, "documents_metadata.json")
        self.init_metadata()
    
    def init_metadata(self):
        """Initialize document metadata"""
        if "uploaded_docs" not in st.session_state:
            st.session_state.uploaded_docs = self.load_metadata()
    
    def load_metadata(self):
        """Load document metadata from file"""
        if os.path.exists(self.metadata_file):
            try:
                with open(self.metadata_file, "r") as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_metadata(self):
        """Save document metadata to file"""
        os.makedirs(self.index_path, exist_ok=True)
        with open(self.metadata_file, "w") as f:
            json.dump(st.session_state.uploaded_docs, f, indent=2)
    
    def add_document(self, filename, chunk_count, file_size):
        """Add document to registry"""
        st.session_state.uploaded_docs[filename] = {
            "chunks": chunk_count,
            "size": file_size,
            "uploaded_at": str(__import__('datetime').datetime.now())
        }
        self.save_metadata()
    
    def remove_document(self, filename):
        """Remove document from registry"""
        if filename in st.session_state.uploaded_docs:
            del st.session_state.uploaded_docs[filename]
            self.save_metadata()
            return True
        return False
    
    def get_documents(self):
        """Get list of all uploaded documents"""
        return list(st.session_state.uploaded_docs.keys())
    
    def get_document_info(self):
        """Get detailed info about all documents"""
        return st.session_state.uploaded_docs
    
    def get_total_chunks(self):
        """Get total number of chunks across all documents"""
        return sum(doc["chunks"] for doc in st.session_state.uploaded_docs.values())
    
    def vector_store_exists(self):
        """Check if vector store exists"""
        return os.path.exists(self.index_path) and os.path.exists(
            os.path.join(self.index_path, "index.faiss")
        )
