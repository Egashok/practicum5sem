from pages.login_page import LoginPage
from data.config import settings


def uncorrect_input_aut(page, login):
    username = "egor"
    password = "1234"
    login(username,password)

    login_page = LoginPage(page)
    error_message = login_page.get_error()
    if error_message:
        assert error_message == 'Epic sadface: Username and password do not match any user in this service'
