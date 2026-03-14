from crewai import Agent
from config.llm import get_llm

documentation_agent = Agent(
    role="Documentation Expert",
    goal="Improve project documentation and README files",
    backstory=(
        "You are a technical writer specializing in writing clear "
        "software documentation and developer guides."
    ),
    verbose=True,
    llm=get_llm()
)