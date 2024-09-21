from pages.login import LoginPage
from playwright.sync_api import expect


def test_uncorrect_input_auth(page, login):
    username = "egor"
    password = "1234"
    login(username,password)

    login_page = LoginPage(page)
    expect(login_page.error_locator).to_have_text(
            "Epic sadface: Username and password do not match any user in this service")