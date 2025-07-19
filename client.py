# client.py
import os, requests

API_KEY = os.environ["OPENROUTER_API_KEY"]
API_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    # These two are required by OpenRouter
    "HTTP-Referer": "https://chat-server-oh2q.onrender.com",
    "X-Title": "ESP32Bot"
}

def ask_openrouter(prompt, model="openai/gpt-3.5-turbo"):
    body = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }
    r = requests.post(API_URL, headers=HEADERS, json=body)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]
