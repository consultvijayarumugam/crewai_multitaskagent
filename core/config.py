from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    MODEL = "gpt-4.1-mini"

    TEMPERATURE = 0.2

    PROFILE_MEMORY = "storage/memory/profiles.json"

    SESSION_MEMORY = "storage/memory/sessions.json"

    SUMMARY_MEMORY = "storage/memory/summaries.json"

    ANSWER_FILE = "storage/answers.txt"


settings = Settings()