from crewai import Agent
from tools.github_tools import get_repo_structure, get_readme
from config.llm import get_llm

repo_agent = Agent(
    role="Repository Analyzer",
    goal="Analyze GitHub repositories and summarize their structure and purpose.",
    backstory="Expert software engineer who understands project architectures.",
    tools=[get_repo_structure, get_readme],
    llm=get_llm(),
    verbose=True
)