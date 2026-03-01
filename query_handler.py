from collections import defaultdict
from vectorstore import load_vector_store
from chat import answer_with_groq
from session_manager import SessionManager
import streamlit as st

def handle_query(question, index_path="faiss_index", top_k=10):
    """Handle user query with enhanced error handling and session tracking"""
    
    session_mgr = SessionManager()
    
    try:
        vs = load_vector_store(index_path)
    except Exception as e:
        st.error("❌ Vector index not found. Upload & process PDFs first.")
        return

    try:
        docs_and_scores = vs.similarity_search_with_score(question, k=top_k)
    except Exception:
        docs = vs.similarity_search(question, k=top_k)
        docs_and_scores = [(d, None) for d in docs]

    grouped = defaultdict(list)
    for item, score in docs_and_scores:
        src = item.metadata.get("source") if hasattr(item, "metadata") else "Unknown"
        grouped[src].append((item.page_content, score))

    ctx_pieces, sources_included = [], []
    for src, chunk_list in grouped.items():
        chunk_list_sorted = sorted(chunk_list, key=lambda x: (float('inf') if x[1] is None else x[1]))
        for c, _ in chunk_list_sorted[:3]:
            ctx_pieces.append(f"[Source: {src}]\n{c}")
        sources_included.append(src)

    context = "\n\n---\n\n".join(ctx_pieces)
    if not context.strip():
        st.warning("⚠️ No relevant content found in the index.")
        return

    # Add user query to session
    session_mgr.add_message("user", question, sources_included)
    
    # Generate answer
    answer = answer_with_groq(context, question, show_sources=sources_included)
    
    # Add answer to session
    if answer:
        session_mgr.add_message("assistant", answer, sources_included)
