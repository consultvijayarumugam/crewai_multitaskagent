from crewai import Agent
from langchain_openai import ChatOpenAI

from core.config import settings


llm = ChatOpenAI(
    api_key=settings.OPENAI_API_KEY,
    model=settings.MODEL,
    temperature=settings.TEMPERATURE,
)


entry_agent = Agent(
    role="Customer Support Manager",
    goal="Understand the customer's question and decide what needs to be done.",
    backstory="""
You are the first point of contact.
You analyse every customer request,
understand the intent,
and assign work to the correct specialist.
""",
    llm=llm,
    verbose=True,
    allow_delegation=True,
)