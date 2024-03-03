from typing import Optional

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from utils.logger_formatter import LOGGER


def generate_explicit_wait(
    driver: WebDriver,
    default_explicit_wait: WebDriverWait[WebDriver | WebElement],
    explicit_wait: Optional[int] = None,
) -> WebDriverWait[WebDriver | WebElement]:
    LOGGER.info('Explicit wait', extra={'explicit_wait': explicit_wait})
    wait: WebDriverWait[WebDriver | WebElement] = default_explicit_wait
    if explicit_wait is not None:
        wait = WebDriverWait(driver, explicit_wait)
    return wait
