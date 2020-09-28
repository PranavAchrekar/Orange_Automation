from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class HomePage(BasePage):
    """Create Locators"""

    HEADER = (By.XPATH, "//h1[text() = 'Dashboard']")
    ACCOUNT_NAME = (By.CSS_SELECTOR, "a.activated-welcome")
    HELP_ICON = (By.CSS_SELECTOR, "a.help-icon-div")

    ADMIN = (By.XPATH, "//b[text()='Admin']")
    USER_MGMT = (By.XPATH, "//a[text()='User Management']")
    USERS_ELE = (By.XPATH, "//a[text()='Users']")

    """Create Constructor"""

    def __init__(self, driver):
        super().__init__(driver)

    """Page Actions"""

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_help_icon_exist(self):
        return self.is_visible(self.HELP_ICON)

    def get_header_value(self):
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)

    def get_account_name_value(self):
        if self.is_visible(self.ACCOUNT_NAME):
            return self.get_element_text(self.ACCOUNT_NAME)

    def do_hover(self):
        self.hover_to(self.ADMIN).hover_to(self.USER_MGMT).hover_to(self.USERS_ELE).click()





