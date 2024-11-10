from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")


driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()#Кнопка "войти в аккаунт"
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()#Кнопка "Зарегистрироваться"
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('Сашок')#Поле "Имя"
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('bakki_98@mail.ru')#Поле "Почта"
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys('123456')#Поле "Пароль"
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()#Кнопка "Зарегистрироваться"

driver.quit()


driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('Сашок')
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('bakki_98@mail.ru')
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys('12345')
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()
assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p').text == 'Некорректный пароль'# Локатор указывает на текст ошибки

driver.quit()