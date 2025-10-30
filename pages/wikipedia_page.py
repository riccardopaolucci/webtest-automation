from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class WikipediaPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "searchInput")
        
    def search(self, term):
        box = self.driver.find_element(*self.search_box)
        box.clear()
        box.send_keys(term)
        box.send_keys(Keys.RETURN)
        