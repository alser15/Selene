import allure
from selenium.common.exceptions import NoSuchElementException
from selene.api import *

class BasePage:
    def __init__(self, initWebDriver):
        # Передача драйвера через фиксутур initWebDriver
        self.browser = initWebDriver


    @allure.step('Проверяем текущий урл')
    def check_url(self, url):
        """ Проверяем текущий урл """
        self.url = lambda: browser.should(be.conditions.url)

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
