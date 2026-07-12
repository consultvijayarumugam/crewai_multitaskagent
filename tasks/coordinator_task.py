from crewai import Task

from agents.coordinator import coordinator


def build_coordinator_task(question: str):

    return Task(

        description=f"""
You are responsible for understanding the customer's intent.

Customer Question:

{question}

Identify:

- Customer intent
- Whether research is required
- Any important context

Return only your analysis.
""",

        expected_output="""
Intent analysis and routing decision.
""",

        agent=coordinator

    )