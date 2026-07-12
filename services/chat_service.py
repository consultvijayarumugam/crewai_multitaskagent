from crew.crew_builder import CrewBuilder
from services.memory_service import MemoryService


class ChatService:

    def __init__(self):

        self.memory = MemoryService()

        self.crew_builder = CrewBuilder()

    def ask(self, username: str, question: str):

        user = self.memory.get_user(username)

        if not user:

            self.memory.create_user(username)

        history = self.memory.get_history(username)

        crew = self.crew_builder.build(
            question=question,
            history=history
        )

        result = crew.kickoff()

        answer = str(result)

        self.memory.add_message(
            username,
            "user",
            question
        )

        self.memory.add_message(
            username,
            "assistant",
            answer
        )

        return answer