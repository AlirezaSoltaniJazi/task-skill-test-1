from typing import Final, Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from utils import generate_explicit_wait, generate_element_by_locating_visibility


class ProductsPage:
    _FIRST_ITEM: Final[tuple] = (
        By.CSS_SELECTOR,
        '#item_4_title_link > div',
    )
    _ADD_SECOND_ITEM_TO_CART: Final[tuple] = (
        By.CSS_SELECTOR,
        '#add-to-cart-sauce-labs-bike-light',
    )
    _BUTTON_SHOPPING_CART: Final[tuple] = (By.ID, 'shopping_cart_container')

    def __init__(self, driver: WebDriver, explicit_time: int = 10):
        self._driver = driver
        self._explicit_wait = WebDriverWait(driver, explicit_time)

    def select_first_product(self, explicit_wait: Optional[int] = None) -> None:
        wait = generate_explicit_wait(self._driver, self._explicit_wait, explicit_wait)
        element = generate_element_by_locating_visibility(wait, self._FIRST_ITEM)
        element.click()

    def add_second_item_to_cart(self, explicit_wait: Optional[int] = None) -> None:
        wait = generate_explicit_wait(self._driver, self._explicit_wait, explicit_wait)
        element = generate_element_by_locating_visibility(
            wait, self._ADD_SECOND_ITEM_TO_CART
        )
        element.click()

    def open_cart(self, explicit_wait: Optional[int] = None) -> None:
        wait = generate_explicit_wait(self._driver, self._explicit_wait, explicit_wait)
        element = generate_element_by_locating_visibility(
            wait, self._BUTTON_SHOPPING_CART
        )
        element.click()
