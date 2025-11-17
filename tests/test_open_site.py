# tests/test_open_site.py

def test_open_wikipedia(driver):
    # use the shared Docker-safe driver from conftest.py
    driver.get("https://www.wikipedia.org/")
    assert "Wikipedia" in driver.title