from groq import Groq
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

def answer_with_groq(context, question, show_sources=None):
    """Generate answer using Groq API with streaming and source tracking"""
    try:
        stream = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            temperature=0.2,
            stream=True,
            messages=[
                {"role": "system", "content": "You are a helpful PDF question answering expert."},
                {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{question}"}
            ]
        )

        answer_box = st.empty()
        full_answer = ""
        for chunk in stream:
            delta = chunk.choices[0].delta.content or ""
            full_answer += delta
            answer_box.markdown(full_answer)

        # Display sources with better formatting
        if show_sources:
            with st.expander("📚 Sources Used", expanded=True):
                for idx, source in enumerate(show_sources, 1):
                    st.markdown(f"**{idx}. {source}**")
            
            full_answer += f"\n\n**Sources:** {', '.join(show_sources)}"

        return full_answer
    
    except Exception as e:
        st.error(f"Error generating answer: {str(e)}")
        return None
