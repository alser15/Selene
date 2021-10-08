from BasePage.LoginPage import LoginPage
import allure
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Tools.Tools import Tools
import os
import requests
import logging
logging.basicConfig(level="DEBUG")
logger = logging.getLogger()

@pytest.fixture(scope='function')
def initWebDriver():
    """ Инициализация драйвера """
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(Tools().url)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def auth(initWebDriver):
    """ Инициализация входа на ресурс, в раздел графики """
    login = LoginPage(initWebDriver)
    driver = initWebDriver
    login.add_login(Tools().login)
    login.add_password(Tools().password)
    login.click_button()
    element_to_hover_over = driver.find_element_by_xpath("//i[@class='m-menu__link-icon flaticon-calendar-2']")
    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    hover.perform()
    driver.find_element_by_xpath("//span[text()='Графики работы']").click()
    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.ID, "schedule-overlay")))
    yield initWebDriver


@allure.step('быстрая авторизация через АПИ')
@pytest.fixture(scope='function')
def test_log(initWebDriver):
    driver = initWebDriver
    session = requests.Session()
    driver.get("https://tt-develop.quality-lab.ru/login")
    get_cookies = driver.get_cookies()
    [session.cookies.set(cookie["name"], cookie['value']) for cookie in get_cookies]
    data = {
        "_csrf_token": "",
        "_username": "Авто Пользователь",
        "_password": "12345678",
        "_submit": "Войти"
    }
    session.post('https://tt-develop.quality-lab.ru/login_check', data=data)
    get_new_cookies = session.cookies.get_dict()
    set_new_cookies = [{"name": name, "value": value} for name, value in get_new_cookies.items()]
    session.close()
    [driver.add_cookie(cookie) for cookie in set_new_cookies]
    driver.get("https://tt-develop.quality-lab.ru/report/group")
    element_to_hover_over = driver.find_element_by_xpath("//i[@class='m-menu__link-icon flaticon-calendar-2']")
    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    hover.perform()
    driver.find_element_by_xpath("//span[text()='Графики работы']").click()
    WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.ID, "schedule-overlay")))
    yield initWebDriver



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """ Скрин при падении теста """
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'initWebDriver' in item.fixturenames:
                    driver = item.funcargs['initWebDriver']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                driver.get_screenshot_as_png(),
                name='error',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))


