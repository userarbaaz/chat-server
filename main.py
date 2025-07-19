from fastapi import FastAPI, Request
from client import ask_openrouter

app = FastAPI()

@app.post("/api/bot")
async def chatbot(request: Request):
    data = await request.json()
    message = data.get("message")
    print(f"User asked: {message}")  # Logs input
    response = ask_openrouter(message)
    print(f"Bot response: {response}")  # Logs output or error
    return {"response": response}
