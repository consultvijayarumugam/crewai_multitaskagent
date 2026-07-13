import time

from crew.crew_builder import CrewBuilder
from services.memory_service import MemoryService
from services.memory_extractor import MemoryExtractor
from services.answer_service import AnswerService


class ChatService:

    def __init__(self):

        self.memory = MemoryService()
        self.extractor = MemoryExtractor()

    def ask(self, username: str, question: str):

        start_time = time.time()

        # -----------------------------------------
        # Normalize Username
        # -----------------------------------------

        username = username.strip().lower()

        # -----------------------------------------
        # Ensure User Exists
        # -----------------------------------------

        self.memory.create_user(username)

        # -----------------------------------------
        # Extract Long-Term Memory
        # -----------------------------------------

        extracted = self.extractor.extract(question)

        profile = extracted.get("profile", {})
        facts = extracted.get("facts", [])

        self.memory.update_profile(
            username,
            profile
        )

        for fact in facts:

            self.memory.add_fact(
                username,
                fact
            )

        # -----------------------------------------
        # Build User Context
        # -----------------------------------------

        context = self.memory.get_context(username)

        # -----------------------------------------
        # Build Crew
        # -----------------------------------------

        crew = CrewBuilder.build(
            question=question,
            context=context
        )

        # -----------------------------------------
        # Execute Crew
        # -----------------------------------------

        result = crew.kickoff(
            inputs={
                "username": username,
                "question": question,
                "context": context
            }
        )

        assistant_answer = ""
        research_answer = ""

        try:

            outputs = result.tasks_output

            if len(outputs) >= 1:
                assistant_answer = outputs[0].raw

            if len(outputs) >= 2:
                research_answer = outputs[1].raw

        except Exception:

            assistant_answer = str(result)
            research_answer = str(result)

        # -----------------------------------------
        # Save Conversation
        # -----------------------------------------

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

        # -----------------------------------------
        # Save Output File
        # -----------------------------------------

        AnswerService.save(
            username=username,
            question=question,
            assistant=assistant_answer,
            research=research_answer
        )

        execution_time = round(
            time.time() - start_time,
            2
        )

        return {

            "assistant": assistant_answer,

            "research": research_answer,

            "execution_time": execution_time,

            "context": context

        }