import json
from pprint import pprint
from ollama import chat
from ollama import ChatResponse
def aitest(prompt):
    response: ChatResponse = chat(model='deepseek-coder-v2:latest', messages=[
      {
        'role': 'user',
        'content': f'{prompt}',
      },
    ])
    return response['message']['content']



