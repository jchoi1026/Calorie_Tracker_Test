import pytest


class TestAddMeals:
    @pytest.mark.addMeals
    @pytest.mark.positive
    def test_add_meals(self, driver):
        # Open Url
        driver.get("https://practice.expandtesting.com/tracalorie/")