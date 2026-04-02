import pytest
from pages.login_page import LoginPage
from data.login_data import valid_user, invalid_users
from utils.config import CONFIG,ENV

URL = CONFIG[ENV]["base_url"]


@pytest.mark.smoke
@pytest.mark.auth
def test_valid_login(page):
    login = LoginPage(page)
    login.navigate(URL)

    login.login(valid_user["username"], valid_user["password"])

    page.wait_for_url("**/inventory.html")

    assert "inventory" in page.url

@pytest.mark.regression
@pytest.mark.auth
@pytest.mark.parametrize("user", invalid_users)
def test_invalid_login(page, user):
    login = LoginPage(page)
    login.navigate(URL)

    login.login(user["username"], user["password"])

    assert login.get_error() is not None

@pytest.mark.regression
@pytest.mark.auth
def test_locked_user_login(page):
    login = LoginPage(page)
    login.navigate(URL)

    login.login("locked_out_user", "secret_sauce")

    assert "locked out" in login.get_error().lower()

@pytest.mark.regression
@pytest.mark.auth
def test_empty_login(page):
    login = LoginPage(page)
    login.navigate(URL)

    login.login("", "")

    assert login.get_error() is not None

@pytest.mark.regression
@pytest.mark.auth
def test_username_only(page):
    login = LoginPage(page)
    login.navigate(URL)

    login.login("standard_user", "")

    assert login.get_error() is not None

@pytest.mark.regression
@pytest.mark.auth
def test_password_only(page):
    login = LoginPage(page)
    login.navigate(URL)

    login.login("", "secret_sauce")

    assert login.get_error() is not None

@pytest.mark.smoke
@pytest.mark.auth
def test_logout(page):
    login = LoginPage(page)
    login.navigate(URL)

    login.login(valid_user["username"], valid_user["password"])
    page.wait_for_url("**/inventory.html")

    # Assuming you have menu actions
    page.click("#react-burger-menu-btn")
    page.click("#logout_sidebar_link")

    page.wait_for_url("**/")
    assert page.url == URL

@pytest.mark.regression
@pytest.mark.auth
def test_session_persistence(page):
    login = LoginPage(page)
    login.navigate(URL)

    login.login(valid_user["username"], valid_user["password"])
    page.wait_for_url("**/inventory.html")

    # Refresh page
    page.reload()

    assert "inventory" in page.url

@pytest.mark.regression
@pytest.mark.auth
def test_direct_inventory_access_without_login(page):
    page.goto(f"{URL}/inventory.html")

    # Should redirect to login
    assert "inventory" not in page.url