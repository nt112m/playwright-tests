from playwright.sync_api import Page, expect

def test_username_field(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")