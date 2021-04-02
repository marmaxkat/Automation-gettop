from pages.top_menu import TopMenu


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.top_menu = TopMenu(self.driver)