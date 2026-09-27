# DevQuotes API

A small FastAPI service that serves developer quotes.

## Endpoints

- `GET /` — welcome message
- `GET /quote` — a random quote (404 when the list is empty)
- `GET /quotes` — all quotes

## Tech stack

- Python 3 + FastAPI
- Quote data in `devquotes-api/quotes.json`

## How to run

```bash
cd devquotes-api
pip install -r requirements.txt
uvicorn main:app --reload
```

## Tests

```bash
cd devquotes-api
pip install pytest
pytest
```

If `quotes.json` is missing or invalid, the API starts with an empty list instead of crashing.
