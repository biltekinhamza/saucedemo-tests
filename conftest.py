import pytest
from playwright.sync_api import Page

BASE_URL = "https://www.saucedemo.com"


@pytest.fixture
def logged_in_page(page: Page) -> Page:
    """A page that is already logged in as standard_user."""
    page.goto(BASE_URL)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_url(f"{BASE_URL}/inventory.html")
    return page
