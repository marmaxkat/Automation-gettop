from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ProductList(Page):
    SORT_OPTIONS_DROPDOWN = (By.CSS_SELECTOR, 'select.orderby')
    PRODUCT_PAGES_NAV_LINKS = (By.CSS_SELECTOR, '.woocommerce-pagination>ul>li>a')
    SORTED_OPTION = (By.XPATH, "//option[contains(@selected,'selected')]")
    IPHONE_DROP_DOWN = (By.CSS_SELECTOR, '#menu-item-469>ul.nav-dropdown>li')
    PRODUCT_LIST = (By.CSS_SELECTOR, '.products div.product')

    def select_sort_option(self, alias: str):
        select = Select(self.find_element(*self.SORT_OPTIONS_DROPDOWN))
        select.select_by_value(f'{alias}')

    def verify_sort_order (self, option: str):
        selected_option = self.driver.find_element(*self.SORTED_OPTION)
        assert selected_option.text == option, f'Actual sort order {selected_option.text}, expected sort order{option}'

    def verify_page_navigation(self):
        self.wait_for_element_click(*self.PRODUCT_PAGES_NAV_LINKS)
        nav_links = self.driver.find_elements(*self.PRODUCT_PAGES_NAV_LINKS)
        n = len(nav_links)
        i = 0
        while i < n:
            nav_links[i].click()
            self.wait_for_element_click(*self.PRODUCT_PAGES_NAV_LINKS)
            nav_links = self.driver.find_elements(*self.PRODUCT_PAGES_NAV_LINKS)
            nav_links[i].click()
            self.wait_for_element_click(*self.PRODUCT_PAGES_NAV_LINKS)
            nav_links = self.driver.find_elements(*self.PRODUCT_PAGES_NAV_LINKS)
            i += 1

    def verify_products_in_category(self, category):
        products_in_menu = self.driver.find_elements(*self.IPHONE_DROP_DOWN)
        products_in_list = self.driver.find_elements(*self.PRODUCT_LIST)
        assert len(products_in_menu) == len(products_in_list), f'User can see {len(products_in_list)} instead of {len(products_in_menu)}'

