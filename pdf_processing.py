from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def extract_texts_from_pdfs(pdf_files):
    docs = []
    for uploaded_file in pdf_files:
        reader = PdfReader(uploaded_file)
        text = ""
        for i, page in enumerate(reader.pages):
            t = page.extract_text()
            if t:
                text += f"\n\n[Page {i+1}]\n" + t
        name = getattr(uploaded_file, "name", "uploaded_pdf")
        docs.append({"text": text, "source": name})
    return docs

def get_chunks_and_metadatas(docs, chunk_size=2000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    all_chunks, all_metadatas = [], []
    for doc in docs:
        text = doc["text"]
        source = doc["source"]
        if not text.strip():
            continue
        chunks = splitter.split_text(text)
        for idx, c in enumerate(chunks):
            all_chunks.append(c)
            all_metadatas.append({"source": source, "chunk_id": idx})
    return all_chunks, all_metadatas
