from ollama import chat
from ollama import ChatResponse
prompt=input("Ваш вопрос: ")
response: ChatResponse = chat(model='deepseek-coder-v2:latest', messages=[
  {
    'role': 'user',
    'content': f'{prompt}',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)