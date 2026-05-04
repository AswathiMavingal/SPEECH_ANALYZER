from crewai import LLM, Agent
import os
from dotenv import load_dotenv

load_dotenv()



class AgentFactory:
    def __init__(self):
        self.llm = LLM(
            model=os.getenv("MODEL"),  #"ollama/llama3",
            base_url=os.getenv("OLLAMA_URL"), #"http://localhost:11434",
            temperature=0.0,
            top_p=0.1,
        )

    def moderator_agent(self):
        return Agent(
            role="Policy Compliance Auditor",
            goal="Objectively categorize text based on safety guidelines without bias.",
            backstory=(
                "You are an unbiased AI classification engine. Your role is to map "
                "input text to specific policy labels. You do not engage in conversation; "
                "you only report metadata properties of the provided string."
            ),
            llm=self.llm,
            verbose=False,
            allow_delegation=False,
        )
