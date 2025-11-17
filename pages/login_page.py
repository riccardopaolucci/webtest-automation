from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.waits import safe_find, safe_visible, click_with_retry


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.login_btn = (By.CSS_SELECTOR, "button[type='submit']")
        self.flash = (By.ID, "flash")
        self.wait = WebDriverWait(self.driver, 20)

    def login(self, user, pwd):
        user_el = safe_find(self.driver, self.username, timeout=20)
        pwd_el = safe_find(self.driver, self.password, timeout=20)

        if user_el is None or pwd_el is None:
            current_url = self.driver.current_url
            raise AssertionError(
                f"Login inputs not found on the page. URL was: {current_url}"
            )

        user_el.clear()
        user_el.send_keys(user)

        pwd_el.clear()
        pwd_el.send_keys(pwd)

        # Use retry logic for stability
        click_with_retry(self.driver, self.login_btn, timeout=20)

    def get_message(self):
        flash_el = safe_visible(self.driver, self.flash, timeout=20)
        if flash_el is None:
            current_url = self.driver.current_url
            raise AssertionError(
                f"Flash message not found after login. URL was: {current_url}"
            )
        return flash_el.text



  