from crewai import Task
from agents.security_agent import security_agent

security_scan_task = Task(
    description="""
    Scan the repository for security vulnerabilities.

    Look for:
    - exposed API keys
    - insecure dependencies
    - unsafe coding patterns
    """,
    expected_output="""
    A report of potential security vulnerabilities.
    """,
    agent=security_agent
)