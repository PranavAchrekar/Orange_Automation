import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTests

'''
 Note :We have imported BaseTests from test_base.py file from Test package and
       also imported LoginPage from Pages package and TestData from Config package.
'''


class Test_Login(BaseTests):

    def test_forgot_password_visible(self):
        """ Create object of LoginPage class """
        self.loginPage = LoginPage(self.driver)
        """With this reference I will call all the methods which are in LoginPage class"""
        flag = self.loginPage.is_forgot_password_exist()  # store in a boolean lets call it flag
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASS_WORD)




