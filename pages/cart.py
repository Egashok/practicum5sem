class CartPage:
    def __init__(self, page):
        self.page = page
        self.bike_in_cart_locator = page.locator(
                "[data-test=\"item-0-title-link\"]"
                )
        self.shopping_cart_badge = page.locator(
                "[data-test=\"shopping-cart-badge\"]")
        self.to_checkout = page.locator(
                "[data-test=\"checkout\"]")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/cart.html")

    def bike_exist(self):
        return self.bike_in_cart_locator

    def amount_of_products(self):
        return self.shopping_cart_badge

    def checkout(self):
        self.to_checkout.click()