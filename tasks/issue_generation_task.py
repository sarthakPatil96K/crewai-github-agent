from crewai import Task
from agents.issue_agent import issue_agent

issue_generation_task = Task(
    description="""
    Based on repository analysis, code review, and security findings,
    generate structured GitHub issues.
    """,
    expected_output="""
    A list of GitHub issues with titles and descriptions.
    """,
    agent=issue_agent
)