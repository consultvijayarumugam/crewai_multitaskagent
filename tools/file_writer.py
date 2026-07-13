from crewai.tools import tool

from core.config import settings
from core.utils import current_time, separator


@tool("Answer Writer Tool")
def save_answers(
    username: str,
    question: str,
    assistant_answer: str,
    search_answer: str
) -> str:
    """
    Save conversation into answers.txt
    """

    with open(settings.ANSWER_FILE, "a", encoding="utf-8") as file:

        file.write(separator() + "\n")

        file.write("Customer Support AI\n")

        file.write(separator() + "\n\n")

        file.write(f"Date : {current_time()}\n")

        file.write(f"User : {username}\n\n")

        file.write("Question\n")

        file.write(question + "\n\n")

        file.write("Assistant Answer\n")

        file.write(assistant_answer + "\n\n")

        file.write("Web Search Answer\n")

        file.write(search_answer + "\n\n")

        file.write(separator() + "\n\n")

    return "Conversation saved successfully."