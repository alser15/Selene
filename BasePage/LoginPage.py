import allure
from BasePage.BasePage import BasePage
from BasePage.ProfilePage import ProfilePage


class LoginPage(BasePage):
    def __init__(self, initWebDriver):
        # Доступ к оригиналу driver
        super().__init__(initWebDriver)
        # Поиск поля Имя пользователя
        self.user_name = lambda: self.driver.find_element_by_xpath(
            '//div[@class="form-group m-form__group"]/input[@name="_username"]')
        # Поиск поля Пароль
        self.user_password = lambda: self.driver.find_element_by_xpath(
            '//div[@class="form-group m-form__group"]/input[@id="password"]')
        # Поиск кнопки Войти
        self.button = lambda: self.driver.find_element_by_xpath(
            "//div[@class='m-login__form-action']/input[@value='Войти']")
        # Поиск текста с ошибкой
        self.error_element_text = lambda: self.driver.find_element_by_xpath(
            '//div[contains(text(),"Invalid credentials")]')

    @allure.step('Ввод логина')
    def add_login(self, name):
        """ Ввод логина """
        self.user_name().send_keys(name)
        return self

    @allure.step('Ввод пароля')
    def add_password(self, password):
        """ Ввод пароля """
        self.user_password().send_keys(password)
        return self

    @allure.step('Нажать кнопку Войти')
    def click_button(self):
        """ Нажать кнопку Войти """
        self.button().click()

    @allure.step('Нажать кнопку Войти')
    def click_button_submit(self):
        """ Нажать кнопку Войти """
        self.click_button()
        return ProfilePage(self.driver)

    @allure.step('Проверка поля ввода Имени пользователя')
    def chech_text_in_input_name(self, user_name):
        """ Проверка поля ввода Имени пользователя """
        assert self.user_name().get_attribute('value') == user_name

    @allure.step('Проверка поля ввода Пароля пользователя')
    def chech_text_in_input_password(self):
        """ Проверка поля ввода Пароля пользователя """
        assert self.user_password().get_attribute('value') == ""
