from crewai import Agent
from config.llm import get_llm

code_review_agent = Agent(
    role="Code Review Specialist",
    goal="Review source code and suggest improvements",
    backstory=(
        "You are a senior software engineer specializing in "
        "clean code, maintainability, and software best practices."
    ),
    verbose=True,
    llm=get_llm()
)