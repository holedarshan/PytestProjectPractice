from pages.soucedemo_login_page import LoginPage

def test_login_valid_user(driver):
    """Test valid login"""
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

def test_login_invalid_user(driver):
    """Test login with invalid credentials"""
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login("wronguser", "wrongpass")
    assert "Username and password do not match any user" in login_page.get_error_message()
