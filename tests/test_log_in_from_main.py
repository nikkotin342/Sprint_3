from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()#Кнопка "войти в аккаунт"
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('alex@ya.ru')
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()#Кнопка "Войти"

driver.quit()


driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()#Кнопка "Личный кабинет"
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('alex@ya.ru')
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

driver.quit()


driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()#Кнопка "Войти"
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('alex@ya.ru')
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

driver.quit()


driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()#Кнопка "Войти"
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('alex@ya.ru')
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

driver.quit()