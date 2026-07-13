from crewai import Agent, Task, Crew, Process
from core.llm import llm

agent = Agent(
    role="Tester",
    goal="Say hello",
    backstory="You are a test agent.",
    llm=llm,
    verbose=True,
)

task = Task(
    description="Say hello",
    expected_output="Hello",
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential,
)

print(crew.kickoff())