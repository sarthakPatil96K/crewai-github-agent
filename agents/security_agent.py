from crewai import Agent
from config.llm import get_llm

security_agent = Agent(
    role="Security Analyst",
    goal="Detect vulnerabilities and insecure coding patterns",
    backstory=(
        "You are a cybersecurity expert specializing in identifying "
        "security flaws, secrets in code, and unsafe dependencies."
    ),
    verbose=True,
    llm=get_llm()
)