from crewai import Crew, Process

from agents.coordinator import coordinator
from agents.assistant import assistant
from agents.researcher import researcher

from tasks.coordinator_task import build_coordinator_task
from tasks.assistant_task import build_assistant_task
from tasks.research_task import build_research_task


class CrewBuilder:

    def build(self, question: str, history: list):

        coordinator_task = build_coordinator_task(question)

        research_task = build_research_task(question)

        assistant_task = build_assistant_task(
            question=question,
            history=history
        )

        crew = Crew(
            agents=[
                coordinator,
                researcher,
                assistant
            ],
            tasks=[
                coordinator_task,
                research_task,
                assistant_task
            ],
            process=Process.sequential,
            verbose=True
        )

        return crew