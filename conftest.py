import pytest
from selenium import webdriver
from Config.config import TestData

web_driver = None


@pytest.fixture(params=['chrome'], scope='class')
def init_driver(request):
    global web_driver
    if request.param == 'chrome':
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    # web_driver.implicitly_wait(5)
    yield
    pass
    # web_driver.close()


"""
Note: executable_path we have imported from config.py file.
"""
