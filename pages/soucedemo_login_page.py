from selenium.webdriver.common.by import By
from pages.soucedemo_base_page import BasePage

class LoginPage(BasePage):
    """Page Object for Login Page"""

    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3")
    # ERROR_MESSAGE = (By.XPATH, "//*[@id="login_button_container"]/div/form/div[3]/h3/button")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        """Perform login action"""
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        """Get login error message"""
        return self.get_text(self.ERROR_MESSAGE)
