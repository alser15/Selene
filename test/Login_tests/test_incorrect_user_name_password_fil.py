from BasePage.LoginPage import LoginPage
from Tools.Tools import Tools


def test_incorrect_user_name_password_fil(initWebDriver):
    test_one = LoginPage(initWebDriver)
    test_one.add_login(Tools().login)
    test_one.click_button()
    test_one.chech_text_in_input_name(Tools().login)
    test_one.chech_text_in_input_password()
