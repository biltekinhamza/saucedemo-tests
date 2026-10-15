from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com"
BACKPACK = "Sauce Labs Backpack"


def add_backpack_to_cart(page: Page):
    page.click("[data-test='add-to-cart-sauce-labs-backpack']")


def test_add_item_updates_cart_badge(logged_in_page: Page):
    add_backpack_to_cart(logged_in_page)
    expect(logged_in_page.locator("[data-test='shopping-cart-badge']")).to_have_text("1")


def test_cart_page_shows_added_item(logged_in_page: Page):
    add_backpack_to_cart(logged_in_page)
    logged_in_page.click("[data-test='shopping-cart-link']")
    expect(logged_in_page).to_have_url(f"{BASE_URL}/cart.html")
    cart_item = logged_in_page.locator("[data-test='cart-list'] [data-test='inventory-item-name']")
    expect(cart_item).to_have_text(BACKPACK)


def test_remove_item_empties_cart(logged_in_page: Page):
    add_backpack_to_cart(logged_in_page)
    logged_in_page.click("[data-test='remove-sauce-labs-backpack']")
    expect(logged_in_page.locator("[data-test='shopping-cart-badge']")).to_have_count(0)


def test_complete_checkout(logged_in_page: Page):
    add_backpack_to_cart(logged_in_page)
    logged_in_page.click("[data-test='shopping-cart-link']")
    logged_in_page.click("[data-test='checkout']")
    logged_in_page.fill("[data-test='firstName']", "Ali")
    logged_in_page.fill("[data-test='lastName']", "Yilmaz")
    logged_in_page.fill("[data-test='postalCode']", "34000")
    logged_in_page.click("[data-test='continue']")
    expect(logged_in_page).to_have_url(f"{BASE_URL}/checkout-step-two.html")
    logged_in_page.click("[data-test='finish']")
    expect(logged_in_page).to_have_url(f"{BASE_URL}/checkout-complete.html")
    expect(logged_in_page.locator("[data-test='complete-header']")).to_have_text(
        "Thank you for your order!"
    )


def test_checkout_requires_first_name(logged_in_page: Page):
    add_backpack_to_cart(logged_in_page)
    logged_in_page.click("[data-test='shopping-cart-link']")
    logged_in_page.click("[data-test='checkout']")
    logged_in_page.click("[data-test='continue']")
    expect(logged_in_page.locator("[data-test='error']")).to_contain_text("First Name is required")
