from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WikipediaPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "searchInput")
        self.wait = WebDriverWait(self.driver, 10)
        
    def search(self, term):
        box = self.driver.find_element(*self.search_box)
        box.clear()
        box.send_keys(term)
        box.send_keys(Keys.RETURN)
        # wait until the page title reflects the search term or the article heading appears
        try:
            # prefer title contains (faster), but fall back to waiting for the first heading
            self.wait.until(lambda d: term.lower() in d.title.lower())
        except Exception:
            # if title doesn't update (e.g. language landing), wait for the article heading
            self.wait.until(EC.presence_of_element_located((By.ID, "firstHeading")))
        