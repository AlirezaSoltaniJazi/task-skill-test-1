from typing import Final, Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from utils import generate_element_by_locating_visibility, generate_explicit_wait


class ProductDetailsPage:
    _ADD_FIRST_ITEM_TO_CART: Final[tuple] = (By.ID, 'add-to-cart-sauce-labs-backpack')
    _BACK_TO_PRODUCTS: Final[tuple] = (By.ID, 'back-to-products')

    def __init__(self, driver: WebDriver, explicit_time: int = 10):
        self._driver = driver
        self._explicit_wait = WebDriverWait(driver, explicit_time)

    def add_product_to_cart(self, explicit_wait: Optional[int] = None) -> None:
        wait = generate_explicit_wait(self._driver, self._explicit_wait, explicit_wait)
        element = generate_element_by_locating_visibility(
            wait, self._ADD_FIRST_ITEM_TO_CART
        )
        element.click()

    def return_to_products(self, explicit_wait: Optional[int] = None) -> None:
        wait = generate_explicit_wait(self._driver, self._explicit_wait, explicit_wait)
        element = generate_element_by_locating_visibility(wait, self._BACK_TO_PRODUCTS)
        element.click()
