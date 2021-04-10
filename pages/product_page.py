from lib2to3.pgen2 import driver

from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.top_menu import *
from time import sleep


class ProductPage(Page):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '.single_add_to_cart_button button alt')
    CART = (By.CSS_SELECTOR, '.header-cart-link')
    TOP_MENU_LINKS = (By.CSS_SELECTOR, '.header-nav>li.menu-item>a')
    IPHONE_PRODUCTS_LINKS = (By.CSS_SELECTOR, '#menu-item-469>ul.nav-dropdown>li>a')
    IPHONE_MENU_LINK = (By.XPATH, "//a[@class = 'nav-top-link' and contains(@href,'product-category/iphone')]")
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.product-info>h1.product-title')

    def open_product_page(self, query):
        self.open_url(query)

    def click_add_to_cart(self):
        self.wait_for_element_appear(*self.ADD_TO_CART_BTN)
        self.click(*self.ADD_TO_CART_BTN)

    def click_cart(self):
        self.click(*self.CART)

    def verify_correct_page_open(self, query):
        category = query
        top_menu_links = self.driver.find_elements(*self.TOP_MENU_LINKS)
        for e in top_menu_links:
            if e.text == category and category == 'IPHONE':

                n = len(self.driver.find_elements(*self.IPHONE_PRODUCTS_LINKS))
                i = 0
                while i < n:

                    TopMenu.top_menu_hover(self, category)
                    p = self.driver.find_elements(*self.IPHONE_PRODUCTS_LINKS)
                    expected_product = p[i].text
                    sleep(6)
                    p[i].click()
                    p = self.driver.find_elements(*self.IPHONE_PRODUCTS_LINKS)

                    current_url = self.driver.current_url

                    if 'iphone' not in current_url:
                        print(f'{p[i].text} link does not work')
                    else:
                        page_product = self.driver.find_element(*self.PRODUCT_TITLE)
                        p = self.driver.find_elements(*self.IPHONE_PRODUCTS_LINKS)
                        assert expected_product == page_product.text, f'{expected_product} link opens wrong {page_product.text} product page'

                    i += 1
