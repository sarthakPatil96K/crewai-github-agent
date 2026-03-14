from crewai import Task
from agents.code_review_agent import code_review_agent

code_review_task = Task(
    description="""
    Review the repository code and identify:

    - bad coding practices
    - duplicate code
    - long functions
    - maintainability issues
    """,
    expected_output="""
    A list of code improvement suggestions.
    """,
    agent=code_review_agent
)