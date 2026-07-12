from langchain_openai import ChatOpenAI

from core.config import settings


llm = ChatOpenAI(
    api_key=settings.OPENAI_API_KEY,
    model=settings.MODEL,
    temperature=settings.TEMPERATURE,
)