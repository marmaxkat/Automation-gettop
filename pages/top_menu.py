from pages.base_page import Page
from selenium.webdriver.common.by import By


class TopMenu(Page):
    LOGO = (By.ID, 'logo')
    TOP_MENU_LINKS = (By.CSS_SELECTOR, 'ul.header-nav-main>li.menu-item"')
    FIRST_MENU_LINK = (By.ID, 'menu-item-468')
    SLIDER = (By.CSS_SELECTOR, '.slider-wrapper')

    def open_main_page(self):
        self.open_url()

    def click_logo(self):
        self.wait_for_element_click(*self.LOGO)
        self.click(*self.LOGO)

    def click_first_link_top_menu(self):
        self.click(*self.FIRST_MENU_LINK)

    def verify_main_page_opened(self):
        self.find_element(*self.SLIDER)