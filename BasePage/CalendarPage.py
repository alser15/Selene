import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from BasePage.BasePage import BasePage


class CalendarPage(BasePage):
    def __init__(self, initWebDriver):
        # Доступ к оригиналу driver
        super().__init__(initWebDriver)
        # Поиск поля с месяцем и годом
        self.month = lambda: self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='input-group date filter_input_date']/input[@type='text']")))
        # Поиск следующего месяца
        self.next_month = lambda: self.driver.find_element_by_xpath(
            "//td[@colspan='7']/span[contains(@class,'month focused active')]/following-sibling::span[@class='month'][1]")
        # Поиск кнопки Применить
        self.setting_button = lambda: self.driver.find_element_by_xpath(
            "//button[@class='btn btn-brand m-btn m-btn--icon btn_do_filter']")
        # Ожидание загрузки рабочих дней в календаре
        self.element_in_table = lambda: self.wait.until(EC.presence_of_element_located((By.XPATH,
            "//td[@class='fc-event-container']/a[@class='fc-day-grid-event fc-h-event fc-event fc-start fc-end schedule-badge schedule-badge--block schedule-badge--default schedule-badge--']")))
        # Поиск поля с Сотрудниками
        self.input_user = lambda: self.driver.find_element_by_xpath(
            "//span[@class='select2-selection select2-selection--single']")
        # Поиск поля для ввода имени нового сотрудника
        self.name_new_user = lambda: self.wait.until(EC.element_to_be_clickable((By.XPATH,
            "//span[@class='select2-search select2-search--dropdown']/input[@class='select2-search__field']")))
        # Поиск нового сотрудника в списке
        self.secect_new_user = lambda: self.wait.until(EC.element_to_be_clickable((By.XPATH,
            "//span[@class='select2-results']/ul[@class='select2-results__options']/li[contains(text(),'{}')]".format(self.person_new_name))))
        # Поиск рабочих дней
        self.work_day = lambda: self.driver.find_element_by_xpath(
            "//a[@lass='fc-day-grid-event fc-h-event fc-event fc-start fc-end schedule-badge schedule-badge--block schedule-badge--default schedule-badge--']")
        # Поиск выходных дней
        self.off_day = lambda: self.driver.find_elements_by_xpath(
            "//a[@class='fc-day-grid-event fc-h-event fc-event fc-start fc-end schedule-badge schedule-badge--block schedule-badge--no-event schedule-badge--']")

    @allure.step('Проверка текущей даты')
    def check_month_and_year_today(self, year):
        """ Проверка текущей даты """
        assert year == self.month().get_attribute('value')

    @allure.step('Проверка есть ли рабочий день в текущем месяце')
    def check_work_day_green_color(self):
        """ Проверка есть ли рабочий день в текущем месяце """
        try:
            self.work_day()
        except NoSuchElementException:
            return True

    @allure.step('Проверка выходной день в текущем месяц')
    def check_day_of(self):
        """ Проверка выходной день в текущем месяце """
        try:
            self.off_day()
        except NoSuchElementException:
            return True

    @allure.step('Клик на поле с месяцем и годом')
    def click_month(self):
        """ Клик на поле с месяцем и годом """
        self.month().click()

    @allure.step('Ставим следующий месяц')
    def select_next_month(self):
        """ Ставим следующий месяц """
        self.next_month().click()

    @allure.step('Применяем новые настройки')
    def try_on(self):
        """ Применяем новые настройки """
        self.setting_button().click()

    @allure.step('Ожидаем загрузку дня в текущем месяце')
    def wait_table(self):
        """ Ожидаем загрузку дня в текущем месяце"""
        self.element_in_table()

    @allure.step('Клик на поле с сотрудником')
    def click_input_user(self):
        """ Клик на поле с сотрудником """
        self.input_user().click()

    @allure.step('Вводим имя нового сотрудника')
    def enter_name_new_user(self, person):
        """ Вводим имя нового сотрудника """
        self.person_new_name = person
        self.name_new_user().send_keys(person)

    @allure.step('Кликаем на нового сотрудника в списке')
    def ckick_new_user(self):
        """ Кликаем на нового сотрудника в списке """
        self.secect_new_user().click()
