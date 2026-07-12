from crewai import Agent
from langchain_openai import ChatOpenAI

from core.config import settings

from tools.search_tool import search_tool


llm = ChatOpenAI(
    api_key=settings.OPENAI_API_KEY,
    model=settings.MODEL,
    temperature=settings.TEMPERATURE,
)


web_agent = Agent(
    role="Research Specialist",
    goal="Search the internet whenever required.",
    backstory="""
You search the web only when
internal knowledge is insufficient.
""",
    tools=[search_tool],
    llm=llm,
    verbose=True,
)