from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

DEFAULT_TIMEOUT = 20
DEFAULT_RETRIES = 2


def safe_find(driver, locator, timeout: int = DEFAULT_TIMEOUT):
    """
    Wait up to `timeout` seconds for element located by `locator`.
    Returns WebElement or None.
    """
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    except TimeoutException:
        return None


def safe_visible(driver, locator, timeout: int = DEFAULT_TIMEOUT):
    """
    Wait up to `timeout` seconds for element located by `locator` to be visible.
    Returns WebElement or None.
    """
    try:
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    except TimeoutException:
        return None


def click_with_retry(
    driver,
    locator,
    timeout: int = DEFAULT_TIMEOUT,
    retries: int = DEFAULT_RETRIES,
) -> bool:
    """
    Try to click an element a few times to avoid flakiness.
    Returns True on success, raises last TimeoutException on failure.
    """
    last_error: TimeoutException | None = None

    for _ in range(retries + 1):
        try:
            elem = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            elem.click()
            return True
        except TimeoutException as e:
            last_error = e

    if last_error:
        raise last_error

    return False


