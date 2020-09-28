from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""" This class is the parent class of all the pages """
""" It contains all the generic methods and utilities for all the pages """


class BasePage:
    """ This function is called everytime a new object of the base class is created """

    def __init__(self, driver):
        self.driver = driver

    """ This function is performs click on web element whose locator is passed to it"""

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).click()

    """ This function performs text entry of the passed in text, in a web element whose locator is passed to it."""

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    """ This function returns the web element's text with passed in text """

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        return element.text

    """ This function checks if the web element whose locator has been passed to it, is visible or not and returns"""

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    """ This function checks if the web element whose locator has been passed to it, is enabled or not and returns"""

    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))

    """ This function returns the title of page """

    def get_title(self, title):
        WebDriverWait(self.driver, 15).until(EC.title_is(title))
        return self.driver.title

    """ This function moves the mouse pointer over a web element whose locator has been passed to it."""

    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()
