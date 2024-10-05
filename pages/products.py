class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_bike_locator =  page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]")
    def navigate(self):
        self.page.goto("https://www.saucedemo.com/inventory.html")

    def add_bike(self):
        self.add_to_cart_bike_locator.click()