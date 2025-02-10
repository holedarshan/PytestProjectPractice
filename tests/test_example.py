

def test_open_google(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title

def test_open_github(driver):
    driver.get("https://github.com")
    assert "GitHub" in driver.title
