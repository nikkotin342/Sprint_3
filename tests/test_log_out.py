from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('bakki_98@mail.ru')
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()#Кнопка "Личный кабинет"
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')))#Кнопка "Выйти"
driver.find_element(By.XPATH, '/html/body/div/div/main/div/nav/ul/li[3]/button').click()#Кнопка "Выйти"
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/h2')))#Локатор указывает на заголовок "Вход" в меню входа в УЗ

driver.quit()