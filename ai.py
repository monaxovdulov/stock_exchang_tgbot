
from ollama import chat
from ollama import ChatResponse


def get_llm_response(prompt) -> str:
    response: ChatResponse = chat(model='deepseek-coder-v2:latest', messages=[
      {
        'role': 'user',
        'content': f'{prompt}',
      },
    ])
    return response['message']['content']



