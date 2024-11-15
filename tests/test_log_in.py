from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import TestLocators


class TestLogIn:

    def test_log_in_main(self,driver):
        driver.get(TestLocators.GET_MAIN_URL)
        driver.find_element(*TestLocators.SEARCH_BUTTON_ENTER).click()
        driver.find_element(*TestLocators.SEARCH_FIELD_EMAIL).send_keys('bakki_98@mail.ru')
        driver.find_element(*TestLocators.SEARCH_FIELD_PASS).send_keys('123456')
        driver.find_element(*TestLocators.SEARCH_ENT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ORDER_BUTTON))
        assert driver.find_element(*TestLocators.SEARCH_ORDER_BUTTON).text == 'Оформить заказ'

    def test_log_in_lk(self,driver):
        driver.get(TestLocators.GET_MAIN_URL)
        driver.find_element(*TestLocators.SEARCH_BUTTON_LK).click()
        driver.find_element(*TestLocators.SEARCH_FIELD_EMAIL).send_keys('bakki_98@mail.ru')
        driver.find_element(*TestLocators.SEARCH_FIELD_PASS).send_keys('123456')
        driver.find_element(*TestLocators.SEARCH_ENT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ORDER_BUTTON))
        assert driver.find_element(*TestLocators.SEARCH_ORDER_BUTTON).text == 'Оформить заказ'

    def test_log_in_registaration(self,driver):
        driver.get(TestLocators.GET_REG_URL)
        driver.find_element(*TestLocators.SEARCH_REG_ENT_BUTTON).click()
        driver.find_element(*TestLocators.SEARCH_FIELD_EMAIL).send_keys('bakki_98@mail.ru')
        driver.find_element(*TestLocators.SEARCH_FIELD_PASS).send_keys('123456')
        driver.find_element(*TestLocators.SEARCH_ENT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ORDER_BUTTON))
        assert driver.find_element(*TestLocators.SEARCH_ORDER_BUTTON).text == 'Оформить заказ'

    def test_log_in_recover_pass(self,driver):
        driver.get(TestLocators.GET_RECPASS_URL)
        driver.find_element(*TestLocators.SEARCH_RECPASS_ENT_BUTTON).click()
        driver.find_element(*TestLocators.SEARCH_FIELD_EMAIL).send_keys('bakki_98@mail.ru')
        driver.find_element(*TestLocators.SEARCH_FIELD_PASS).send_keys('123456')
        driver.find_element(*TestLocators.SEARCH_ENT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ORDER_BUTTON))
        assert driver.find_element(*TestLocators.SEARCH_ORDER_BUTTON).text == 'Оформить заказ'