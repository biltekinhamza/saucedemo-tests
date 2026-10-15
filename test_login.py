from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com"


def login(page: Page, username: str, password: str):
    page.goto(BASE_URL)
    page.fill("#user-name", username)
    page.fill("#password", password)
    page.click("#login-button")


def test_successful_login(page: Page):
    login(page, "standard_user", "secret_sauce")
    expect(page).to_have_url(f"{BASE_URL}/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


def test_locked_out_user_sees_error(page: Page):
    login(page, "locked_out_user", "secret_sauce")
    expect(page.locator("[data-test='error']")).to_contain_text("locked out")


def test_wrong_password_shows_error(page: Page):
    login(page, "standard_user", "wrong_password")
    expect(page.locator("[data-test='error']")).to_contain_text("do not match")
