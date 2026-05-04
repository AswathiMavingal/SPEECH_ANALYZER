from app.services.crew_manager import ModerationService

system = ModerationService()


def test_safe_text():
    result = system.run_analysis("Hello friend")
    assert result["label"] in ["Safe", "Hate"]


def test_hate_text():
    result = system.run_analysis("Hate text")
    assert result["label"] == "Hate"
