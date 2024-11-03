# app/api/v1/query_route.py

from fastapi import APIRouter, HTTPException
from app.schemas.rag import RAGQueryRequest, RAGResponse
from app.services.rag_services import RAGService

router = APIRouter()
rag_service = RAGService()

@router.post("/query/", response_model=RAGResponse)
async def query_endpoint(request: RAGQueryRequest):
    """
    Endpoint to query the RAG service.
    
    - **question**: The question to ask the RAG service.
    """
    try:
        response = rag_service.query_data(request)  # Pass the request body directly
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
