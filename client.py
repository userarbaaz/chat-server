# openrouter_client.py
import requests

API_KEY = "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"  # 🔒 Your actual OpenRouter key
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def ask_openrouter(prompt: str, model: str = "mistralai/mistral-7b-instruct"):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(API_URL, headers=headers, json=data)

    # Debugging output
    print("Status Code:", response.status_code)
    print("Response:", response.text)

    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
