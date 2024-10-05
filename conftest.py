import os
import pytest
from playwright.sync_api import sync_playwright
from pages.login import LoginPage


@pytest.fixture(scope="session")
def browser():
    headless = os.getenv("HEADLESS", "false").lower() == "true"
    browser_type = os.getenv("BROWSER", "chromium")
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=headless)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
@pytest.fixture
def login(page):
    login_page = LoginPage(page)
    def _login(username, password):
        page.goto("https://www.saucedemo.com")
        login_page.login(username, password)
    return _login
