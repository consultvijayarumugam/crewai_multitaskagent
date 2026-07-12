from crewai import Task

from agents.researcher import researcher


def build_research_task(question):

    return Task(

        description=f"""
Research the following question.

Question

{question}

Return concise findings.

""",

        expected_output="""
Verified research summary.
""",

        agent=researcher

    )