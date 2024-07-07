import allure

from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("ожидание поп-апа")
    def timeout_order_popup(self):
        self.timeout((OrderFeedLocators.CONSIST_TEXT))

    @allure.step("клие по кнопке Лента заказов в хедере")
    def click_order_feed_header_btn(self):
        self.click_element((OrderFeedLocators.ORDER_FEED_HEADER_BTN))

    @allure.step("ожидание загрузки страницы Лента заказов")
    def timeout_order_feed_page(self):
        self.timeout((OrderFeedLocators.ALL_ORDER_AMOUNT))

    @allure.step("клик по последнему заказу")
    def click_last_order(self):
        self.click_element((OrderFeedLocators.ORDER_ITEM))

    @allure.step("проверка отображения поп-апа с деталями заказа")
    def check_order_detail_popup(self):
        return self.check_element_is_displayed((OrderFeedLocators.CONSIST_TEXT))

    @allure.step("ожидание номера заказа")
    def timeot_order_id(self):
        self.timeout((OrderFeedLocators.ORDER_NUMBER))

    @allure.step("ожидание кнопки закрытия поп-апа")
    def timeout_close_btn(self):
        self.timeout_clickable((OrderFeedLocators.CLOSE_MODAL_BTN))

    @allure.step("закрытие поп-апа")
    def close_order_id_popup(self):
        self.click_element((OrderFeedLocators.CLOSE_MODAL_BTN))

    @allure.step("получение номера заказа")
    def get_order_number(self):
        return self.get_element_text((OrderFeedLocators.ORDER_NUMBER))

    @allure.step("получение списка заказов")
    def get_order_list(self):
        return self.get_element_text((OrderFeedLocators.ORDERS_LIST))

    @allure.step("получение значения счетчика Выолнено за сегодня")
    def get_today_order_amount(self):
        return self.get_element_text((OrderFeedLocators.TODAY_ORDER_AMOUNT))

    @allure.step("получение значения счетчика Выолнено за все время")
    def get_all_order_amount(self):
        return self.get_element_text((OrderFeedLocators.ALL_ORDER_AMOUNT))

    @allure.step("ожидание появления номера заказа В работе")
    def timeout_order_in_progress(self):
        self.invisibility_of_element((OrderFeedLocators.ALL_ORDER_ARE_DONE_TEXT))

    @allure.step("получение номера заказа В работе")
    def get_order_numbers_in_progress(self):
        return self.get_element_text((OrderFeedLocators.ORDER_IN_PROGRESS))

