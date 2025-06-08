import requests
import json

api_key = "your-key-here"

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

payload = {
    "model": "your model's name here",
    "messages": "your message here"}

response = requests.post('https://api.openai.com/v1/chat/completions',
                         headers=headers,
                         data=json.dumps(payload))

chat_response = response.json()["choices"][0]['message']['content']
