"""
Persistent Memory Manager
"""

import json
from pathlib import Path
from datetime import datetime

MEMORY_FILE = Path("storage/memory.json")


class MemoryManager:

    @staticmethod
    def load():

        if not MEMORY_FILE.exists():
            return {}

        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def save(memory: dict):

        memory["metadata"]["last_updated"] = datetime.now().isoformat()

        with open(MEMORY_FILE, "w", encoding="utf-8") as file:
            json.dump(memory, file, indent=4)

    @staticmethod
    def add_chat(question: str, answer: str):

        memory = MemoryManager.load()

        memory.setdefault("chat_history", [])

        memory["chat_history"].append(
            {
                "question": question,
                "answer": answer,
            }
        )

        MemoryManager.save(memory)

    @staticmethod
    def update_user(key: str, value: str):

        memory = MemoryManager.load()

        memory.setdefault("user", {})

        memory["user"][key] = value

        MemoryManager.save(memory)