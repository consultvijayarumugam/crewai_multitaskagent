from crewai import Agent
from langchain_openai import ChatOpenAI

from core.config import settings


llm = ChatOpenAI(
    api_key=settings.OPENAI_API_KEY,
    model=settings.MODEL,
    temperature=settings.TEMPERATURE,
)


assistant_agent = Agent(
    role="Customer Support Expert",
    goal="Provide accurate and friendly customer support.",
    backstory="""
You answer customer questions using
company knowledge and previous conversations.
Never hallucinate.
Always be polite.
""",
    llm=llm,
    verbose=True,
)