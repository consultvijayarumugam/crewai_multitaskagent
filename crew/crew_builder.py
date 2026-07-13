from crewai import Crew, Process

from agents.assistant import assistant
from agents.researcher import researcher
from agents.entry_agent import entry_agent

from tasks.assistant_task import build_assistant_task
from tasks.research_task import build_research_task
from tasks.entry_task import build_entry_task


class CrewBuilder:

    @staticmethod
    def build(
        question: str,
        context: str
    ):

        # ----------------------------
        # Assistant Task
        # ----------------------------

        assistant_task = build_assistant_task(
            question=question,
            context=context
        )

        # ----------------------------
        # Research Task
        # ----------------------------

        research_task = build_research_task(
            question=question
        )

        research_task.context = [
            assistant_task
        ]

        # ----------------------------
        # Entry Task
        # ----------------------------

        entry_task = build_entry_task()

        entry_task.context = [
            assistant_task,
            research_task
        ]

        # ----------------------------
        # Crew
        # ----------------------------

        return Crew(

            agents=[
                assistant,
                researcher,
                entry_agent
            ],

            tasks=[
                assistant_task,
                research_task,
                entry_task
            ],

            process=Process.sequential,

            verbose=True,

            memory=False

        )