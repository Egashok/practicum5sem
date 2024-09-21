from playwright.sync_api import expect

from pages.login import LoginPage

def test_empty_field_auth(page,login):
    username = ''
    password = ''
    login(username,password)

    login_page = LoginPage(page)
    expect(login_page.error_locator).to_have_text(
            "Epic sadface: Username is required")
