from crewai import Task
from agents.documentation_agent import documentation_agent

documentation_task = Task(
    description="""
    Analyze the project documentation.

    Improve:
    - README clarity
    - installation instructions
    - usage examples
    """,
    expected_output="""
    Improved documentation suggestions.
    """,
    agent=documentation_agent
)