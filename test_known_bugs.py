"""Known defects of the demo shop's `problem_user`, written as tests.

Each test describes the CORRECT behaviour and is marked xfail(strict=True):
- today the bug exists, so the test fails and is reported as "xfailed" (expected);
- once the bug is fixed the test passes, strict mode turns that into a failure,
  which reminds us to remove the xfail marker.
See the matching write-ups in the bug-reports/ folder.
"""
import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com"


@pytest.fixture
def problem_user_page(page: Page) -> Page:
    page.goto(BASE_URL)
    page.fill("#user-name", "problem_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_url(f"{BASE_URL}/inventory.html")
    return page


@pytest.mark.xfail(strict=True, reason="BUG-001: last name text is typed into first name")
def test_problem_user_can_enter_last_name(problem_user_page: Page):
    problem_user_page.click("[data-test='add-to-cart-sauce-labs-backpack']")
    problem_user_page.click("[data-test='shopping-cart-link']")
    problem_user_page.click("[data-test='checkout']")
    problem_user_page.fill("[data-test='firstName']", "Ali")
    problem_user_page.fill("[data-test='lastName']", "Yilmaz")

    expect(problem_user_page.locator("[data-test='firstName']")).to_have_value("Ali")
    expect(problem_user_page.locator("[data-test='lastName']")).to_have_value("Yilmaz")


@pytest.mark.xfail(strict=True, reason="BUG-002: all product images are identical")
def test_problem_user_sees_distinct_product_images(problem_user_page: Page):
    sources = problem_user_page.locator(".inventory_item_img img").evaluate_all(
        "images => images.map(image => image.getAttribute('src'))"
    )

    assert len(sources) == 6
    assert len(set(sources)) == 6  # six different image files
