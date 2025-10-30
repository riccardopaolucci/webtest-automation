from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.login_btn = (By.CSS_SELECTOR, "button[type='submit']")
        self.flash = (By.ID, "flash")
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_btn).click()

    def get_message(self):
        # wait for the flash message to appear and return its text
        flash_el = self.wait.until(EC.visibility_of_element_located(self.flash))
        return flash_el.text