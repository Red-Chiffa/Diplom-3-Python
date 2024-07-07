from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/../input")  # поле ввода email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/../input")  # поле ввода пароля
    PERSONAL_ACCOUNT_BTN = [By.XPATH, "//a[@href = '/account']"]  # кнопка "Личный кабинет"
    LOGIN_BTN_REGISTRATION_FORM = (By.XPATH, "//a[text()='Войти']")  # кнопка Войти на странице регистрации и на странице восстановления пароля
    ORDERS_HISTORY_BTN = (By.XPATH, "//a[text()='История заказов']")
    EXIT_BTN = (By.XPATH, "//button[text()='Выход']")
    ORDERS_HISTORY_PLACE = (By.XPATH, "//div[contains(@class, 'OrderHistory')]")
