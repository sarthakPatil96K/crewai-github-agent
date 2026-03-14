from crewai import Crew, Process

from agents.repo_agent import repo_agent
from agents.code_review_agent import code_review_agent
from agents.security_agent import security_agent
from agents.documentation_agent import documentation_agent
from agents.issue_agent import issue_agent

from tasks.repo_analysis_task import repo_analysis_task
from tasks.code_review_task import code_review_task
from tasks.security_scan_task import security_scan_task
from tasks.documentation_task import documentation_task
from tasks.issue_generation_task import issue_generation_task


def create_crew():

    crew = Crew(
        agents=[
            repo_agent,
            code_review_agent,
            security_agent,
            documentation_agent,
            issue_agent
        ],

        tasks=[
            repo_analysis_task,
            code_review_task,
            security_scan_task,
            documentation_task,
            issue_generation_task
        ],

        process=Process.sequential,
        verbose=True
    )

    return crew