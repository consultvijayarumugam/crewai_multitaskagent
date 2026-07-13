import json

from openai import OpenAI

from core.config import settings


class MemoryExtractor:

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    def extract(self, message: str):

        prompt = f"""
You are an AI Memory Extraction Engine.

Your responsibility is to identify ONLY long-term
user information from the message below.

MESSAGE

{message}

Return ONLY valid JSON.

Schema

{{
    "profile": {{
        "name":"",
        "email":"",
        "company":"",
        "designation":"",
        "location":""
    }},
    "facts":[]
}}

Rules

1. Extract only long-term user information.

2. Ignore greetings.

3. Ignore temporary questions.

4. Never guess.

5. If a field is missing return "".

6. Facts should be short.

Example

"My name is Vijay.
I own Bluemoon Construction."

Output

{{
    "profile": {{
        "name":"Vijay",
        "email":"",
        "company":"Bluemoon Construction",
        "designation":"",
        "location":""
    }},
    "facts":[
        "User owns Bluemoon Construction"
    ]
}}

Return JSON only.
"""

        response = self.client.chat.completions.create(

            model=settings.MODEL,

            temperature=0,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        content = response.choices[0].message.content.strip()

        try:

            return json.loads(content)

        except Exception:

            return {
                "profile": {},
                "facts": []
            }