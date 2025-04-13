import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_metadata.plugin import metadata_key


# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome() #driver instance is created
#     return driver

import undetected_chromedriver as uc

#
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome",
#                      help="Specify the browser: chrome or firefox or edge")


# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")


@pytest.fixture()
def setup():
    # global driver
    # if browser == "chrome":
    #     driver = webdriver.Chrome()
    # elif browser == "firefox":
    #     driver = webdriver.Firefox()
    # elif browser == "edge":
    #     driver = webdriver.Edge()
    # else:
    #     raise ValueError("Unsupported Browser")

    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--headless")  # Optional
    driver = uc.Chrome(version_main=134, options=options)
    yield driver
    driver.quit()
    time.sleep(5)

####for pytest html reports ####
#hook for adding environment info in html report
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Ecommerce Project, nopcommerce'
    config.stash[metadata_key]['Test Module Name'] = 'Admin Login Tests'
    config.stash[metadata_key]['Tester Name'] = 'Ujjwal'
#hook for delete/modify environment info in html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME',None)
    metadata.pop('Plugins',None)