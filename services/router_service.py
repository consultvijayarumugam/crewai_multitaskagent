import re


class RouterService:

    SEARCH_KEYWORDS = [

        "latest",
        "today",
        "current",
        "news",
        "price",
        "cost",
        "weather",
        "stock",
        "bitcoin",
        "crypto",
        "ipl",
        "score",
        "result",
        "live",
        "search",
        "research",
        "compare",
        "release",
        "launch",
        "top",
        "best",
        "recent",
        "update"

    ]

    @classmethod
    def needs_search(cls, question: str) -> bool:

        question = question.lower().strip()

        # Explicit search request

        if "search" in question:
            return True

        if "research" in question:
            return True

        # Keyword based

        for keyword in cls.SEARCH_KEYWORDS:

            if re.search(rf"\b{re.escape(keyword)}\b", question):
                return True

        return False