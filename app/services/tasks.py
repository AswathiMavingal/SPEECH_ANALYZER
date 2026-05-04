from crewai import Task

from app.models.schemas import HateAnalysis


class TaskFactory:
    def analysis_task(self, agent, user_text):
        return Task(
            description=(
                "Analyze the following text strictly and independently: \n\n"
                "TEXT TO ANALYZE: '{text}' \n\n"
                "STEPS:\n"
                "1. Identify language targeting protected groups (race, religion, gender, etc.).\n"
                "2. Check for dehumanizing language or threats.\n"
                "3. Evaluate context to avoid false positives.\n"
                "4. Final classification must be based ONLY on the text above."
            ),
            expected_output="A JSON object containing label, confidence, and reason.",
            agent=agent,
            output_pydantic=HateAnalysis,
        )
