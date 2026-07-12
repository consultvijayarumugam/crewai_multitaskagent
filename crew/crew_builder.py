from crewai import Crew

from tasks.coordinator_task import build_coordinator_task
from tasks.assistant_task import build_assistant_task
from tasks.research_task import build_research_task


class CrewBuilder:

    def build(

        self,

        question,

        memory

    ):

        coordinator = build_coordinator_task(question)

        researcher = build_research_task(question)

        assistant = build_assistant_task(

            question,

            memory,

            researcher

        )

        return Crew(

            agents=[

                coordinator.agent,

                researcher.agent,

                assistant.agent

            ],

            tasks=[

                coordinator,

                researcher,

                assistant

            ],

            verbose=True

        )