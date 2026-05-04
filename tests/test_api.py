from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_analyze_endpoint():
    response = client.post("/analyze", json={"text": "Safe text"})
    assert response.status_code == 200
    assert "result" in response.json()
