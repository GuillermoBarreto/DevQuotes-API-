from fastapi.testclient import TestClient

import main

client = TestClient(main.app)


def test_root_returns_welcome_message():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the DevQuotes API!"}


def test_quotes_returns_list():
    response = client.get("/quotes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_random_quote_has_author_and_quote():
    response = client.get("/quote")
    assert response.status_code == 200
    body = response.json()
    assert "author" in body
    assert "quote" in body


def test_quote_returns_404_when_list_is_empty(monkeypatch):
    monkeypatch.setattr(main, "quotes", [])
    response = client.get("/quote")
    assert response.status_code == 404
