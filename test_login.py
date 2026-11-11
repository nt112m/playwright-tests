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


def test_add_to_cart(page: Page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    cart_page = CartPage(page)
    cart_page.add_product_to_cart()
    cart_page.open_cart()
    assert cart_page.get_cart_item_name()





