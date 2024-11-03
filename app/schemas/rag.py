from pydantic import BaseModel
from typing import List

class RAGResponse(BaseModel):
    """Schema for the response from the RAG API endpoint."""
    answer: str

class RAGQueryRequest(BaseModel):
    """Schema for the request body to the RAG API endpoint."""
    question: str  
