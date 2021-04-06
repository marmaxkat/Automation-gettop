from pages.top_menu import TopMenu
from pages.checkout_page import Checkout
from pages.product_page import ProductPage
from pages.shopping_cart import ShoppingCart


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.top_menu = TopMenu(self.driver)
        self.checkout_page = Checkout(self.driver)
        self.product_page = ProductPage(self.driver)
        self.shopping_cart = ShoppingCart(self.driver)