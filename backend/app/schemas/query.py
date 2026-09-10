from pydantic import BaseModel
from typing import Optional

class QueryRequest(BaseModel):
    question: str
    filename: Optional[str] = None  # Optional filename filter for targeted search

class QueryResponse(BaseModel):
    answer: str
    sources: list[str]