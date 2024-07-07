from selenium.webdriver.common.by import By

class OrderFeedLocators:

    ORDER_FEED_HEADER_BTN = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    ORDER_ITEM = (By.XPATH, "//li[1]/a[contains(@class, 'OrderHistory_link')]")
    CONSIST_TEXT = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//../p[contains(text(),'Cостав')]")
    ORDER_HISTORY_NUMBER = (By.XPATH, "//li[1]//div[contains(@class, 'OrderHistory')]//..//p[contains(text(),'#')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow')]")
    TODAY_ORDER_AMOUNT = (By.XPATH, "//div[3]/p[contains(@class, 'OrderFeed_number')]")
    ALL_ORDER_AMOUNT = (By.XPATH, "//div[2]/p[contains(@class, 'OrderFeed_number')]")
    ORDER_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")
    CLOSE_MODAL_BTN =  (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]/div/button[contains(@class, 'modal__close')]")
    ORDERS_LIST = (By.XPATH, ".//p[@class='text text_type_digits-default']")
    ALL_ORDER_ARE_DONE_TEXT = (By.XPATH, "//li[contains(text(),'Все текущие заказы готовы!')]")