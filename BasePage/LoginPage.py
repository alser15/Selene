import allure
from BasePage.BasePage import BasePage
from selene.api import *

class LoginPage(BasePage):
    def __init__(self, initWebDriver):
        # Доступ к оригиналу driver
        super().__init__(initWebDriver)
        # Поиск поля Имя пользователя
        self.user_name = lambda: s('//*[@id="username"]')
        # Поиск поля Пароль
        self.user_password = lambda: s('#password')
        # Поиск кнопки Войти
        self.button = lambda: s('#_submit')
        # Поиск текста с ошибкой
        self.error_element_text = lambda: s('.m-login__signin > div:nth-child(1)')

    @allure.step('Ввод логина')
    def add_login(self, name):
        """ Ввод логина """
        self.user_name().set(name)
        return self

    @allure.step('Ввод пароля')
    def add_password(self, password):
        """ Ввод пароля """
        self.user_password().set(password)
        return self

    @allure.step('Нажать кнопку Войти')
    def click_button(self):
        """ Нажать кнопку Войти """
        self.button().click()


    @allure.step('Проверка поля ввода Имени пользователя')
    def chech_text_in_input_name(self, user_name):
        """ Проверка поля ввода Имени пользователя """
        self.user_name().should(be.visible)
        self.user_name().should(have.value(user_name))

    @allure.step('Проверка поля ввода Пароля пользователя')
    def chech_text_in_input_password(self):
        """ Проверка поля ввода Пароля пользователя """
        self.user_password().should(have.text(""))
