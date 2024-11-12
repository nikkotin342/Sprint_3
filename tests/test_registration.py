from tests.locators import TestLocators

class TestRegistration:


    def test_registration_success(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_BUTTON_ENTER).click()
        driver.find_element(*TestLocators.SEARCH_BUTTON_REG).click()
        driver.find_element(*TestLocators.SEARCH_FIELD_NAME).send_keys('Сашок')
        driver.find_element(*TestLocators.SEARCH_FIELD_EMAIL).send_keys('bakki_98@mail.ru')
        driver.find_element(*TestLocators.SEARCH_FIELD_PASS).send_keys('123456')
        driver.find_element(*TestLocators.SEARCH_BUTTON_REGSAVE).click()

    def test_incorrect_password(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SEARCH_BUTTON_ENTER).click()
        driver.find_element(*TestLocators.SEARCH_BUTTON_REG).click()
        driver.find_element(*TestLocators.SEARCH_FIELD_NAME).send_keys('Сашок')
        driver.find_element(*TestLocators.SEARCH_FIELD_EMAIL).send_keys('bakki_98@mail.ru')
        driver.find_element(*TestLocators.SEARCH_FIELD_PASS).send_keys('12345')
        driver.find_element(*TestLocators.SEARCH_BUTTON_REGSAVE).click()
        assert driver.find_element(*TestLocators.SEARCH_INCORRECT_PASS).text == 'Некорректный пароль'
