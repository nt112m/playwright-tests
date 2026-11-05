from playwright.sync_api import Page, expect


def test_username_field(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    expect(page.get_by_placeholder("Username")).to_have_value("standard_user")


def test_login_button(page: Page):
    page.goto("https://www.saucedemo.com")
    expect(page.get_by_role("button", name="Login")).to_be_visible()


def test_page_text(page: Page):
    page.goto("https://www.saucedemo.com")
    expect(page.get_by_text("Accepted usernames are:")).to_be_visible()


def test_click_login(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Username is required")).to_be_visible()


def test_check(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    page.get_by_role("checkbox").first.check()
    expect(page.get_by_role("checkbox").first).to_be_checked()


def test_select_option(page: Page):
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.locator("#dropdown").select_option("Option 2")
    expect(page.locator("#dropdown")).to_have_value("2")
    



    