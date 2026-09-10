from pydantic import BaseModel, Field
from typing import Optional

class QueryRequest(BaseModel):
    question: str = Field(..., min_length=1, description="The question cannot be empty")
    filename: Optional[str] = None  # Optional filename filter for targeted search

class QueryResponse(BaseModel):
    answer: str
    sources: list[str]