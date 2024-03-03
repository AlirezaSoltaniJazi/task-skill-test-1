from typing import Final, Optional

from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from utils import generate_explicit_wait, generate_element_by_locating_visibility


class CartPage:
    _CART_ITEMS: Final[tuple] = (By.XPATH, '//div[contains(@class,"cart_item_label")]')
    _BUTTON_CHECKOUT: Final[tuple] = (By.ID, 'checkout')

    def __init__(self, driver: WebDriver, explicit_time: int = 10):
        self._driver = driver
        self._explicit_wait = WebDriverWait(driver, explicit_time)

    def verify_items_count(
        self, items_count: int, explicit_wait: Optional[int] = None
    ) -> None:
        wait = generate_explicit_wait(self._driver, self._explicit_wait, explicit_wait)
        element = generate_element_by_locating_visibility(wait, self._CART_ITEMS)
        cart_items = element.find_elements()
        assert_that(len(cart_items)).is_equal_to(items_count)

    def open_checkout(self, explicit_wait: Optional[int] = None) -> None:
        wait = generate_explicit_wait(self._driver, self._explicit_wait, explicit_wait)
        element = generate_element_by_locating_visibility(wait, self._BUTTON_CHECKOUT)
        element.click()
