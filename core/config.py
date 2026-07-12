from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    MODEL = "gpt-4.1-mini"

    TEMPERATURE = 0.2

    MEMORY_FILE = "storage/memory.json"

    ANSWER_FILE = "storage/answers.txt"


settings = Settings()