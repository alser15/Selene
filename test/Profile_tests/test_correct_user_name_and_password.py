import os
from BasePage.ProfilePage import ProfilePage
from BasePage.LoginPage import LoginPage
from Tools.Tools import Tools
import pytest


@pytest.mark.parametrize("name,password",
                         [(Tools().login, Tools().password), ('test_parametrixe', 'test_password')])
def test_correct_user_name_and_password(initWebDriver, name, password):
    test_one = LoginPage(initWebDriver)
    test_one_one = ProfilePage(initWebDriver)
    test_one.add_login(name)
    test_one.add_password(password)
    test_one.click_button()
    test_one_one.check_url(os.environ['current_url'])
    test_one_one.click_on_avatar()
    test_one_one.check_name_user(Tools().login)
    test_one_one.check_mail_user('dawdawd@m.r')
