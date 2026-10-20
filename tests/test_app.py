import sys
import os
import asyncio

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

def test_get_books_returns_a_200():
    client = app.test_client()
    response = client.get("/books")
    assert response.status_code == 200


def test_get_books_returns_all_the_books():
    client = app.test_client()
    response = client.get("/books")
    assert "The Gruffalo" in response.text
    assert "Julia Donaldson" in response.text
    assert "Ada Twist, Scientist" in response.text
    assert "Andrea Beaty" in response.text
    assert "The Girl Who Drank the Moon" in response.text
    assert "Kelly Barnhill" in response.text
    assert "Dragons in a Bag" in response.text
    assert "Zetta Elliott" in response.text

def test_get_authors_returns_a_200():
    client = app.test_client()
    response = client.get("/authors")
    assert response.status_code == 200

def test_get_authors_returns_all_the_authors():
    client = app.test_client()
    response = client.get("/authors")
    assert response.json == [
        {
            "name": "Julia Donaldson",
            "dob": "1948-09-16"
        },
        {
            "name": "Andrea Beaty",
            "dob": "1961-10-08"
        },
        {
            "name": "Kelly Barnhill",
            "dob": "1973-01-01"
        },
        {
            "name": "Zetta Elliott",
            "dob": "1979-11-11"
        }
        ]