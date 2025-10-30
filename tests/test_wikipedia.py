import pytest
from pages.wikipedia_page import WikipediaPage

@pytest.mark.parametrize("term", ["Automation", "Machine Learning", "Artificial Intelligence"])
def test_search_wikipedia(driver, term):
    driver.get("https://www.wikipedia.org/")
    page = WikipediaPage(driver)
    page.search(term)
    assert term.lower() in driver.title.lower()