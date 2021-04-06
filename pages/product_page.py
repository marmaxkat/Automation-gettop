from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProductPage(Page):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '.single_add_to_cart_button')
    CART = (By.CSS_SELECTOR, '.header-cart-link')

    def open_product_page(self, query):
        self.open_url(query)

    def click_add_to_cart(self):
        self.wait_for_element_appear(*self.ADD_TO_CART_BTN)
        self.click(*self.ADD_TO_CART_BTN)

    def click_cart(self):
        self.click(*self.CART)