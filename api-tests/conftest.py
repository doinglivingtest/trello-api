import pytest

from config import browser, baseURL
from selenium import webdriver



@pytest.fixture()
def setup(request):
    """
        if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    return driver
    :return:
    """
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    request.instance.driver = driver
    driver.implicitly_wait(10)
    driver.get(baseURL + '/login')
    driver.maximize_window()

    yield driver
    driver.close()



