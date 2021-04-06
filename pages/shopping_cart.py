from pages.base_page import Page
from selenium.webdriver.common.by import By


class ShoppingCart(Page):
    CHECKOUT_BTN = (By.CSS_SELECTOR, 'a.checkout-button')

    def checkout_btn_clock(self):
        self.wait_for_element_appear(*self.CHECKOUT_BTN)
        self.click(*self.CHECKOUT_BTN)
