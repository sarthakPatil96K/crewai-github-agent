from crewai import Agent
from config.llm import get_llm
from tools.github_tools import index_repository_tool
 

code_review_agent = Agent(
    role="Code Review Specialist",

    goal="""
Analyze Python source code from a GitHub repository
and identify maintainability and quality issues.
""",

    backstory="""
You are a senior software engineer specializing in code quality.
You carefully inspect source files to identify problems such as
duplicate logic, long functions, bad naming conventions,
and poor maintainability.
""",

    tools=[
    index_repository_tool
    ],

    llm=get_llm(),

    verbose=True
)