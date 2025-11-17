from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.waits import safe_find


class WikipediaPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "searchInput")
        self.wait = WebDriverWait(self.driver, 10)

    def search(self, term: str):
        # Use safe_find instead of direct find_element
        box = safe_find(self.driver, self.search_box)

        if box is None:
            # Optional: fail fast with a clearer error instead of cryptic Selenium traceback
            raise AssertionError("Search box not found on Wikipedia page")

        box.clear()
        box.send_keys(term)
        box.send_keys(Keys.RETURN)

        # Wait until the page title reflects the search term or the article heading appears
        try:
            # Prefer title contains (faster)
            self.wait.until(EC.title_contains(term))
        except Exception:
            # Fallback: wait for the article heading if title doesn't update
            self.wait.until(EC.presence_of_element_located((By.ID, "firstHeading")))
        