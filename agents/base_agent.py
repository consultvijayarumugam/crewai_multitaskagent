from crewai import Agent

from core.llm import llm


def create_agent(
    role: str,
    goal: str,
    backstory: str,
    tools=None,
    allow_delegation=False,
):

    return Agent(
        role=role,
        goal=goal,
        backstory=backstory,
        llm=llm,
        tools=tools or [],
        verbose=True,
        allow_delegation=allow_delegation,
    )