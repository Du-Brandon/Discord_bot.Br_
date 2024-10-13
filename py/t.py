import requests
import os

with open(os.path.join("..", "info", "chatAPI.txt"), 'r') as f:
    api_key = [f.read().strip("\n")]
print(api_key)
prompt = "1+1=多少"

response = requests.post(
    'https://api.openai.com/v1/chat/completions',
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    },
    json = {
        'model': 'gpt-3.5-turbo', # 一定要用chat可以用的模型
        'messages' : [{"role": "user", "content": prompt}]
    })

#使用json解析
json = response.json()
print(json)