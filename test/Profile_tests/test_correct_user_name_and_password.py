import os
from BasePage.ProfilePage import ProfilePage
from BasePage.LoginPage import LoginPage
from Tools.Tools import Tools
import pytest


@pytest.mark.parametrize("name,password",
                         [(Tools().login, Tools().password), ('test_parametrixe', 'test_password')])
def test_correct_user_name_and_password(initWebDriver, name, password):
    test_one = LoginPage(initWebDriver)
    test_one.add_login(name)\
        .add_password(password)\
        .click_button_submit()\
        .check_url(os.environ['current_url'])\
        .click_on_avatar()\
        .check_name_user(Tools().login)\
        .check_mail_user('dawdawd@m.r')
