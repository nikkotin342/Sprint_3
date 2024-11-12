from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import TestLocators


class TestGoToLK:

    def test_go_to_lk(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_BUTTON_ENTER).click()
        driver.find_element(*TestLocators.SEARCH_FIELD_EMAIL).send_keys('bakki_98@mail.ru')
        driver.find_element(*TestLocators.SEARCH_FIELD_PASS).send_keys('123456')
        driver.find_element(*TestLocators.SEARCH_ENT_BUTTON).click()
        driver.find_element(*TestLocators.SEARCH_BUTTON_LK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.SEARCH_USER_FIELD))