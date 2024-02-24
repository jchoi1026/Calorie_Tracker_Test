import time

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

        # Add meals and calories
        add_meals_page.execute_add_meal("Rice", 130)
        time.sleep(5)

        # Verify if "Total Calories" show the Calories figure

        # Verify if the record you put is listed properly
