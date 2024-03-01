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
        add_meals_page.execute_add_meal("rice", 130)
        time.sleep(5)

        # Verify if "Total Calories" show the Calories figure
        assert add_meals_page.is_total_calories_displayed(), "ERROR. Total Calories should be displayed."

        # Verify if the record you put is listed properly
        assert add_meals_page.get_meal_added_to_list() == "rice:", "ERROR. First meal item should be listed."
