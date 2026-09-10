import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.abspath(os.path.join(current_dir, "../../"))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from app.core.config import settings

def load_vector_store():
    """Load the Chroma vector database using pre-configured embedding models."""
    embeddings = HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL_PATH)
    vector_db = Chroma(
        persist_directory=settings.VECTOR_DB_PATH,
        embedding_function=embeddings
    )
    return vector_db

def retrieve_documents(query: str, k: int = 4, filename: str = None):
    """
    Retrieve relevant document chunks from the vector store.
    Supports optional metadata filtering by filename to target specific documents.
    """
    vector_db = load_vector_store()
    
    # Configure search parameters, adding a metadata filter if a filename is provided
    search_kwargs = {"k": k}
    if filename:
        search_kwargs["filter"] = {"filename": filename}
        
    results = vector_db.similarity_search(query, **search_kwargs)
    return results