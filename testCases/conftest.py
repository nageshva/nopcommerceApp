import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):

    if browser =='ie':
        driver = webdriver.Ie()
        print('Launching Edge browser............')
    elif browser == 'firefox':
        driver=webdriver.Firefox()
        print('Launching Firefox browser............')
    else:
        driver=webdriver.Chrome()
        print('Launching Chrome browser............')
    return driver

def pytest_addoption(parser):  # This will get the value  from  CLI/Hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # This will return the browser value to setup method
    return request.config.getoption("--browser")
