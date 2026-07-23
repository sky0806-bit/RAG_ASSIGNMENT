import os
import numpy as np
import cohere

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, TextLoader


# ==========================================================
# Task 1: Custom Document Loader
# ==========================================================

def load_and_chunk_document(file_path, chunk_size=300, overlap=50):
    """
    Loads a PDF or TXT document and returns text chunks.
    """

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        loader = PyPDFLoader(file_path)

    elif extension == ".txt":
        loader = TextLoader(file_path, encoding="utf-8")

    else:
        raise ValueError("Only PDF and TXT files are supported.")

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )

    chunks = splitter.split_documents(documents)

    return [chunk.page_content for chunk in chunks]


# ==========================================================
# Task 2: Custom Embedding Function
# ==========================================================

def create_embeddings(chunks, model_name="all-MiniLM-L6-v2"):
    """
    Creates embeddings for text chunks.
    """

    model = SentenceTransformer(model_name)

    embeddings = model.encode(chunks)

    return embeddings.tolist()


# ==========================================================
# Task 3: Search Function
# ==========================================================

def search_chunks(query, chunks, embeddings, k=3):
    """
    Returns top-k most relevant chunks for the query.
    """

    model = SentenceTransformer("all-MiniLM-L6-v2")

    query_embedding = model.encode([query])

    similarities = cosine_similarity(
        query_embedding,
        np.array(embeddings)
    )[0]

    top_indices = similarities.argsort()[-k:][::-1]

    top_chunks = [chunks[i] for i in top_indices]

    return top_chunks


# ==========================================================
# Task 5: Cohere Answer Generation
# ==========================================================

def generate_answer(query, context, api_key):

    co = cohere.Client(api_key)

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the provided context.

Context:
{context}

Question:
{query}
"""

    response = co.chat(
        model="command-a-03-2025",
        message=prompt
    )

    return response.text


