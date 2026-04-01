import pytest
from pages.login_page import LoginPage
from data.login_data import valid_user, invalid_users

URL = "https://www.saucedemo.com/"

def test_valid_login(page):
    login = LoginPage(page)
    login.navigate(URL)

    login.login(valid_user["username"], valid_user["password"])

    page.wait_for_url("**/inventory.html")

    assert "inventory" in page.url


@pytest.mark.parametrize("user", invalid_users)
def test_invalid_login(page, user):
    login = LoginPage(page)
    login.navigate(URL)

    login.login(user["username"], user["password"])

    assert login.get_error() is not None