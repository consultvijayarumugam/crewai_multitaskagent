from crewai import Task

from agents.researcher import researcher


def build_research_task(question: str):

    return Task(

        description=f"""
You are the Internet Research Specialist.

------------------------------------------------
CUSTOMER QUESTION
------------------------------------------------

{question}

------------------------------------------------
INSTRUCTIONS
------------------------------------------------

1. Review the Assistant's previous response.

2. Decide whether internet verification is required.

3. If the answer is already correct and does not
need current information, confirm it.

4. If current or updated information is required,
use the Internet Search Tool.

5. Improve the answer whenever necessary.

6. Always provide the final verified answer.

Be concise, professional and accurate.

""",

        expected_output="""
A verified customer support response based on
internet research whenever necessary.
""",

        agent=researcher

    )