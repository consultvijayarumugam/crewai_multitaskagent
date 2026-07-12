from langchain_openai import ChatOpenAI

from core.config import settings


llm = ChatOpenAI(
    model=settings.MODEL,
    temperature=settings.TEMPERATURE,
    api_key=settings.OPENAI_API_KEY,
)