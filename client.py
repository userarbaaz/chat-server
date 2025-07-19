# client.py
import os
import requests

API_KEY = os.environ.get("OPENROUTER")

if not API_KEY:
    raise ValueError("Missing OPENROUTER_API_KEY environment variable!")

API_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://chat-server-oh2q.onrender.com",  # optional, good to have
    "X-Title": "ESP32Bot"
}

def ask_openrouter(prompt, model="openai/gpt-3.5-turbo"):
    body = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = requests.post(API_URL, headers=HEADERS, json=body)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
    except KeyError:
        return "Error: Invalid response structure"

