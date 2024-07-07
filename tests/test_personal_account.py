import allure


from URLS import *
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:

    @allure.title("Проверка перехода по клику на Личный кабинет")
    def test_personal_account_click(self, driver, login):
        personal_account = PersonalAccountPage(driver)
        personal_account.click_personal_account()
        personal_account.timeout_profile()
        assert driver.current_url == PROFILE_URL

    @allure.title("Проверка перехода в раздел «История заказов»")
    def test_order_history(self, driver, login):
        personal_account = PersonalAccountPage(driver)
        personal_account.click_personal_account()
        personal_account.timeout_profile()
        personal_account.click_orders_history()
        assert driver.current_url == ORDER_HISTORY


    @allure.title("Проверка выхода из аккаунта")
    def test_exit_account(self, driver, login):
        personal_account = PersonalAccountPage(driver)
        personal_account.click_personal_account()
        personal_account.timeout_profile()
        personal_account.click_exit_btn()
        personal_account.timeout_login()
        assert driver.current_url == LOGIN_URL
