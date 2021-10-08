import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, initWebDriver):
        # Передача драйвера через фиксутур initWebDriver
        self.driver = initWebDriver
        # Текуший урл
        self.url = lambda: self.driver.current_url
        # Сетап времени для драйвера
        self.wait = WebDriverWait(self.driver, 20)

    @allure.step('Проверяем текущий урл')
    def check_url(self, url):
        """ Проверяем текущий урл """
        assert self.url() == url, 'url не соответствует ожиданию'

    @allure.step('Проверка отсутствия отсутствия элемента')
    def check_element_false(self, element_false):
        """ Проверка отсутствия отсутствия элемента """
        try:
            element_false()
        except NoSuchElementException:
            return True

    @allure.step('Проверка существования элемента в ДОМ')
    def check_element_true(self, element_true):
        """ Проверка существования элемента """
        return element_true()
