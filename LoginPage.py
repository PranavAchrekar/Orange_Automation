
from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage

"""Note: we have imported BasePage and TestData from Pages and Config packages"""


class LoginPage(BasePage):
    """ By Locators """
    USERNAME = (By.ID, 'txtUsername')
    PASSWORD = (By.ID, 'txtPassword')
    LOGIN_BUTTON = (By.ID, 'btnLogin')
    FORGOT_PASSWORD = (By.LINK_TEXT, 'Forgot your password?')

    """ Constructor of the page class"""

    def __init__(self, driver):
        # use super keyword to call the parent class (BasePage)
        super().__init__(driver)
        self.driver.maximize_window()
        self.driver.get(TestData.BASE_URL)

    """ Page Actions for Login Page """

    """ This is used to get page title """

    def get_login_page_title(self, title):
        return self.get_title()

    """ This is used to check Forgot Password link"""

    def is_forgot_password_exist(self):
        return self.is_visible(self.FORGOT_PASSWORD)

    """ This is used to login the website """

    def do_login(self, username, password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        """ Page chaining concept"""
        """ This do_click method should return object of nxt landing page so we should write homepg class obj
            because we have written constructor in HomePage also
        """
        return HomePage(self.driver)





