from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Base class for common Selenium operations"""

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        """Click an element"""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        """Enter text into an input field"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        """Get text from an element"""
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text

    def is_element_visible(self, locator):
        """Check if an element is visible"""
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).is_displayed()
