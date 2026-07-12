"""
Application Configuration
Loads environment variables.
"""

from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    @staticmethod
    def validate():
        if not Config.OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY not found. Please configure your .env file."
            )