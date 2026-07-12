from crew.crew_builder import CrewBuilder

from services.memory_service import MemoryService


class ChatService:

    def __init__(self):

        self.memory = MemoryService()

        self.crew = CrewBuilder()

    def chat(

            self,

            username,

            question

    ):

        profile = self.memory.get_profile(username)

        if not profile:

            profile = self.memory.create_profile(username)

        history = self.memory.get_history(username)

        crew = self.crew.build(

            question=question,

            memory=history

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

        self.memory.update_last_seen(username)

        return answer