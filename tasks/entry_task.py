from crewai import Task

from agents.entry_agent import entry_agent


def build_entry_task():

    return Task(

        description="""
Validate the conversation.

Ensure all required responses exist.

Return ONLY

Conversation validated successfully.
""",

        expected_output="""
Conversation validated successfully.
""",

        agent=entry_agent

    )