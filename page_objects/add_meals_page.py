from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


# Bring a parent object (BasePage)
class AddMealPage(BasePage):
    __url = "https://practice.expandtesting.com/tracalorie/?#"
    __add_item_locator = (By.ID, "item-name")
    __add_calories_locator = (By.ID, "item-calories")
    __add_meal_btn_locator = (By.XPATH, "//form[@class='col']/div/button[1]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_add_meal(self, food: str, calorie: int):
        super()._type(self.__add_item_locator, food)
        super()._type(self.__add_calories_locator, calorie)
        super()._click(self.__add_meal_btn_locator)


