import streamlit as st
from datetime import datetime
import json
import os

class SessionManager:
    """Manage chat history and conversation sessions"""
    
    def __init__(self):
        self.session_file = "chat_sessions.json"
        self.init_session_state()
    
    def init_session_state(self):
        """Initialize Streamlit session state for chat history"""
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
        if "current_session_id" not in st.session_state:
            st.session_state.current_session_id = datetime.now().isoformat()
        if "document_count" not in st.session_state:
            st.session_state.document_count = 0
    
    def add_message(self, role, content, sources=None):
        """Add a message to chat history"""
        message = {
            "timestamp": datetime.now().isoformat(),
            "role": role,
            "content": content,
            "sources": sources or []
        }
        st.session_state.chat_history.append(message)
    
    def get_chat_history(self):
        """Get current chat history"""
        return st.session_state.chat_history
    
    def clear_history(self):
        """Clear chat history"""
        st.session_state.chat_history = []
        st.session_state.current_session_id = datetime.now().isoformat()
    
    def export_chat(self):
        """Export chat history as formatted text"""
        if not st.session_state.chat_history:
            return "No chat history to export."
        
        export_text = f"Chat Session - {st.session_state.current_session_id}\n"
        export_text += "=" * 60 + "\n\n"
        
        for msg in st.session_state.chat_history:
            timestamp = msg["timestamp"].split("T")[1][:5]
            role = msg["role"].upper()
            export_text += f"[{timestamp}] {role}:\n"
            export_text += msg["content"] + "\n"
            
            if msg.get("sources"):
                export_text += f"Sources: {', '.join(msg['sources'])}\n"
            
            export_text += "\n" + "-" * 60 + "\n\n"
        
        return export_text
