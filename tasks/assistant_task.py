from crewai import Task

from agents.assistant import assistant


def build_assistant_task(question: str, history: list):

    return Task(

        description=f"""
Customer Question:

{question}

Conversation History:

{history}

Using the available context,
generate the best possible customer support response.

If previous conversations are useful,
use them naturally.

Be concise, accurate and professional.
""",

        expected_output="""
Final response for the customer.
""",

        agent=assistant

    )