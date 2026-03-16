from crewai import Task
from agents.security_agent import security_agent

security_scan_task = Task(
    description="""
    Scan the repository for security vulnerabilities.

    Steps:

    1. Use the tool `index_repository_tool`
    to retrieve indexed source files.

    2. Analyze each file.

    Look for:
    - hardcoded API keys
    - unsafe eval()
    - subprocess usage
    - command injection
    - insecure file handling

    IMPORTANT:
    Only analyze files returned by the tool.
    Do NOT hallucinate vulnerabilities.
    Return a short summary.
    """,
    expected_output="""
    A report of potential security vulnerabilities.
    """,
    agent=security_agent
)