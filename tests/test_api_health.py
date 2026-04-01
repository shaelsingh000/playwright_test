def test_api_health(page):
    response = page.request.get("https://www.saucedemo.com/")
    assert response.status == 200