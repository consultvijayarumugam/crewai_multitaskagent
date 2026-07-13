import json
from datetime import datetime
from pathlib import Path

from core.config import settings


class MemoryService:

    def __init__(self):

        self.memory_file = Path(settings.MEMORY_FILE)

        if not self.memory_file.exists():
            self.memory_file.parent.mkdir(parents=True, exist_ok=True)
            self.memory_file.write_text("{}")

    # =====================================================
    # Internal Helpers
    # =====================================================

    def _normalize_username(self, username: str) -> str:
        return username.strip().lower()

    def _default_user(self):

        return {

            "profile": {

                "name": "",
                "email": "",
                "company": "",
                "designation": "",
                "location": ""

            },

            "facts": [],

            "history": [],

            "summary": "",

            "last_seen": ""

        }

    def _load(self):

        with open(self.memory_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save(self, data):

        with open(self.memory_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def _ensure_user(self, username):

        username = self._normalize_username(username)

        data = self._load()

        defaults = self._default_user()

        if username not in data:

            data[username] = defaults

        else:

            user = data[username]

            # Top Level Keys

            for key, value in defaults.items():

                if key not in user:

                    user[key] = value

            # Profile Keys

            for key, value in defaults["profile"].items():

                if key not in user["profile"]:

                    user["profile"][key] = value

        self._save(data)

        return username

    # =====================================================
    # User
    # =====================================================

    def create_user(self, username):

        username = self._ensure_user(username)

        return self.get_user(username)

    def get_user(self, username):

        username = self._ensure_user(username)

        data = self._load()

        return data[username]

    # =====================================================
    # Profile
    # =====================================================

    def get_profile(self, username):

        return self.get_user(username)["profile"]

    def update_profile(self, username, profile):

        username = self._ensure_user(username)

        data = self._load()

        for key, value in profile.items():

            if value:

                data[username]["profile"][key] = value

        self._save(data)

    # =====================================================
    # Facts
    # =====================================================

    def add_fact(self, username, fact):

        if not fact:
            return

        username = self._ensure_user(username)

        data = self._load()

        if fact not in data[username]["facts"]:

            data[username]["facts"].append(fact)

        self._save(data)

    def get_facts(self, username):

        return self.get_user(username)["facts"]

    # =====================================================
    # History
    # =====================================================

    def add_message(self, username, role, content):

        username = self._ensure_user(username)

        data = self._load()

        data[username]["history"].append({

            "role": role,

            "content": content,

            "timestamp": datetime.now().isoformat()

        })

        data[username]["last_seen"] = datetime.now().isoformat()

        self._save(data)

    def get_history(self, username):

        return self.get_user(username)["history"]

    # =====================================================
    # Summary
    # =====================================================

    def update_summary(self, username, summary):

        username = self._ensure_user(username)

        data = self._load()

        data[username]["summary"] = summary

        self._save(data)

    # =====================================================
    # Context
    # =====================================================

    def get_context(self, username):

        username = self._ensure_user(username)

        user = self.get_user(username)

        profile = user["profile"]

        facts = user["facts"]

        history = user["history"][-10:]

        lines = []

        # ---------------- Profile ----------------

        lines.append("USER PROFILE")

        for key, value in profile.items():

            if value:

                lines.append(f"{key.title()}: {value}")

        # ---------------- Facts ----------------

        if facts:

            lines.append("")
            lines.append("KNOWN FACTS")

            for fact in facts:

                lines.append(f"- {fact}")

        # ---------------- History ----------------

        if history:

            lines.append("")
            lines.append("RECENT CONVERSATION")

            for item in history:

                lines.append(
                    f"{item['role']}: {item['content']}"
                )

        return "\n".join(lines)