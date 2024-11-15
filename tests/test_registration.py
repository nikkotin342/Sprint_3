from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import TestLocators

class TestRegistration:


    def test_registration_success(self, driver, email, password_correct):
        driver.get(TestLocators.GET_MAIN_URL)
        driver.find_element(*TestLocators.SEARCH_BUTTON_ENTER).click()
        driver.find_element(*TestLocators.SEARCH_BUTTON_REG).click()
        driver.find_element(*TestLocators.SEARCH_FIELD_NAME).send_keys('Сашок')
        driver.find_element(*TestLocators.SEARCH_FIELD_EMAIL).send_keys(email)
        driver.find_element(*TestLocators.SEARCH_FIELD_PASS).send_keys(password_correct)
        driver.find_element(*TestLocators.SEARCH_BUTTON_REGSAVE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.SEARCH_HEADER_ENTER))
        assert driver.find_element(*TestLocators.SEARCH_HEADER_ENTER).text == 'Вход'

    def test_incorrect_password(self, driver, email, password_incorrect):
        driver.get(TestLocators.GET_MAIN_URL)
        driver.find_element(*TestLocators.SEARCH_BUTTON_ENTER).click()
        driver.find_element(*TestLocators.SEARCH_BUTTON_REG).click()
        driver.find_element(*TestLocators.SEARCH_FIELD_NAME).send_keys('Сашок')
        driver.find_element(*TestLocators.SEARCH_FIELD_EMAIL).send_keys(email)
        driver.find_element(*TestLocators.SEARCH_FIELD_PASS).send_keys(password_incorrect)
        driver.find_element(*TestLocators.SEARCH_BUTTON_REGSAVE).click()
        assert driver.find_element(*TestLocators.SEARCH_INCORRECT_PASS).text == 'Некорректный пароль'
