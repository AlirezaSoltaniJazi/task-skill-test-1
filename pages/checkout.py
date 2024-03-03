from typing import Final, Optional

from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from utils import generate_explicit_wait, generate_element_by_locating_visibility


class CheckoutPage:
    _INPUT_FIELD_FIRST_NAME: Final[tuple] = (By.ID, 'first-name')
    _INPUT_FIELD_LAST_NAME: Final[tuple] = (By.ID, 'last-name')
    _INPUT_FIELD_ZIP: Final[tuple] = (By.ID, 'postal-code')
    _BUTTON_CONTINUE: Final[tuple] = (By.ID, 'continue')
    _LABEL_TOTAL_PRICE: Final[tuple] = (
        By.CSS_SELECTOR,
        '#checkout_summary_container > div > '
        'div.summary_info > div.summary_info_label.summary_total_label',
    )
    _BUTTON_FINISH_PURCHASE: Final[tuple] = (By.ID, 'finish')
    _LABEL_SUCCESSFUL_MESSAGE: Final[tuple] = (By.XPATH, '//div//h2')

    def __init__(self, driver: WebDriver, explicit_time: int = 10):
        self._driver = driver
        self._explicit_wait = WebDriverWait(driver, explicit_time)

    def enter_first_name(
        self, first_name: str, explicit_wait: Optional[int] = None
    ) -> None:
        wait = generate_explicit_wait(self._driver, self._explicit_wait, explicit_wait)
        element = generate_element_by_locating_visibility(
            wait, self._INPUT_FIELD_FIRST_NAME
        )
        element.send_keys(first_name)

    def enter_last_name(
        self, last_name: str, explicit_wait: Optional[int] = None
    ) -> None:
        wait = generate_explicit_wait(self._driver, self._explicit_wait, explicit_wait)
        element = generate_element_by_locating_visibility(
            wait, self._INPUT_FIELD_LAST_NAME
        )
        element.send_keys(last_name)

    def enter_zip(self, zip_code: str, explicit_wait: Optional[int] = None) -> None:
        wait = generate_explicit_wait(self._driver, self._explicit_wait, explicit_wait)
        element = generate_element_by_locating_visibility(wait, self._INPUT_FIELD_ZIP)
        element.send_keys(zip_code)

    def continue_payment(self, explicit_wait: Optional[int] = None) -> None:
        wait = generate_explicit_wait(self._driver, self._explicit_wait, explicit_wait)
        element = generate_element_by_locating_visibility(wait, self._BUTTON_CONTINUE)
        element.click()

    def verify_total_amount(
        self, total_amount: str, explicit_wait: Optional[int] = None
    ) -> None:
        wait = generate_explicit_wait(self._driver, self._explicit_wait, explicit_wait)
        element = generate_element_by_locating_visibility(wait, self._LABEL_TOTAL_PRICE)
        amount = element.text
        assert_that(amount).is_equal_to(total_amount)

    def confirm_purchase(self, explicit_wait: Optional[int] = None) -> None:
        wait = generate_explicit_wait(self._driver, self._explicit_wait, explicit_wait)
        element = generate_element_by_locating_visibility(
            wait, self._BUTTON_FINISH_PURCHASE
        )
        element.click()

    def verify_successful_purchase(
        self, purchase_message: str, explicit_wait: Optional[int] = None
    ) -> None:
        wait = generate_explicit_wait(self._driver, self._explicit_wait, explicit_wait)
        element = generate_element_by_locating_visibility(
            wait, self._BUTTON_FINISH_PURCHASE
        )
        purchase_result = element.text
        assert_that(purchase_result).is_equal_to(purchase_message)
