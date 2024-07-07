import allure

from locators.personal_account_locators import PersonalAccountLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('клик по кнопке Личный кабинет')
    def click_personal_account(self):
        self.click_element((PersonalAccountLocators.PERSONAL_ACCOUNT_BTN))

    @allure.step('клик по кнопке История заказов')
    def click_orders_history(self):
        self.click_element((PersonalAccountLocators.ORDERS_HISTORY_BTN))

    @allure.step('клик по кнопке Выход')
    def click_exit_btn(self):
        self.click_element((PersonalAccountLocators.EXIT_BTN))

    @allure.step("ожидание прогрузки страницы Личный кабинет")
    def timeout_profile(self):
        self.timeout((PersonalAccountLocators.ORDERS_HISTORY_BTN))

    @allure.step("ожидание прогрузки страницы авторизации")
    def timeout_login(self):
        self.timeout_clickable((PersonalAccountLocators.EMAIL_INPUT))
    def timeout_personal_account(self):
        self.timeout_clickable((PersonalAccountLocators.PERSONAL_ACCOUNT_BTN))

    def timeout_order_history_place(self):
        self.timeout((PersonalAccountLocators.ORDERS_HISTORY_PLACE))

    def timeout_exit(self):
        self.timeout((PersonalAccountLocators.LOGIN_BTN_REGISTRATION_FORM))

