from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



class TopMenu(Page):
    LOGO = (By.CSS_SELECTOR, '#logo>a')
    MOBILE_MENU = (By.CSS_SELECTOR, 'ul.mobile-nav>li.nav-icon>a')
    CART = (By.CSS_SELECTOR, 'ul.header-nav>li.cart-item>a.header-cart-link')
    TOP_MENU_LINKS = (By.CSS_SELECTOR, '.header-nav>li.menu-item>a')
    FIRST_MENU_LINK = (By.XPATH, "//li[@id='menu-item-469']//a[@class='nav-top-link']")
    FIRST_MENU_LINK_MOBILE = (By.CSS_SELECTOR, 'ul.nav-vertical>li.menu-item-468>a')
    SLIDER = (By.CSS_SELECTOR, '.slider-wrapper')
    IPHONE_MENU_LINK = (By.XPATH, "//a[@class = 'nav-top-link' and contains(@href,'product-category/iphone')]")

    def open_main_page(self):
        self.open_url()

    def click_logo(self):
        self.wait_for_element_click(*self.LOGO)
        self.click(*self.LOGO)

    def click_cart(self):
        self.click(*self.CART)

    def click_first_link_top_menu(self):
        test_mode = self.is_mobile(*self.MOBILE_MENU)
        if test_mode == 'mobile':
            self.click(*self.MOBILE_MENU)
            self.click(*self.FIRST_MENU_LINK_MOBILE)
        else:
            self.click(*self.FIRST_MENU_LINK)

    def verify_main_page_opened(self):
        self.find_element(*self.SLIDER)

    def top_menu_hover(self, category):
        top_menu_links = self.driver.find_elements(*self.TOP_MENU_LINKS)
        for e in top_menu_links:
            if e.text == category and category == 'IPHONE':
                top_menu_link = self.driver.find_element(*self.IPHONE_MENU_LINK)
                action = ActionChains(self.driver)
                action.move_to_element(top_menu_link)
                action.perform()

