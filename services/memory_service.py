from datetime import datetime

from core.config import settings
from core.utils import load_json, save_json


class MemoryService:

    def __init__(self):

        self.profile_db = settings.PROFILE_MEMORY

        self.session_db = settings.SESSION_MEMORY

        self.summary_db = settings.SUMMARY_MEMORY

    def get_profile(self, username):

        profiles = load_json(self.profile_db)

        return profiles.get(username)

    def create_profile(self, username):

        profiles = load_json(self.profile_db)

        if username not in profiles:

            profiles[username] = {

                "name": username,

                "created_at": datetime.now().isoformat(),

                "last_seen": datetime.now().isoformat(),

                "preferences": {},

                "summary": ""

            }

            save_json(self.profile_db, profiles)

        return profiles[username]

    def update_last_seen(self, username):

        profiles = load_json(self.profile_db)

        if username in profiles:

            profiles[username]["last_seen"] = datetime.now().isoformat()

            save_json(self.profile_db, profiles)

    def add_message(self, session_id, role, message):

        sessions = load_json(self.session_db)

        sessions.setdefault(session_id, [])

        sessions[session_id].append({

            "role": role,

            "content": message,

            "time": datetime.now().isoformat()

        })

        save_json(self.session_db, sessions)

    def get_history(self, session_id):

        sessions = load_json(self.session_db)

        return sessions.get(session_id, [])