from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests import help_for_tests
from tests.locators import TestLocators


class TestSelectElementsOfConstruction:

    def test_select_elements_of_construction(self,driver):
        driver.get(help_for_tests.GET_MAIN_URL)
        driver.find_element(*TestLocators.SEARCH_BUTTON_SAUCES).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.SEARCH_HEADER_SAUCES))
        assert driver.find_element(*TestLocators.SEARCH_BUTTON_SAUCES).text == "Соусы"
        driver.find_element(*TestLocators.SEARCH_BUTTON_STAFFS).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.SEARCH_HEADER_STAFFS))
        assert driver.find_element(*TestLocators.SEARCH_BUTTON_STAFFS).text == "Начинки"
        driver.find_element(*TestLocators.SEARCH_BUTTON_BREADS).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.SEARCH_HEADER_BREADS))
        assert driver.find_element(*TestLocators.SEARCH_BUTTON_BREADS).text == "Булки"