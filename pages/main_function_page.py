import allure

from locators.main_function_locators import MainFunctionLocators
from pages.base_page import BasePage
from seletools.actions import drag_and_drop


class MainFunctionPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('клик по кнопке Конструктор')
    def click_constructor_btn(self):
        self.click_element((MainFunctionLocators.CONSTRUCTOR_BTN))

    @allure.step('ожидание кликабельности кнопки Булки')
    def timeout_buns(self):
        self.timeout_clickable(MainFunctionLocators.BUN_FLUOR)

    @allure.step('клик по кнопке Летна заказов')
    def click_order_feed(self):
        self.click_element((MainFunctionLocators.ORDER_FEED))

    @allure.step('ожидание отображения списка Ленты заказов')
    def timeout_order_feed(self):
        self.timeout(MainFunctionLocators.ORDER_FEED_LIST)

    @allure.step('проверка отображения списка Ленты заказов')
    def check_order_feed_presents(self):
        return self.check_element_is_displayed((MainFunctionLocators.ORDER_FEED_LIST))

    @allure.step('клик по Флюоресцентной булке')
    def click_ingredient(self):
        self.click_element((MainFunctionLocators.BUN_FLUOR))

    @allure.step('проверка отображения поп-апа')
    def check_popup_presents(self):
        return self.check_element_is_displayed((MainFunctionLocators.MODAL_WINDOW))

    @allure.step('ожидание поп-апа')
    def timeout_popup(self):
        self.timeout((MainFunctionLocators.MODAL_WINDOW))

    @allure.step('закрытие поп-апа')
    def close_popup(self):
        self.click_element((MainFunctionLocators.CLOSE_BTN))

    @allure.step('проверка отображения Флюоресцентной булки')
    def check_buns(self):
        return self.check_element_is_displayed((MainFunctionLocators.BUN_FLUOR))

    @allure.step("добавление ингредиента в корзину")
    def add_ingredient_in_basket(self):
        source = self.wait_and_find_element_located(MainFunctionLocators.BUN_BUTTON)
        target = self.wait_and_find_element_located(MainFunctionLocators.BASKET_AREA)
        drag_and_drop(self.driver, source, target)

    @allure.step("получение значения счетчика ингредиента")
    def get_ingredient_counter_value(self):
        result = self.get_element_text((MainFunctionLocators.BUN_FLUOR_COUNTER))
        return result

    @allure.step("клик по кнопке Оформить заказ")
    def click_create_oreder_btn(self):
        self.click_element((MainFunctionLocators.CREATE_ORDER_BTN))


    @allure.step("Получение строки «Ваш заказ начали готовить»")
    def order_id_in_modal(self):
        self.timeout((MainFunctionLocators.ORDER_ID))
        return self.get_element_text((MainFunctionLocators.ORDER_ID))

