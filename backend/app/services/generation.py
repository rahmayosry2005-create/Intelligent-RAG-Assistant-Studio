import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.abspath(os.path.join(current_dir, "../../"))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from openai import OpenAI
from app.core.config import settings
from app.services.retrieval import retrieve_documents

def generate_rag_answer(query: str, filename: str = None):
    """
    Generate a RAG-based answer using retrieved document context and an LLM via OpenRouter.
    Supports optional metadata filtering by filename.
    """
    api_key = settings.OPENROUTER_API_KEY or os.getenv("OPENROUTER_API_KEY")
    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    
    # Retrieve relevant documents, passing the optional filename filter
    docs = retrieve_documents(query, k=4, filename=filename)
    
    # Extract context and unique sources from the retrieved chunks
    context = "\n\n".join([doc.page_content for doc in docs])
    
    # Safely extract filename from metadata (supporting both 'filename' and 'file_name')
    sources = list(set([
        doc.metadata.get('filename') or doc.metadata.get('file_name', 'Unknown') 
        for doc in docs
    ]))
    
    prompt = f"""You are a professional research assistant. Answer the user's question accurately using ONLY the provided context below. If the answer cannot be found in the context, state that you don't know. Always cite your sources.

Context:
{context}

Question: {query}

Answer (with source citations):"""

    completion = client.chat.completions.create(
        model="meta-llama/llama-3.3-70b-instruct",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.1,
        max_tokens=250
    )
    
    answer = completion.choices[0].message.content
    return answer, sources