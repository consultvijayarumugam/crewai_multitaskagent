from core.config import settings
from core.utils import load_json, save_json


class Memory:

    def __init__(self):

        self.path = settings.MEMORY_FILE

        self.memory = load_json(self.path)

    def get_user(self, user):

        return self.memory.get(user, {})

    def update(self, user, question, answer):

        if user not in self.memory:

            self.memory[user] = {
                "history": []
            }

        self.memory[user]["history"].append({

            "question": question,

            "answer": answer

        })

        save_json(self.path, self.memory)