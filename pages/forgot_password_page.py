import allure

from locators.forgot_password_locators import ForgotPasswodrLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('клик по кнопке восстановтиь пароль в подвале страницы авторизации')
    def click_restore_password_btn(self):
        self.click_element((ForgotPasswodrLocators.RESTORE_PASSWORD_BTN))

    @allure.step('заполнгение поля Email')
    def fill_email(self, email):
        self.fill_input((ForgotPasswodrLocators.EMAIL_INPUT), email)

    @allure.step('клик по кнопке восстановтиь пароль на стренице восстановления пароля')
    def click_restore_btn(self):
        self.click_element((ForgotPasswodrLocators.RESTORE_BTN))

    @allure.step('клик по кнопке показать/скрыть пароль поля Пароль')
    def click_show_hide_btn(self):
        self.click_element((ForgotPasswodrLocators.SHOW_HIDE_BTN))

    def timeout_restore_password_btn(self):
        self.timeout((ForgotPasswodrLocators.RESTORE_PASSWORD_BTN))

    def timeout_restore_btn(self):
        self.timeout((ForgotPasswodrLocators.RESTORE_BTN))

    def timeout_show_hide_btn(self):
        self.timeout((ForgotPasswodrLocators.SHOW_HIDE_BTN))

    def get_password_input_attribute(self):
        attribute = self.get_element_attribute((ForgotPasswodrLocators.PASSWORD_INPUT), 'class')
        return attribute
