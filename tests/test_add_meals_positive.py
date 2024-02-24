import pytest
from page_objects.add_meals_page import AddMealPage


class TestAddMeals:
    @pytest.mark.addMeals
    @pytest.mark.positive
    def test_add_meals(self, driver):
        # Create an testMealsPage obj
        add_meals_page = AddMealPage(driver)

        # Open Url
        add_meals_page.open()
