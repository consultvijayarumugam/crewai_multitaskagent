from crewai import Task

from agents.researcher import researcher


def build_research_task(question: str):

    return Task(

        description=f"""
Research the following question if external information is needed.

Question:

{question}

Provide concise, reliable findings.
""",

        expected_output="""
Research summary.
""",

        agent=researcher

    )