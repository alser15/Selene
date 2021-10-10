import allure
from BasePage.BasePage import BasePage
from selene.api import *


class ProfilePage(BasePage):
    def __init__(self, initWebDriver):
        # Доступ к оригиналу driver
        super().__init__(initWebDriver)
        # Поиск поиск Профиля пользователя
        self.avatar = lambda: s(".m-topbar__userpic > div:nth-child(1) > div:nth-child(1)")
        # Поиск Имени пользователя в профие
        self.user_name_in_profile = lambda: s(".m-card-user__name")
        # Поиск Почты в профие
        self.user_email_in_profile = lambda: s(".m-card-user__email")



    @allure.step('Нажать на профиль пользователя')
    def click_on_avatar(self):
        """ Нажать на профиль пользователя """
        self.avatar().click()
        return self

    @allure.step('Проверить Имя пользователя в профиле')
    def check_name_user(self, name):
        """ Проверить Имя пользователя в профиле """
        self.user_name_in_profile().should(have.text(name))
        return self

    @allure.step('Проверить Почту пользователя в профиле')
    def check_mail_user(self, mail):
        """ Проверить Почту пользователя в профиле """
        assert self.user_email_in_profile().should(have.text(mail))
        return self