import pytest
from login_page import LoginPage

@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    return page