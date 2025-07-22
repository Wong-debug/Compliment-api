# main.py

from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
  CORSMiddleware,
  allow_origins=["https://thetoolsnest.com","http://127.0.0.1:5500",
        "http://localhost:5500"],
  allow_methods=["*"],
  allow_headers=["*"],
)
class Input(BaseModel):
    name: str

COMPLIMENTS = [
    "You're crushing it!",
    "You're a genius in disguise.",
    "Your code smells like roses.",
    "You're making the internet a better place.",
    "Your ideas? 🔥 Absolute fire."
]

@app.post("/generate")
def generate_compliment(data: Input):
    compliment = random.choice(COMPLIMENTS)
    return {"message": f"{compliment} Keep going, {data.name}!"}
