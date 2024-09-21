from playwright.sync_api import expect

from pages.login import LoginPage
from pages.products import ProductsPage
from pages.cart import CartPage

def test_add_one_product(page,login):
    username = "standard_user"
    password = "secret_sauce"
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    login_page.navigate()
    login(username, password)

    products_page.navigate()
    products_page.add_bike()

    cart_page.navigate()

    expect(cart_page.amount_of_products()).to_have_text("1")
    expect(cart_page.bike_exist()).to_be_visible()