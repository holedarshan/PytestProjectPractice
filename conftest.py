import pytest
from utils.driver_factory import DriverFactory

@pytest.fixture(scope="class")
def setup(request):
    # Fetch browser type from CLI arguments or use default (Chrome)
    browser = request.config.getoption("--browser")

    driver = DriverFactory.get_driver(browser)
    request.cls.driver = driver  # Assign driver to test class
    yield driver
    driver.quit()  # Cleanup after tests

def pytest_addoption(parser):
    """Allows command-line options like --browser"""
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests (chrome/firefox)")
