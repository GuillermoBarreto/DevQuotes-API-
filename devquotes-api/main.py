from fastapi import FastAPI, HTTPException
import random
import json

app = FastAPI()

with open("quotes.json") as f:
    quotes = json.load(f)

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
