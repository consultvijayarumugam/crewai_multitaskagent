import re


class MemoryRouter:

    MEMORY_PATTERNS = [

        r"\bmy name is\b",
        r"\bi am\b",
        r"\bi'm\b",
        r"\bi work at\b",
        r"\bi work for\b",
        r"\bi own\b",
        r"\bi live in\b",
        r"\bi am from\b",
        r"\bi'm from\b",
        r"\bmy email\b",
        r"\bmy phone\b",
        r"\bmy company\b",
        r"\bmy designation\b",
        r"\bmy goal\b",
        r"\bmy project\b"

    ]

    @classmethod
    def needs_memory_update(cls, message: str) -> bool:

        message = message.lower().strip()

        for pattern in cls.MEMORY_PATTERNS:

            if re.search(pattern, message):
                return True

        return False