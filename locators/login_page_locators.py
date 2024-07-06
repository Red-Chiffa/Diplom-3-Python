from selenium.webdriver.common.by import By


class LoginPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/../input")  # поле ввода имени
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/../input")  # поле ввода email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/../input")  # поле ввода пароля
    LOGIN_BTN_LOGIN_PAGE = (By.XPATH, "//button[text()='Войти']")  # кнопка Войти на странице авторизации
    BUNS_BTN = (By.XPATH, "//span[text() = 'Булки']/parent::div")