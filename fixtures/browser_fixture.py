import pytest
from playwright.sync_api import sync_playwright
from utils.config import CONFIG,ENV

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = CONFIG[ENV]["headless"])
        context =  browser.new_context()
        page = context.new_page()
        
        yield page

        context.close()
        browser.close()

    