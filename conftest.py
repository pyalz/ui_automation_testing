import shutil
import time
import pytest
from pytest_base_url.plugin import base_url
import allure
import os
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import urllib
from datetime import datetime
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import urllib3
import logging
import boto3, pytest


# Get browser name from arguments, use parser as it is
# this allows to access Python parser to add a new optional parameter
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome:  ")
    parser.addoption("--cleanresults", action="store", default="False", help="Clean allure results folder")


# just added request param, from selenium import webdriver and request.cls.driver = driver
# this fixture or function will run before, in this case, the class, as that is the scope
@pytest.fixture(scope="function")
def test_setup(request, variables):
    timeout = variables["timeout"]
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        # only this command is needed to download or look the chromedriver, no need for .exe
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--start-maximized")
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-sandbox')
        driver = webdriver.Chrome("/usr/bin/chromedriver",options=chrome_options)
        driver.implicitly_wait(timeout)
        # driver = webdriver.Chrome(executable_path= "C:/Users/jorge/Desktop/Work/Code/Mine/PythonAutomationFramework/drivers/chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "edge":
        driver = webdriver.Edge(EdgeDriverManager().install())
    elif browser == "remote":
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps)
    elif browser == "aws":
        devicefarm_client = boto3.client("devicefarm", region_name="us-west-2")
        testgrid_url_response = devicefarm_client.create_test_grid_url(
            projectArn="arn:aws:devicefarm:us-west-2:484386781700:testgrid-project:ee01db55-6654-45e8-b364-608ef8c1e64b",
            expiresInSeconds=300)
        driver = webdriver.Remote(testgrid_url_response["url"],
                                                webdriver.DesiredCapabilities.CHROME)

    else:
        #driver = webdriver.Chrome(ChromeDriverManager().install())
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-sandbox')
        driver = webdriver.Chrome("/usr/bin/chromedriver", options=chrome_options)

    driver.implicitly_wait(5)
    driver.maximize_window()
    # next line will sent the driver variable to the class
    request.cls.driver = driver


    yield
    driver.close()
    driver.quit()
    print("Test completed.")

#attach this later on https://pypi.org/project/pytest-allure-adaptor/1.3.6/
#https://i.stack.imgur.com/jsXCH.png
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            if 'request' in item.fixturenames:
                feature_request_driver = item.funcargs['request'].cls.driver
            allure.attach(feature_request_driver.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))


# @pytest.fixture(scope="session",autouse=True)
# def clean_pytest_folder(request):
#     if request.config.getoption("--cleanresults"):
#         for root, dirs, files in os.walk('/home/alister/PycharmProjects/ui_automation_final1/allure-results/'):
#             for f in files:
#                 os.unlink(os.path.join(root, f))
#
#             for d in dirs:
#                 shutil.rmtree(os.path.join(root, d))

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     RESULT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/results/"
#     timestamp = datetime.now().strftime('%H-%M-%S-%f')
#
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#     if report.when == 'call':
#         feature_request = item.funcargs['request']
#         if feature_request.cls is not None :
#             driver = feature_request.cls.driver
#             # always add url to report
#             extra.append(pytest_html.extras.url(driver.current_url))
#             xfail = hasattr(report, 'wasxfail')
#             if (report.skipped and xfail) or (report.failed and not xfail):
#                 # only add additional html on failure
#                 driver.save_screenshot(RESULT_DIR + timestamp + '.png')
#                 extra.append(pytest_html.extras.image(RESULT_DIR +timestamp+'.png'))
#                 extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
#             report.extra = extra



#attach this later on https://pypi.org/project/pytest-allure-adaptor/1.3.6/
#https://i.stack.imgur.com/jsXCH.png
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            if 'request' in item.fixturenames:
                feature_request_driver = item.funcargs['request'].cls.driver
            allure.attach(feature_request_driver.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))