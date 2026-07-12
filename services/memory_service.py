import json
from datetime import datetime
from pathlib import Path


class MemoryService:

    def __init__(self):
        self.memory_file = Path("storage/memory.json")

        if not self.memory_file.exists():
            self.memory_file.write_text("{}")

    def _load(self):
        with open(self.memory_file, "r") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.memory_file, "w") as f:
            json.dump(data, f, indent=4)

    def get_user(self, username):
        data = self._load()
        return data.get(username)

    def create_user(self, username):

        data = self._load()

        if username not in data:

            data[username] = {
                "profile": {
                    "name": username,
                    "email": "",
                    "company": ""
                },
                "history": [],
                "summary": "",
                "last_seen": ""
            }

            self._save(data)

        return data[username]

    def get_history(self, username):

        data = self._load()

        if username not in data:
            return []

        return data[username]["history"]

    def add_message(self, username, role, message):

        data = self._load()

        if username not in data:
            self.create_user(username)
            data = self._load()

        data[username]["history"].append(
            {
                "role": role,
                "content": message,
                "timestamp": datetime.now().isoformat()
            }
        )

        data[username]["last_seen"] = datetime.now().isoformat()

        self._save(data)

    def update_summary(self, username, summary):

        data = self._load()

        data[username]["summary"] = summary

        self._save(data)