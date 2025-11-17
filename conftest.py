# conftest.py
import os
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1280,800")

    chrome_driver_env = os.getenv("CHROME_DRIVER", "/usr/bin/chromedriver")
    if Path(chrome_driver_env).exists():
        service = Service(chrome_driver_env)
    else:
        # fallback for running locally outside Docker
        service = Service(ChromeDriverManager().install())

    drv = webdriver.Chrome(service=service, options=opts)
    yield drv
    drv.quit()
