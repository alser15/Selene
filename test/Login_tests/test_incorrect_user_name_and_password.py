from BasePage.LoginPage import LoginPage


def test_incorrect_user_name_and_password(initWebDriver):
    test_two = LoginPage(initWebDriver)
    test_two.add_login('TestUser')
    test_two.add_password('Password')
    test_two.check_element_false(test_two.error_element_text)
    test_two.click_button()
    test_two.check_url("https://tt-develop.quality-lab.ru/login")
    test_two.check_element_true(test_two.error_element_text)
