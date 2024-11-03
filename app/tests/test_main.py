from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the RAG API"}

def test_query_rag_model():
    response = client.post("/api/v1/query/", json={"query": "What is FastAPI?"})
    assert response.status_code == 200
    assert "answer" in response.json()
