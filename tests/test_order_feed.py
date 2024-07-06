import allure

from URLS import *
from pages.main_function_page import MainFunctionPage
from pages.order_feed_page import OrderFeedPage


class TestOrderFeed:

    @allure.title("Проверка появления всплывающего окна с деталями при клике на заказ")
    def test_open_order_detail_popup(self, driver):
        order_page = OrderFeedPage(driver)
        order_page.get_new_url(FEED_URL)
        order_page.timeout_order_feed_page()
        order_page.click_last_order()
        order_page.timeout_order_popup()
        assert order_page.check_order_detail_popup()

    @allure.title("Проверка отображения заказа пользователя на стренице Лента заказов")
    def test_user_order_in_order_feed(self, driver, create_order):
        order_page = OrderFeedPage(driver)
        order_page.timeout_close_btn()
        order_page.close_order_id_popup()
        order_number = order_page.get_order_number()
        order_page.click_order_feed_header_btn()
        order_page.timeout_order_feed_page()
        order_list = order_page.get_order_list()
        assert order_number in order_list

    @allure.title("Проверка, что при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_day_counter_increases(self, driver, login):
        order_page = OrderFeedPage(driver)
        order_page.get_new_url(FEED_URL)
        order_page.timeout_order_feed_page()
        amount_before_order = order_page.get_today_order_amount()
        main_function = MainFunctionPage(driver)
        main_function.get_new_url(BASE_URL)
        main_function.timeout_url(BASE_URL)
        main_function.add_ingredient_in_basket()
        main_function.click_create_oreder_btn()
        order_page.timeout_close_btn()
        order_page.close_order_id_popup()
        order_page.get_new_url(FEED_URL)
        order_page.timeout_order_feed_page()
        amount_after_order = order_page.get_today_order_amount()
        assert amount_before_order < amount_after_order

    @allure.title("Проверка, что при создании нового заказа счётчик Выполнено за все время увеличивается")
    def test_all_counter_increases(self, driver, login):
        order_page = OrderFeedPage(driver)
        order_page.get_new_url(FEED_URL)
        order_page.timeout_order_feed_page()
        amount_before_order = order_page.get_all_order_amount()
        main_function = MainFunctionPage(driver)
        main_function.get_new_url(BASE_URL)
        main_function.timeout_url(BASE_URL)
        main_function.add_ingredient_in_basket()
        main_function.click_create_oreder_btn()
        order_page.timeout_close_btn()
        order_page.close_order_id_popup()
        order_page.get_new_url(FEED_URL)
        order_page.timeout_order_feed_page()
        amount_after_order = order_page.get_all_order_amount()
        assert amount_before_order < amount_after_order

    @allure.title("Проверка отображения номера оформленного заказа в разделе В работе")
    def test_check_order_number_in_progress(self, driver, create_order):
        order_page = OrderFeedPage(driver)
        order_page.timeout_close_btn()
        order_page.close_order_id_popup()
        order_number = order_page.get_order_number()
        order_page.click_order_feed_header_btn()
        order_page.timeout_order_feed_page()
        order_page.timeout_order_in_progress()
        order_in_progress = order_page.get_order_numbers_in_progress()
        assert order_number in order_in_progress
