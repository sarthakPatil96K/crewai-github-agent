from crewai import Task
from agents.code_review_agent import code_review_agent


code_review_task = Task(
    description="""
Perform repository-wide code review.

Steps:

1. Use the tool `index_repository_tool`
   to retrieve indexed source code.

2. Review each file in the index.

Identify:
- bad coding practices
- duplicate code
- long functions
- maintainability issues
- poor naming conventions

IMPORTANT:
Only analyze first 5 files returned by the tool.
Do NOT include full code in the response.
Summarize issues only.
""",

    expected_output="""
A concise markdown report describing:

- file name
- detected issue
- explanation
- suggested fix
""",

    agent=code_review_agent
)