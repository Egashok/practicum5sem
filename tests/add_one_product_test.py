from playwright.sync_api import expect

from pages.login import LoginPage
from pages.products import ProductsPage
from pages.cart import CartPage

def add_one_product_test(page):
    username = "standard_user"
    password = "secret_sauce"
    login = LoginPage(page)
    products = ProductsPage(page)
    cart = CartPage(page)

    login_page.navigate()
    login_page.login(username, password)

    products.navigate()
    products.add_bike()

    cart.navigate()

    expect(cart.amount_of_products()).to_have_text("1")
    expect(cart.bike_exist()).to_be_visible()