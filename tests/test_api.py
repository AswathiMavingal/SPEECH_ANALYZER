from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_analyze_endpoint(monkeypatch):
    def mock_analyse_text(self, text):
        return {"label": "Safe", "confidence": 0.9, "reason": "mock"}
    from app.services.crew_manager import ModerationService
    
    monkeypatch.setattr(ModerationService, "run_analysis", mock_analyse_text)
    response = client.post("/analyze", json={"text": "Safe text"})
    assert response.status_code == 200
    # assert "result" in response.json()
    assert response.json()["result"]["label"] == "Safe"
