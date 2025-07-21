from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

app = FastAPI()

# ✅ Allow requests from anywhere (ESP32, browsers, phones)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/bot")
async def chat_bot(req: Request):
    data = await req.json()
    msg = data.get("message", "")
    return {"response": f"You asked: {msg}"}  # Replace with AI logic if needed

# ✅ Run server on Render port (e.g., 10000+) instead of localhost:8000
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
