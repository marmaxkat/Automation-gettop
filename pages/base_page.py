from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.base_url = 'https://gettop.us/'

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open_url(self,end_url=''):
        self.driver.get(f'{self.base_url}{end_url}')

    def input_text(self, text: str, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def is_element_active(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def verify_text(self, expected_text: str, *locator):
        """
        Search for a webelement, get its text, compare with expected_text
        :param expected_text: Text to be in webelement
        :param locator: Search strategy and locator of webelemnt (ex. (By.ID, 'id') )
        """
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f"Expected {expected_text} does not match actual {actual_text}"

    def verify_url_contains_query(self, query):
        assert query in self.driver.current_url, f'{query} is not in {self.driver.current_url}'

    def store_original_window(self):
        self.original_window = self.driver.current_window_handle

    def switch_to_new_window(self):
        self.driver.wait.until(EC.new_window_is_opened)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def close_window_and_switch_to_old_window(self):
        self.driver.close()
        self.driver.switch_to.window(self.original_window)