from app.services.crew_manager import ModerationService

system = ModerationService()


def test_safe_text(monkeypatch):
    # system = ModerationService()
    def mock_analyse_text(text):
        return {"label": "Safe", "confidence": 0.9, "reason": "mock"}
    
    monkeypatch.setattr(system, "run_analysis", mock_analyse_text)
    result = system.run_analysis("Hello friend")
    assert result["label"] in ["Safe", "Hate"]


def test_hate_text(monkeypatch):
    # system = ModerationService()
    def mock_analyse_text(text):
        return {"label": "Hate", "confidence": 0.95, "reason": "mock"}
    monkeypatch.setattr(system, "run_analysis", mock_analyse_text)
    result = system.run_analysis("Hate text")
    assert result["label"] == "Hate"
