import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_open_google(self):
        self.driver.get("https://www.google.com")
        assert "Google" in self.driver.title

    def test_open_github(self):
        self.driver.get("https://github.com")
        assert "GitHub" in self.driver.title
