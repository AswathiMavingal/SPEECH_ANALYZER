import logging

from crewai import Crew

from .agents import AgentFactory
from .tasks import TaskFactory


class ModerationService:
    def __init__(self):
        self.agent_factory = AgentFactory()
        self.task_factory = TaskFactory()

    def run_analysis(self, user_text: str):
        auditor = self.agent_factory.moderator_agent()
        task = self.task_factory.analysis_task(auditor, user_text)

        crew = Crew(
            agents=[auditor], tasks=[task], verbose=False, memory=False, cache=False
        )
        try:
            result = crew.kickoff(inputs={"text": user_text})
            if result.pydantic:
                return result.pydantic.model_dump()
            return {
                "label": "Error",
                "confidence": 0,
                "reason": "Failed to parse LLM response",
            }
        except ConnectionError:
            # Specifically handle if Ollama is offline
            return {
                "label": "Error",
                "confidence": 0,
                "reason": "Ollama server is unreachable",
            }
        except Exception as e:
            logging.error(f"Moderation Error: {str(e)}")
            return {
                "label": "Error",
                "confidence": 0,
                "reason": "Internal analysis engine failure.",
            }
