# client.py
import os
import requests

API_KEY = os.environ.get("OPENROUTER_API_KEY")

API_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://chat-server-oh2q.onrender.com",
    "X-Title": "ESP32Bot"
}

def ask_openrouter(prompt, model="openai/gpt-3.5-turbo"):
    body = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(API_URL, headers=HEADERS, json=body)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
