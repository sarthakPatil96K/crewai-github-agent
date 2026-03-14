from crewai import Agent

agent = Agent(
    role="Test Agent",
    goal="Verify CrewAI installation",
    backstory="Testing environment setup"
)

print("CrewAI working correctly!")