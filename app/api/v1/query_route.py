from fastapi import APIRouter, HTTPException, Depends
from services.rag_services import RAGService
router = APIRouter()

@router.post("/rag/")
def query_rag_model(query: str, service: RAGService = Depends()):
    try:
        response = service.query_data(query)
        return {"answer": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
