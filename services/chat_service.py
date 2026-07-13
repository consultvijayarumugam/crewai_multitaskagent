import time

from crew.crew_builder import CrewBuilder
from services.memory_service import MemoryService
from services.memory_extractor import MemoryExtractor
from services.memory_router import MemoryRouter
from services.router_service import RouterService
from services.answer_service import AnswerService


class ChatService:

    def __init__(self):

        self.memory = MemoryService()
        self.extractor = MemoryExtractor()

    def ask(self, username: str, question: str):

        start_time = time.time()

        username = username.strip().lower()

        # ---------------------------------
        # Ensure User Exists
        # ---------------------------------

        self.memory.create_user(username)

        # ---------------------------------
        # Update Memory (if required)
        # ---------------------------------

        memory_updated = False

        if MemoryRouter.needs_memory_update(question):

            extracted = self.extractor.extract(question)

            profile = extracted.get("profile", {})
            facts = extracted.get("facts", [])

            if profile:
                self.memory.update_profile(
                    username,
                    profile
                )

            for fact in facts:
                self.memory.add_fact(
                    username,
                    fact
                )

            memory_updated = True

        # ---------------------------------
        # Build Context
        # ---------------------------------

        context = self.memory.get_context(username)

        # ---------------------------------
        # Decide Research
        # ---------------------------------

        use_research = RouterService.needs_search(question)

        # ---------------------------------
        # Build Crew
        # ---------------------------------

        crew = CrewBuilder.build(
            question=question,
            context=context,
            use_research=use_research
        )

        # ---------------------------------
        # Execute Crew
        # ---------------------------------

        assistant_answer = ""
        research_answer = ""

        try:

            result = crew.kickoff(
                inputs={
                    "username": username,
                    "question": question,
                    "context": context
                }
            )

            outputs = result.tasks_output

            assistant_answer = outputs[0].raw

            if use_research:
                research_answer = outputs[1].raw
            else:
                research_answer = assistant_answer

        except Exception as e:

            assistant_answer = f"Error : {str(e)}"

            research_answer = assistant_answer

        # ---------------------------------
        # Save Conversation
        # ---------------------------------

        self.memory.add_message(
            username,
            "user",
            question
        )

        self.memory.add_message(
            username,
            "assistant",
            research_answer
        )

        # ---------------------------------
        # Save Answer Log
        # ---------------------------------

        AnswerService.save(
            username=username,
            question=question,
            assistant=assistant_answer,
            research=research_answer
        )

        # ---------------------------------
        # Execution Time
        # ---------------------------------

        execution_time = round(
            time.time() - start_time,
            2
        )

        # ---------------------------------
        # Dashboard Metrics
        # ---------------------------------

        try:

            import streamlit as st

            st.session_state.questions = (
                st.session_state.get("questions", 0) + 1
            )

            if use_research:

                st.session_state.research_calls = (
                    st.session_state.get(
                        "research_calls",
                        0
                    ) + 1
                )

            if memory_updated:

                st.session_state.memory_updates = (
                    st.session_state.get(
                        "memory_updates",
                        0
                    ) + 1
                )

            st.session_state.avg_time = execution_time

        except Exception:
            pass

        return {

            "assistant": assistant_answer,

            "research": research_answer,

            "execution_time": execution_time,

            "used_research": use_research,

            "memory_updated": memory_updated,

            "context": context

        }