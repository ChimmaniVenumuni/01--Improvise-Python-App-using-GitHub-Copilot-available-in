from fastapi.testclient import TestClient
from main import app
 
client = TestClient(app)
 
def test_welcome():
    response = client.get("/api/hello")
    assert response.status_code == 200
    assert "Shaban Kaishar" in response.json()["message"]
 
def test_generate_route():
    response = client.post("/generate", json={"text": "sample input"})
    assert response.status_code == 200
    data = response.json()
    assert "tokens" in data
    assert "checksum" in data
