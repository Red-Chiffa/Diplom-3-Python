from selenium.webdriver.common.by import By


class MainFunctionLocators:

    CONSTRUCTOR_BTN = (By.XPATH, "//p[contains(text(),'Конструктор')]")  # Кнопка конструктор в хэдере
    ORDER_FEED = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    ORDER_FEED_LIST = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")
    MODAL_WINDOW = (By.XPATH, "//h2[contains(text(),'Детали ингредиента')]")
    CLOSE_BTN = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]/div/button[contains(@class, 'modal__close')]")
    BUN_FLUOR = (By.XPATH, "//a[contains(@href,'61c0c5a71d1f82001bdaaa6d')]")
    BUN_BUTTON = (By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']")  # кнопка "Флюоресцентная булка"
    BASKET = (By.XPATH, "//span[contains(@class, 'BurgerConstructor_basket__list')]")
    BASKET_AREA = (By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket__list')]")
    BUN_FLUOR_COUNTER = (By.XPATH, "//a[contains(@href,'61c0c5a71d1f82001bdaaa6d')]/div[contains(@class, 'counter_counter')]/p")
    BUN_KRATOR = (By.XPATH, "//a[contains(@href,'61c0c5a71d1f82001bdaaa6c')]")
    CREATE_ORDER_BTN = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    ORDER_ID = (By.XPATH,  "//p[contains(text(),'идентификатор заказа')]")
    SAUCE_SPICY = (By.XPATH, "//a[contains(@href,'61c0c5a71d1f82001bdaaa72')]")
    SAUCE_SPACE = (By.XPATH, "//a[contains(@href,'61c0c5a71d1f82001bdaaa73')]")  # Соус фирменный Space Sauce
    SAUCE_TRADITIONAL = (By.XPATH, "//a[contains(@href,'61c0c5a71d1f82001bdaaa74')]")  # Соус традиционный галактический
    SAUCE_THORN = (By.XPATH, "//a[contains(@href,'61c0c5a71d1f82001bdaaa75')]") # Соус с шипами Антарианского плоскоходца


