from crewai import Agent
from config.llm import get_llm

agent = Agent(
    role="Test Agent",
    goal="Verify CrewAI installation",
    backstory="Testing environment setup",
    llm=get_llm()
)

print("CrewAI + Groq working!")