from fastapi import FastAPI
from pydantic import BaseModel
from client import ask_openrouter

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post("/api/bot")
def chat_with_bot(msg: Message):
    user_input = msg.message
    reply = ask_openrouter(user_input)
    return {"reply": reply}
