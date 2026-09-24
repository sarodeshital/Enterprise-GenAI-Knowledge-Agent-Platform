from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_query():
    response = client.post("/query", json={"question": "How should secrets be stored?"})
    assert response.status_code == 200
    body = response.json()
    assert "answer" in body
    assert "sources" in body
