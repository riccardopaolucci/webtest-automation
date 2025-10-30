from pages.login_page import LoginPage
import pytest

@pytest.mark.parametrize("username,password", [
    ("wrongUser", "wrongPass"),
    ("", ""),
    ("admin", "incorrectPassword")
])
def test_invalid_login(driver, username, password):
    driver.get("https://the-internet.herokuapp.com/login")
    page = LoginPage(driver)
    page.login(username, password)
    msg = page.get_message().lower()
    assert "invalid" in msg or "unsuccessful" in msg