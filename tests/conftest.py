import random

import pytest

from selenium import webdriver



@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture()
def email():
    return f"bakki_{random.randint(100, 999)}@mail.ru"

@pytest.fixture()
def password_correct():
    return f'{random.randint(100000, 999999)}'

@pytest.fixture()
def password_incorrect():
    return f'{random.randint(10000,99999)}'