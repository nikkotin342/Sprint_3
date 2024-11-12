from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import TestLocators


class TestSelectElementsOfConstruction:

    def test_select_elements_of_construction(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_BUTTON_SAUCES).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.SEARCH_FIELD_SAUCES))
        driver.find_element(*TestLocators.SEARCH_BUTTON_STAFFS).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.SEARCH_FIELD_STAFFS))
        driver.find_element(*TestLocators.SEARCH_BUTTON_BREADS).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.SEARCH_FIELD_BREADS))