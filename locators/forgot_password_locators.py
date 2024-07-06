from selenium.webdriver.common.by import By


class ForgotPasswodrLocators:
    RESTORE_PASSWORD_BTN = (By.XPATH, "//a[text() = 'Восстановить пароль']")
    EMAIL_INPUT = (By.XPATH, ".//div[contains(@class, 'input')]/input")
    RESTORE_BTN = (By.XPATH, ".//button[text() = 'Восстановить']")
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Введите новый пароль']/parent::div")
    SHOW_HIDE_BTN = (By.XPATH, '//div[@class="input__icon input__icon-action"]')


