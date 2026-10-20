from playwright.sync_api import Page, expect
from database_connection import DatabaseConnection

def test_create_new_film(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    page.goto("http://localhost:5001/films")
    page.get_by_placeholder("Title").fill("Argo")
    page.get_by_placeholder("Director").fill("Ben Affleck")
    page.get_by_role("button", name="Submit").click()
    films = page.locator('li')
    new_film = films.all_inner_texts()[-1]
    assert new_film == "Argo by Ben Affleck"