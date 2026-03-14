from crewai import Task
from agents.repo_agent import repo_agent

repo_analysis_task = Task(
    description="""
Analyze the GitHub repository using available tools.

Steps:
1. Use the tool to get repository structure
2. Read the README file
3. Identify:
   - programming languages
   - main folders
   - project purpose

Repository URL: {repo_url}

Return output in JSON format:

{
 "languages": [],
 "folders": [],
 "purpose": ""
}

Do NOT hallucinate information.
Only use the tool outputs.
Limit response to 200 words.
""",
    expected_output="JSON summary of the repository",
    agent=repo_agent
)