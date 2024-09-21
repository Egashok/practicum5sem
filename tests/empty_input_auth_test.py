from pages.login_page import LoginPage

def test_login_empty_fields(page, login):
    username = ""
    password = ""
    login(username, password)

    login_page = LoginPage(page)
    error_message = login_page.get_error()
    if error_message:
        assert error_message == 'Epic sadface: Username is required'
