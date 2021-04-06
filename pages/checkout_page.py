from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Checkout(Page):
    CART = (By.CSS_SELECTOR, '.header-cart-link')
    PLACE_ORDER_BTN = (By.CSS_SELECTOR, 'button#place_order.button.alt')
    INVALID_INPUT_FIELDS = (By.CSS_SELECTOR, '.woocommerce-invalid input')
    FIRST_NAME_INPUT_FIELD = (By.ID, 'billing_first_name')
    LAST_NAME_INPUT_FIELD = (By.ID, 'billing_last_name')
    COMPANY_INPUT_FIELD = (By.ID, 'billing_company')
    COUNTRY_SELECT_FIELD = (By.ID, 'select2-billing_country-container')
    ADRESS_1_INPUT_FIELD = (By.ID, 'billing_address_1')
    ADRESS_2_INPUT_FIELD = (By.ID, 'billing_address_2')
    TOWN_INPUT_FIELD = (By.ID, 'billing_city')
    STATE__SELECT_FIELD = (By.ID, 'billing_state')
    ZIP_INPUT_FIELD = (By.ID, 'billing_postcode')
    PHONE_INPUT_FIELD = (By.ID, 'billing_phone')
    EMAIL_INPUT_FIELD = (By.ID, 'billing_email')
    COUNTRY_SELECT_OPTIONS = (By.CSS_SELECTOR, '.woocommerce-input-wrapper>select#billing_country')
    COUNTRY_SELECT_OPTION = (By.XPATH, "//span[contains(@class,'select2-container')]//span[contains(@class,'select2-results')]//ul//li[contains(@id,'select2-billing_country-result-9h08-AX')]")
    ERROR_MESSAGES = (By.CSS_SELECTOR, '.woocommerce-error li')
    COUNTRY_SELECT_OPTIONS_TEST = (By.XPATH, "//span[contains(@class,'select2-container')]//span[contains(@class,'select2-results')]//ul//li")


    def verify_active_fields(self):
        self.is_element_active(*self.FIRST_NAME_INPUT_FIELD)
        self.is_element_active(*self.LAST_NAME_INPUT_FIELD)
        self.is_element_active(*self.COMPANY_INPUT_FIELD)
        self.is_element_active(*self.COUNTRY_SELECT_FIELD)
        self.is_element_active(*self.ADRESS_1_INPUT_FIELD)
        self.is_element_active(*self.ADRESS_2_INPUT_FIELD)
        self.is_element_active(*self.TOWN_INPUT_FIELD)
        self.is_element_active(*self.STATE__SELECT_FIELD)
        self.is_element_active(*self.ZIP_INPUT_FIELD)
        self.is_element_active(*self.PHONE_INPUT_FIELD)
        self.is_element_active(*self.EMAIL_INPUT_FIELD)

    def click_cart(self):
        self.click(*self.CART)

    def place_order_btn_click(self):
        self.wait_for_element_appear(*self.PLACE_ORDER_BTN)
        sleep(5)
        self.click(*self.PLACE_ORDER_BTN)

    def select_country(self):
        self.wait_for_element_appear(*self.COUNTRY_SELECT_FIELD)
        self.click(*self.COUNTRY_SELECT_FIELD)
        sleep(6)
        countries = self.driver.find_elements(*self.COUNTRY_SELECT_OPTIONS_TEST)
        n = len(countries)
        i = 0
        while i < n:
            countries[i].click()
            self.wait_for_element_appear(*self.COUNTRY_SELECT_FIELD)
            self.click(*self.COUNTRY_SELECT_FIELD)
            countries = self.driver.find_elements(*self.COUNTRY_SELECT_OPTIONS_TEST)
            i += 1

    def invalid_fields(self, query):
        invalid_fields = self.driver.find_elements(*self.INVALID_INPUT_FIELDS)
        assert int(len(invalid_fields)) == int(query), f'User can leave {int(len(invalid_fields)) - int(query)} required fields blank'

    def verify_error_messages(self):
        expected_messages = ['Billing First name', 'Billing Last name', 'Billing Street address', 'Billing Town / City', 'Billing ZIP', 'Billing Phone', 'Billing Email address', 'Invalid payment method']
        e = self.driver.find_elements(*self.ERROR_MESSAGES)
        i = 0
        for x in e:
            assert expected_messages[i] in x.text, f'User see {x.text}, but expected {expected_messages[i]}'
            i += 1


