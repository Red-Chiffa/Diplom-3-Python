import allure

from URLS import *
from pages.main_function_page import MainFunctionPage


class TestMainFunction:

    @allure.title("Проверка перехода по клику на «Конструктор»")
    def test_click_constructor_btn(self, driver):
        main_function = MainFunctionPage(driver)
        main_function.get_new_url(LOGIN_URL)
        main_function.click_constructor_btn()
        main_function.timeout_buns()
        assert driver.current_url == BASE_URL

    @allure.title("Проверка перехода по клику на «Лента заказов»")
    def test_click_order_feed(self, driver):
        main_function = MainFunctionPage(driver)
        main_function.click_order_feed()
        main_function.timeout_order_feed()
        assert main_function.check_order_feed_presents()

    @allure.title("Проверка появления всплывающего окна с деталями при клике на ингредиент")
    def test_click_ingredient(self, driver):
        main_function = MainFunctionPage(driver)
        main_function.click_ingredient()
        assert main_function.check_popup_presents()

    @allure.title("Проверка закрытия всплывающего окна кликом по крестику ")
    def test_close_popup(self, driver):
        main_function = MainFunctionPage(driver)
        main_function.click_ingredient()
        main_function.timeout_popup()
        main_function.close_popup()
        assert main_function.check_buns()

    @allure.title("Проверка добавлении ингредиента в заказ, увеличения счётчика этого ингридиента")
    def test_ingredient_counter_increases(self, driver):
        main_function = MainFunctionPage(driver)
        main_function.timeout_url(BASE_URL)
        main_function.add_ingredient_in_basket()
        counter = main_function.get_ingredient_counter_value()
        assert counter == '2'

    @allure.title("Проверка создания заказа")
    def test_create_order(self, driver, login):
        main_function = MainFunctionPage(driver)
        main_function.timeout_url(BASE_URL)
        main_function.add_ingredient_in_basket()
        main_function.click_create_oreder_btn()
        assert main_function.order_id_in_modal() == "идентификатор заказа"
