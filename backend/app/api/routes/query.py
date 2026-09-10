import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.abspath(os.path.join(current_dir, "../../../"))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from fastapi import APIRouter, HTTPException
from app.schemas.query import QueryRequest, QueryResponse
from app.services.generation import generate_rag_answer

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
async def query_rag_assistant(request: QueryRequest):
    """
    Endpoint to handle user queries, retrieve relevant documents,
    and generate a grounded RAG response using the LLM.
    """
    try:
        if not request.question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty.")
        
        # Pass the optional filename filter to the generation/retrieval pipeline if needed
        answer, sources = generate_rag_answer(request.question, filename=request.filename)
        return QueryResponse(answer=answer, sources=sources)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
async def health_check():
    """Health check endpoint to verify backend status."""
    return {"status": "healthy"}