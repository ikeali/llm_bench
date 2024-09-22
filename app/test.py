from fastapi.testclient import TestClient
from main import app  # Adjust import based on your structure

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "This is just a test"}

def test_create_llm():
    response = client.post("/llms/", json={"name": "Test LLM", "description": "A test model"})
    assert response.status_code == 200
    assert "id" in response.json()  # Check if ID is returned
