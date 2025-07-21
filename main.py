from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()
API_KEY = os.environ.get("OPENROUTER")
OPENROUTER_API_KEY =   API_KEY# Paste your actual key here
MODEL = "mistralai/mistral-7b-instruct:free"

class Message(BaseModel):
    message: str

@app.post("/api/bot")
async def bot_endpoint(msg: Message):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": msg.message}
        ]
    }

    try:
        res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        res.raise_for_status()
        response = res.json()["choices"][0]["message"]["content"]
        return {"response": response}
    except Exception as e:
        return {"response": f"❌ Error: {str(e)}"}
