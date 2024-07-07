import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from URLS import *
from locators.personal_account_locators import PersonalAccountLocators
from pages.login_page import LoginPage
from pages.main_function_page import MainFunctionPage


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
    driver.get(BASE_URL)

    yield driver

    driver.quit()


@pytest.fixture
def login(driver):
    login_page = LoginPage(driver)
    login_page.get_new_url(LOGIN_URL)
    login_page.fill_email('am1234@ya.ru')  # имя Александра
    login_page.fill_password('am1234')
    login_page.click_login_btn()
    login_page.timeout_buns()


@pytest.fixture
def create_order(driver, login):
    main_function = MainFunctionPage(driver)
    main_function.timeout_url(BASE_URL)
    main_function.add_ingredient_in_basket()
    main_function.click_create_oreder_btn()