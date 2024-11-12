from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.conftest import driver
from tests.locators import TestLocators


class TestFromLkToConstruction:

    def test_from_lk_to_construction_button(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_BUTTON_ENTER).click()
        driver.find_element(*TestLocators.SEARCH_FIELD_EMAIL).send_keys('bakki_98@mail.ru')
        driver.find_element(*TestLocators.SEARCH_FIELD_PASS).send_keys('123456')
        driver.find_element(*TestLocators.SEARCH_ENT_BUTTON).click()
        driver.find_element(*TestLocators.SEARCH_BUTTON_LK).click()
        driver.find_element(*TestLocators.SEARCH_BUTTON_CONSTRUCTION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.SEARCH_CONTRUCTION_FIELD))

    def test_from_lk_to_construction_logo(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_BUTTON_ENTER).click()
        driver.find_element(*TestLocators.SEARCH_FIELD_EMAIL).send_keys('bakki_98@mail.ru')
        driver.find_element(*TestLocators.SEARCH_FIELD_PASS).send_keys('123456')
        driver.find_element(*TestLocators.SEARCH_ENT_BUTTON).click()
        driver.find_element(*TestLocators.SEARCH_BUTTON_LK).click()
        driver.find_element(*TestLocators.SEARCH_BUTTON_LOGO).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.SEARCH_CONTRUCTION_FIELD))