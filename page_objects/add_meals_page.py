from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


# Bring a parent object (BasePage)
class AddMealPage(BasePage):
    __url = "https://practice.expandtesting.com/tracalorie/?#"
    __add_item_locator = (By.ID, "item-name")
    __add_calories_locator = (By.ID, "item-calories")
    __add_meal_btn_locator = (By.XPATH, "//form[@class='col']/div/button[1]")
    __total_calories_header_locator = (By.XPATH, "//body//h3[@class='center-align']")
    __list_first_meals_locator = (By.XPATH, "//li[@id='item-0']//strong")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_add_meal(self, food: str, calorie: int):
        super()._type(self.__add_item_locator, food)
        super()._type(self.__add_calories_locator, calorie)
        super()._click(self.__add_meal_btn_locator)

    def is_total_calories_displayed(self,) -> bool:
        super()._wait_until_element_is_visible(self.__total_calories_header_locator)
        return super()._find(self.__total_calories_header_locator).is_displayed()

    def get_meal_added_to_list(self) -> str:
        return super()._get_text(self.__list_first_meals_locator)

