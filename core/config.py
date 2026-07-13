import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    # ----------------------------------------
    # OpenAI
    # ----------------------------------------

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    MODEL = "gpt-4.1-mini"

    TEMPERATURE = 0.2

    MAX_ITERATIONS = 3

    # ----------------------------------------
    # Application
    # ----------------------------------------

    APP_NAME = "Customer Support AI"

    # ----------------------------------------
    # Storage
    # ----------------------------------------

    MEMORY_FILE = "storage/memory.json"

    ANSWER_FILE = "storage/answers.txt"


settings = Settings()