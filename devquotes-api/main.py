from fastapi import FastAPI, HTTPException
from pathlib import Path
import random
import json

app = FastAPI()

QUOTES_PATH = Path(__file__).with_name("quotes.json")

try:
    with QUOTES_PATH.open() as f:
        quotes = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    # Start with an empty list so the API stays up; /quote answers 404.
    quotes = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the DevQuotes API!"}

@app.get("/quote")
def get_random_quote():
    if not quotes:
        raise HTTPException(status_code=404, detail="No quotes available")
    return random.choice(quotes)

@app.get("/quotes")
def get_all_quotes():
    return quotes
