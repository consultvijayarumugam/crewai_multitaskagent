from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()


@tool("Internet Search Tool")
def internet_search(query: str) -> str:
    """
    Search the internet for the latest information.
    """

    query = query.strip()

    if not query:
        return "No search query provided."

    try:

        result = search.run(query)

        if not result:
            return "No useful information found."

        return result

    except Exception as e:

        return f"Internet search failed: {str(e)}"