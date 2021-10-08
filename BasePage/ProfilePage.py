import allure
from BasePage.BasePage import BasePage


class ProfilePage(BasePage):
    def __init__(self, initWebDriver):
        # Доступ к оригиналу driver
        super().__init__(initWebDriver)
        # Поиск поля Имя пользователя
        self.user_name = lambda: self.driver.find_element_by_xpath(
            '//div[@class="form-group m-form__group"]/input[@name="_username"]')
        # Поиск поля Имя пользователя
        self.user_password = lambda: self.driver.find_element_by_xpath(
            '//div[@class="form-group m-form__group"]/input[@id="password"]')
        # Поиск кнопки Войти
        self.button = lambda: self.driver.find_element_by_xpath(
            "//div[@class='m-login__form-action']/input[@value='Войти']")
        # Поиск поиск Профиля пользователя
        self.avatar = lambda: self.driver.find_element_by_xpath("//div[@class='avatarCover']")
        # Поиск Имени пользователя в профие
        self.user_name_in_profile = lambda: self.driver.find_element_by_xpath(
            "//span[@class='m-card-user__name m--font-weight-500']")
        # Поиск Почты в профие
        self.user_email_in_profile = lambda: self.driver.find_element_by_xpath(
            "//span[@class='m-card-user__email m--font-weight-300 m-link']")



    @allure.step('Нажать на профиль пользователя')
    def click_on_avatar(self):
        """ Нажать на профиль пользователя """
        self.avatar().click()
        return self

    @allure.step('Проверить Имя пользователя в профиле')
    def check_name_user(self, name):
        """ Проверить Имя пользователя в профиле """
        assert self.user_name_in_profile().text == name, "Имя пользователя не соответствует ожиданию"
        return self

    @allure.step('Проверить Почту пользователя в профиле')
    def check_mail_user(self, mail):
        """ Проверить Почту пользователя в профиле """
        assert self.user_email_in_profile().text == mail, "Почта пользователя не соответствует ожиданию"
        return self