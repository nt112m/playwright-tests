from playwright.sync_api import Page, expect
from login_page import LoginPage
from cart_page import CartPage


def test_valid_login(page: Page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_invalid_login(page: Page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "wrong_password")
    expect(page.get_by_text("Username and password do not match")).to_be_visible()


def test_add_to_cart(logged_in_page):
    cart_page = CartPage(logged_in_page)
    cart_page.add_product_to_cart()
    cart_page.open_cart()
    assert cart_page.get_cart_item_name()


def test_checkout_page(logged_in_page):
    cart_page = CartPage(logged_in_page)
    cart_page.add_product_to_cart()
    cart_page.open_cart()
    logged_in_page.get_by_role("button", name="Checkout").click()
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")


def test_checkout_details(logged_in_page):
    cart_page = CartPage(logged_in_page)
    cart_page.add_product_to_cart()
    cart_page.open_cart()
    logged_in_page.get_by_role("button", name="Checkout").click()
    logged_in_page.get_by_placeholder("First Name").fill("Dani")
    logged_in_page.get_by_placeholder("Last Name").fill("Cohen")
    logged_in_page.get_by_placeholder("Zip/Postal Code").fill("12345")
    logged_in_page.get_by_role("button", name="Continue").click()
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

def test_wait_for_inventory(page: Page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    expect(page.locator(".inventory_list")).to_be_visible()