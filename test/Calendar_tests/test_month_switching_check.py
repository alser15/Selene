from BasePage.CalendarPage import CalendarPage


def test_month_switching_check(auth):
    test_two = CalendarPage(auth)
    test_two.click_month()
    test_two.select_next_month()
    test_two.try_on()
    test_two.check_month_and_year_today('Ноябрь 2021')
    test_two.check_url('https://tt-develop.quality-lab.ru/calendar/')
    test_two.check_work_day_green_color()
    test_two.check_day_of()
