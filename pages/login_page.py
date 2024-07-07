import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('заполнгение поля Email')
    def fill_email(self, email):
        self.fill_input((LoginPageLocators.EMAIL_INPUT), email)

    @allure.step('заполнгение поля Пароль')
    def fill_password(self, password):
        self.fill_input((LoginPageLocators.PASSWORD_INPUT), password)

    @allure.step('клик по кнопке Войти')
    def click_login_btn(self):
        self.click_element((LoginPageLocators.LOGIN_BTN_LOGIN_PAGE))

    @allure.step('ожидание кликабельности кнопки Булки')
    def timeout_buns(self):
        self.timeout_clickable((LoginPageLocators.BUNS_BTN))