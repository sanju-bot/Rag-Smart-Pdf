from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def build_vector_store(chunks, metadatas, persist_directory="faiss_index"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vs = FAISS.from_texts(chunks, embedding=embeddings, metadatas=metadatas)
    vs.save_local(persist_directory)
    return vs

def load_vector_store(persist_directory="faiss_index"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local(persist_directory, embeddings, allow_dangerous_deserialization=True)
