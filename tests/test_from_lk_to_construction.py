

from tests import help_for_tests
from tests.conftest import driver
from tests.locators import TestLocators


class TestFromLkToConstruction:

    def test_from_lk_to_construction_button(self, driver):
        driver.get(help_for_tests.GET_MAIN_URL)
        driver.find_element(*TestLocators.SEARCH_BUTTON_ENTER).click()
        driver.find_element(*TestLocators.SEARCH_FIELD_EMAIL).send_keys('bakki_98@mail.ru')
        driver.find_element(*TestLocators.SEARCH_FIELD_PASS).send_keys('123456')
        driver.find_element(*TestLocators.SEARCH_ENT_BUTTON).click()
        driver.find_element(*TestLocators.SEARCH_BUTTON_LK).click()
        driver.find_element(*TestLocators.SEARCH_BUTTON_CONSTRUCTION).click()
        assert driver.find_element(*TestLocators.SEARCH_CONTRUCTION_FIELD).is_displayed()

    def test_from_lk_to_construction_logo(self,driver):
        driver.get(help_for_tests.GET_MAIN_URL)
        driver.find_element(*TestLocators.SEARCH_BUTTON_ENTER).click()
        driver.find_element(*TestLocators.SEARCH_FIELD_EMAIL).send_keys('bakki_98@mail.ru')
        driver.find_element(*TestLocators.SEARCH_FIELD_PASS).send_keys('123456')
        driver.find_element(*TestLocators.SEARCH_ENT_BUTTON).click()
        driver.find_element(*TestLocators.SEARCH_BUTTON_LK).click()
        driver.find_element(*TestLocators.SEARCH_BUTTON_LOGO).click()
        assert driver.find_element(*TestLocators.SEARCH_CONTRUCTION_FIELD).is_displayed()