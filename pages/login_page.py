from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.waits import safe_find, click_with_retry


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.login_btn = (By.CSS_SELECTOR, "button[type='submit']")
        self.flash = (By.ID, "flash")
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, user, pwd):
        user_el = safe_find(self.driver, self.username)
        pwd_el = safe_find(self.driver, self.password)

        if user_el is None or pwd_el is None:
            raise AssertionError("Login inputs not found on the page")

        user_el.clear()
        user_el.send_keys(user)

        pwd_el.clear()
        pwd_el.send_keys(pwd)

        # Use retry logic for stability
        click_with_retry(self.driver, self.login_btn)

    def get_message(self):
        flash_el = self.wait.until(EC.visibility_of_element_located(self.flash))
        return flash_el.text


  