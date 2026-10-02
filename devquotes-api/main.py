from fastapi import FastAPI, HTTPException
from pathlib import Path
import random
import json

app = FastAPI()

QUOTES_PATH = Path(__file__).with_name("quotes.json")


def _is_valid_quote(entry):
    return isinstance(entry, dict) and "author" in entry and "quote" in entry


try:
    with QUOTES_PATH.open() as f:
        loaded = json.load(f)
    if isinstance(loaded, list):
        # Drop malformed entries so /quote never returns garbage.
        quotes = [q for q in loaded if _is_valid_quote(q)]
    else:
        quotes = []
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
