from crewai import Task
from agents.repo_agent import repo_agent

repo_analysis_task = Task(
    description="""
    Analyze the given GitHub repository.
    
    Identify:
    - programming languages used
    - project structure
    - frameworks and libraries
    - main functionality of the project
    """,
    expected_output="""
    A detailed explanation of the repository structure and purpose.
    """,
    agent=repo_agent
)