from crewai import Task

from agents.coordinator import coordinator


def build_coordinator_task(question: str):

    return Task(

        description=f"""
Understand the customer request.

Customer Question:

{question}

Decide:

1. Can memory answer?

2. Should the assistant answer?

3. Is web research required?

""",

        expected_output="""
Decision regarding how the request should be handled.
""",

        agent=coordinator

    )