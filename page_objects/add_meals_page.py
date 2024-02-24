from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


# Bring a parent object (BasePage)
class AddMealPage(BasePage):
    __url = "https://practice.expandtesting.com/tracalorie/?#"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)
