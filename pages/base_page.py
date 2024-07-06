import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('клик по элементу')
    def click_element(self, element):
        self.driver.find_element(*element).click()

    @allure.step('Ожидание элемента')
    def wait_and_find_element_located(self, locator):
        WebDriverWait(self.driver, 6).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('ожидание URL')
    def timeout_url(self, url):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(url))

    @allure.step('ожидание отображения элемента')
    def timeout(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('ожидание кликабельности элемента')
    def timeout_clickable(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('ожидание отсутствия элемента')
    def invisibility_of_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located(locator))

    @allure.step('получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('заполнение инпутa')
    def fill_input(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('получение текста элемента')
    def get_element_text(self, locator):
        result = self.driver.find_element(*locator).text
        return result

    @allure.step('Проверка отоборажения элемента')
    def check_element_is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Получение атрибута локатора')
    def get_element_attribute(self, locator, attribute):
        return self.driver.find_element(*locator).get_attribute(attribute)

    @allure.step('Переход на заданную страницу')
    def get_new_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        self.driver.find_element(*locator)

    @allure.step('Перетаскивание ингредиента в корзину')
    def drag_and_drop(self, source, target):
        drag_and_drop(self.driver, source, target)
