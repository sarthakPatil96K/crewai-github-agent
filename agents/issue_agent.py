from crewai import Agent
from config.llm import get_llm

issue_agent = Agent(
    role="Issue Manager",
    goal="Create structured GitHub issues for identified problems",
    backstory=(
        "You are a DevOps engineer responsible for organizing "
        "software improvement tasks and managing GitHub issues."
    ),
    verbose=True,
    llm=get_llm()
)