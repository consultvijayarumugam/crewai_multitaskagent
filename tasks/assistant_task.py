from crewai import Task

from agents.assistant import assistant


def build_assistant_task(

        question,

        memory,

        research

):

    return Task(

        description=f"""
Customer Question

{question}

Customer Memory

{memory}

Research

{research}

Generate the best customer support response.

""",

        expected_output="""
Helpful customer support response.
""",

        agent=assistant

    )