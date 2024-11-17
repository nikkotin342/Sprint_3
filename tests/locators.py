from selenium.webdriver.common.by import By

class TestLocators:
    SEARCH_BUTTON_ENTER = [By.XPATH, '//*[contains(@class,"button_button_size_large") and text()="Войти в аккаунт"]']# Кнопка "Войти в аккаунт"
    SEARCH_BUTTON_REG = [By.XPATH, '//*[contains(@class,"Auth_link")]']# Кнопка "Зарегистрироваться"
    SEARCH_FIELD_NAME = [By.XPATH, '//fieldset[1]/div/div/input']# Заполнить поле для Имени
    SEARCH_FIELD_EMAIL = [By.XPATH, '//fieldset[2]/div/div/input']# Заполнить поле для Емаил
    SEARCH_FIELD_PASS = [By.XPATH, '//fieldset[3]/div/div/input']# Заполнить поле для Пароля
    SEARCH_BUTTON_REGSAVE = [By.XPATH, '//*[contains(@class,"button_button_type_primary")]']# Кнопка "Зарегистрироваться" во вкладке регистрации
    SEARCH_INCORRECT_PASS = [By.XPATH, '//*[contains(@class, "input__error")]']# Ошибка "Некорректный пароль"
    SEARCH_ENT_BUTTON = [By.XPATH, '//*[contains(@class, "button_type_primary")]']# Кнопка "Войти" во вкладке входа
    SEARCH_BUTTON_LK = [By.XPATH, '//*[contains(@class, "AppHeader") and text() = "Личный Кабинет"]']# Кнопка "Личный кабинет"
    SEARCH_REG_ENT_BUTTON = [By.XPATH, '//*[contains(@class, "Auth_link") and text() = "Войти"]']# Кнопка "Войти" во вкладке регистрации
    SEARCH_RECPASS_BUTTON = [By.XPATH, '//*[contains(@class, "Auth_link") and text() = "Восстановить пароль"]']# Кнопка "Войти" во вкладке восстановления пароля
    SEARCH_RECPASS_ENT_BUTTON = SEARCH_REG_ENT_BUTTON
    SEARCH_USER_FIELD = [By.XPATH, '//*[contains(@class, "Account_text")]']# Поле пользователя во вкладке Личный Кабинет
    SEARCH_BUTTON_CONSTRUCTION = [By.XPATH, '//*[contains(@class, "AppHeader") and text() = "Конструктор"]']# Кнопка "Конструктор"
    SEARCH_CONTRUCTION_FIELD = [By.XPATH, '//*[contains(@class, "BurgerIngredients_ingredients")]']# Поле конструктора с ингредиентами
    SEARCH_BUTTON_LOGO = [By.XPATH, '//*[@href = "/"]']# Кнопка на логотипе "Stellar Burgers"
    SEARCH_BUTTON_EXIT = [By.XPATH, '//*[contains(@class, "Account_button") and text() = "Выход"]']# Кнопка "Выход"
    SEARCH_HEADER_ENTER = [By.XPATH, '//*[text()="Вход"]']# Заголовок "Вход" во вкладке входа в УЗ
    SEARCH_BUTTON_SAUCES = [By.XPATH, '//*[contains(@class, "text_type_main-default") and text() = "Соусы"]']# Кнопка "Соусы" в конструкторе
    SEARCH_BUTTON_STAFFS = [By.XPATH, '//*[contains(@class, "text_type_main-default") and text() = "Начинки"]']# Кнопка "Начинки" в конструкторе
    SEARCH_BUTTON_BREADS = [By.XPATH, '//*[contains(@class, "text_type_main-default") and text() = "Булки"]']# Кнопка "Булки" в конструкторе
    SEARCH_HEADER_SAUCES = [By.XPATH, '//*[contains(@class, "type_current")]']# Активный заголовок "Соусы" в меню конструктора
    SEARCH_HEADER_STAFFS = [By.XPATH, '//*[contains(@class, "type_current")]']# Активный заголовок "Начинки" в меню конструктора
    SEARCH_HEADER_BREADS = [By.XPATH, '//*[contains(@class, "type_current")]']# Активный заголовок "Булки" в меню конструктора
    SEARCH_FIELD_SAUCES = [By.XPATH, '//*[contains(@class, "text_type_main-medium") and text() = "Соусы"]']# Заголовок "Соусы" в поле с соусами в ингредиентах конструктора
    SEARCH_FIELD_STAFFS = [By.XPATH, '//*[contains(@class, "text_type_main-medium") and text() = "Начинки"]']# Заголовок "Начинки" в поле с соусами в ингредиентах конструктора
    SEARCH_FIELD_BREADS = [By.XPATH, '//*[contains(@class, "text_type_main-medium") and text() = "Булки"]']# Заголовок "Булки" в поле с соусами в ингредиентах конструктора
    SEARCH_ORDER_BUTTON = [By.XPATH, '//*[contains(@class, "button_size_large")]']# Кнопка "Оформить заказ"
    SEARCH_CONTRUCTION_HEADER = [By.XPATH, '//*[contains(@class, "text_type_main-large")]']# Заголовок меню конструктора с текстом "Соберите бургер"