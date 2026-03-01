import streamlit as st
from dotenv import load_dotenv
from pdf_processing import extract_texts_from_pdfs, get_chunks_and_metadatas
from vectorstore import build_vector_store
from chat import answer_with_groq
from query_handler import handle_query
from session_manager import SessionManager
from document_manager import DocumentManager

load_dotenv()

def main():
    st.set_page_config("RAG PDF Chatbot", page_icon="📚", layout="wide")
    st.markdown("<h1 style='text-align:center; color:#FFB000;'>📚 Multi-PDF Chatbot</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#bbbbbb;'>Ask anything from your uploaded PDFs instantly ⚡</p>", unsafe_allow_html=True)

    # Initialize managers
    session_mgr = SessionManager()
    doc_mgr = DocumentManager()

    # Main layout
    col1, col2 = st.columns([3, 1])

    with col2:
        st.subheader("⚙️ Settings")
        
        # Document info
        if doc_mgr.vector_store_exists():
            st.success("✅ Vector Store Ready")
            docs = doc_mgr.get_documents()
            if docs:
                st.metric("Documents", len(docs))
                st.metric("Total Chunks", doc_mgr.get_total_chunks())
        else:
            st.info("📤 Upload PDFs to get started")

    # Sidebar for PDF uploads
    with st.sidebar:
        st.title("📁 Upload & Manage PDFs")
        
        pdf_docs = st.file_uploader(
            "Select PDF files", 
            accept_multiple_files=True,
            key="pdf_uploader"
        )
        
        if st.button("🚀 Process PDFs", use_container_width=True):
            if not pdf_docs:
                st.warning("Upload at least one PDF.")
            else:
                with st.spinner("Processing PDFs..."):
                    try:
                        docs = extract_texts_from_pdfs(pdf_docs)
                        chunks, metadatas = get_chunks_and_metadatas(docs)
                        if chunks:
                            build_vector_store(chunks, metadatas)
                            
                            # Track documents
                            for pdf in pdf_docs:
                                doc_mgr.add_document(
                                    pdf.name,
                                    len([m for m in metadatas if m.get("source") == pdf.name]),
                                    pdf.size
                                )
                            
                            st.success(f"✔️ Processed {len(pdf_docs)} PDF(s)")
                        else:
                            st.error("No text extracted from PDFs.")
                    except Exception as e:
                        st.error(f"Error processing PDFs: {str(e)}")
        
        st.divider()
        
        # Manage uploaded documents
        if doc_mgr.get_documents():
            st.subheader("📋 Uploaded Documents")
            doc_info = doc_mgr.get_document_info()
            
            for doc_name, info in list(doc_info.items()):
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.text(f"📄 {doc_name}")
                    st.caption(f"Chunks: {info['chunks']} | Size: {info['size'] / 1024:.1f}KB")
                with col2:
                    if st.button("🗑️", key=f"del_{doc_name}"):
                        doc_mgr.remove_document(doc_name)
                        st.warning(f"⚠️ Note: Rebuild vector store to fully remove '{doc_name}'")
        
        st.divider()
        
        # Chat history controls
        st.subheader("💬 Conversation")
        if st.button("🔄 Clear Chat History", use_container_width=True):
            session_mgr.clear_history()
            st.success("Chat history cleared!")
        
        # Export chat
        if session_mgr.get_chat_history():
            chat_export = session_mgr.export_chat()
            st.download_button(
                label="📥 Export Chat",
                data=chat_export,
                file_name="chat_export.txt",
                mime="text/plain",
                use_container_width=True
            )

    # Main content area with chat history
    st.subheader("💬 Chat")
    
    # Display chat history
    for msg in session_mgr.get_chat_history():
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg.get("sources"):
                st.caption(f"🔗 Sources: {', '.join(msg['sources'])}")

    # Input area
    question = st.text_input("💬 Enter your question here")
    if question:
        if not doc_mgr.vector_store_exists():
            st.error("❌ No vector store found. Upload and process PDFs first.")
        else:
            with st.spinner("Searching and generating answer..."):
                handle_query(question)

if __name__ == "__main__":
    main()
