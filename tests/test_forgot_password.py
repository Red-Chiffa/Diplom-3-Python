import allure

from URLS import *
from pages.forgot_password_page import ForgotPasswordPage


class TestForgotPassword:

    @allure.title('переход на страницу восстановления пароля по кнопке «Восстановить пароль')
    def test_go_to_restore_passwprd_page(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.driver.get(LOGIN_URL)
        forgot_password_page.timeout_restore_password_btn()
        forgot_password_page.click_restore_password_btn()
        forgot_password_page.timeout_restore_btn()
        assert driver.current_url == FORGOT_PASSWORD_URL

    @allure.title('ввод почты и клик по кнопке Восстановить')
    def test_fill_email_and_restore_btn_click(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.driver.get(FORGOT_PASSWORD_URL)
        forgot_password_page.timeout_restore_btn()
        forgot_password_page.fill_email('am1234@ya.ru')
        forgot_password_page.click_restore_btn()
        forgot_password_page.timeout_show_hide_btn()
        assert driver.current_url == RESET_PASSWORD_URL

    @allure.title('Проверка, что нажатие на кнопку показать/скрыть делает поле Пароль активным')
    def test_fpassword_input_is_active(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.driver.get(FORGOT_PASSWORD_URL)
        forgot_password_page.timeout_restore_btn()
        forgot_password_page.fill_email('am1234@ya.ru')
        forgot_password_page.click_restore_btn()
        forgot_password_page.timeout_show_hide_btn()
        forgot_password_page.click_show_hide_btn()
        real_attribute = forgot_password_page.get_password_input_attribute()
        assert 'input_status_active' in real_attribute
