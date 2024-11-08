from fastapi import FastAPI
from app.api.v1 import query_route
from app.core.config import settings

app = FastAPI(
    title="RAG FastAPI Docs",
    description="A FastAPI implementation of RAG (Retrieval Augmented Generation)",
    version="1.0.0"
)

# Include versioned routes
app.include_router(query_route.router, prefix="/api/v1")

