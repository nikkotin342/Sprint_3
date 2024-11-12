from tests.locators import TestLocators


class TestLogIn:

    def test_log_in_main(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_BUTTON_ENTER).click()
        driver.find_element(*TestLocators.SEARCH_FIELD_EMAIL).send_keys('bakki_98@mail.ru')
        driver.find_element(*TestLocators.SEARCH_FIELD_PASS).send_keys('123456')
        driver.find_element(*TestLocators.SEARCH_ENT_BUTTON).click()

    def test_log_in_lk(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_BUTTON_LK).click()
        driver.find_element(*TestLocators.SEARCH_FIELD_EMAIL).send_keys('bakki_98@mail.ru')
        driver.find_element(*TestLocators.SEARCH_FIELD_PASS).send_keys('123456')
        driver.find_element(*TestLocators.SEARCH_ENT_BUTTON).click()

    def test_log_in_registaration(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.SEARCH_REG_ENT_BUTTON).click()
        driver.find_element(*TestLocators.SEARCH_FIELD_EMAIL).send_keys('bakki_98@mail.ru')
        driver.find_element(*TestLocators.SEARCH_FIELD_PASS).send_keys('123456')
        driver.find_element(*TestLocators.SEARCH_ENT_BUTTON).click()

    def test_log_in_recover_pass(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(*TestLocators.SEARCH_RECPASS_ENT_BUTTON).click()
        driver.find_element(*TestLocators.SEARCH_FIELD_EMAIL).send_keys('bakki_98@mail.ru')
        driver.find_element(*TestLocators.SEARCH_FIELD_PASS).send_keys('123456')
        driver.find_element(*TestLocators.SEARCH_ENT_BUTTON).click()