from BasePage.CalendarPage import CalendarPage


def test_check_another_schedule(test_log):
    test_three = CalendarPage(test_log)
    test_three.click_input_user()
    test_three.enter_name_new_user('Агафонова Инна')
    test_three.ckick_new_user()
    test_three.try_on()
    test_three.wait_table()
    test_three.check_work_day_green_color()
    test_three.check_day_of()
