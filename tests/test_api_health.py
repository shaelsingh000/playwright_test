import pytest

@pytest.mark.api
@pytest.mark.smoke
def test_api_health(page):
    response = page.request.get("https://www.saucedemo.com/")
    assert response.status == 200