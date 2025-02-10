# import pytest
# from utils.driver_factory import DriverFactory
#
# @pytest.fixture(scope="class")
# def setup(request):
#     # Fetch browser type from CLI arguments or use default (Chrome)
#     browser = request.config.getoption("--browser")
#
#     driver = DriverFactory.get_driver(browser)
#     request.cls.driver = driver  # Assign driver to test class
#     yield driver
#     driver.quit()  # Cleanup after tests
#
# def pytest_addoption(parser):
#     """Allows command-line options like --browser"""
#     parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests (chrome/firefox)")


import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture(scope="function")
def driver():
    """Fixture to initialize and quit WebDriver using WebDriver Manager"""
    # Choose browser: "chrome" or "firefox"
    browser = "chrome"  # Change to "firefox" if needed

    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver  # Provide the driver instance to the test

    driver.quit()  # Close browser after test

