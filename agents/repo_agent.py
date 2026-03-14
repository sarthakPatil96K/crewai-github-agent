from crewai import Agent
from config.llm import get_llm

repo_agent = Agent(
    role="Repository Analyzer",
    goal="Understand repository structure and identify project components",
    backstory=(
        "You are an experienced software architect who analyzes "
        "GitHub repositories to understand structure, frameworks, "
        "languages, and project design."
    ),
    verbose=True,
    llm=get_llm()
)