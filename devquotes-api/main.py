from fastapi import FastAPI, HTTPException
from pathlib import Path
import random
import json

app = FastAPI()

QUOTES_PATH = Path(__file__).with_name("quotes.json")


def _is_valid_quote(entry):
    # Check value types too: an entry like {"author": 123, "quote": None}
    # passes a key-presence check but would serve garbage to API consumers.
    return (
        isinstance(entry, dict)
        and isinstance(entry.get("author"), str)
        and isinstance(entry.get("quote"), str)
        and bool(entry["author"].strip())
        and bool(entry["quote"].strip())
    )


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


@app.get("/health")
def health_check():
    """Lightweight liveness probe reporting how many quotes are loaded."""
    return {"status": "ok", "quotes_loaded": len(quotes)}


@app.get("/quote")
def get_random_quote():
    if not quotes:
        raise HTTPException(status_code=404, detail="No quotes available")
    return random.choice(quotes)


@app.get("/quotes")
def get_all_quotes():
    return quotes
