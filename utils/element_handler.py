from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions


def generate_element_by_locating_visibility(wait, locator: tuple) -> WebElement:
    condition = expected_conditions.visibility_of_element_located(*locator)
    element: WebElement = wait.until(condition)
    return element
