from BasePage.CalendarPage import CalendarPage


def test_check_current_month(auth):
    test_one = CalendarPage(auth)
    test_one.check_url("https://tt-develop.quality-lab.ru/calendar/")
    test_one.check_month_and_year_today('Октябрь 2021')
    test_one.check_work_day_green_color()
    test_one.check_day_of() 