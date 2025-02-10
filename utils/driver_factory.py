from selenium import webdriver

class DriverFactory:
    @staticmethod
    def get_driver(browser="chrome"):
        if browser.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            driver = webdriver.Chrome(options=options)
        elif browser.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--start-maximized")
            driver = webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        driver.implicitly_wait(10)  # Set default implicit wait
        return driver
