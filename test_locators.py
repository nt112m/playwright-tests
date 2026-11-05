from playwright.sync_api import Page, expect

def test_username_field(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    expect(page.get_by_placeholder("Username")).to_have_value("standard_user")

def test_login_button(page: Page):
    page.goto("https://www.saucedemo.com")
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    


    