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
        context: str,
        use_research: bool = True
    ):

        assistant_task = build_assistant_task(
            question,
            context
        )

        tasks = [assistant_task]

        if use_research:

            research_task = build_research_task(question)
            research_task.context = [assistant_task]

            tasks.append(research_task)

            entry_task = build_entry_task()
            entry_task.context = [
                assistant_task,
                research_task
            ]

        else:

            entry_task = build_entry_task()
            entry_task.context = [
                assistant_task
            ]

        tasks.append(entry_task)

        agents = [
            assistant,
            entry_agent
        ]

        if use_research:

            agents = [
                assistant,
                researcher,
                entry_agent
            ]

        return Crew(

            agents=agents,

            tasks=tasks,

            process=Process.sequential,

            verbose=True,

            memory=False

        )