import json
from pprint import pprint
import os
import requests

import dotenv
def generate_response_llm(prompt:str):
    dotenv.load_dotenv()
    token = os.getenv("OPENROUTER_API_TOKEN")
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        data=json.dumps(
            {
                "model": "google/gemini-2.0-flash-exp:free",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            }
        ),
    )
    pprint(response.json())

generate_response_llm("можно ли попить из кружки у которой запаян верх и нету дна?")

