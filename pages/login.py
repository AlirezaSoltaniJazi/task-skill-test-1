from typing import Final, Optional

from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from utils import (
    LOGGER,
    generate_explicit_wait,
    generate_element_by_locating_visibility,
)


class LoginPage:
    _INPUT_FIELD_USERNAME: Final[tuple] = (By.ID, 'user-name')
    _INPUT_FIELD_PASSWORD: Final[tuple] = (By.ID, 'password')
    _BUTTON_LOGIN: Final[tuple] = (By.ID, 'login-button')
    _TITLE_MAIN_PAGE: Final[tuple] = (By.XPATH, '//div[contains(@class,"app_logo")]')

    def __init__(self, driver: WebDriver, explicit_time: int = 10):
        self._driver = driver
        self._explicit_wait = WebDriverWait(driver, explicit_time)

    def open_login_page(self, address: str):
        self._driver.get(address)

    def enter_username(
        self, username: str, explicit_wait: Optional[int] = None
    ) -> None:
        LOGGER.info('Username data', extra={'username': username})
        wait = generate_explicit_wait(self._driver, self._explicit_wait, explicit_wait)
        element = generate_element_by_locating_visibility(
            wait, self._INPUT_FIELD_USERNAME
        )
        element.send_keys(username)

    def enter_password(
        self, password: str, explicit_wait: Optional[int] = None
    ) -> None:
        LOGGER.info('Password data', extra={'password': password})
        wait = generate_explicit_wait(self._driver, self._explicit_wait, explicit_wait)
        element = generate_element_by_locating_visibility(
            wait, self._INPUT_FIELD_PASSWORD
        )
        element.send_keys(password)

    def click_login_button(self, explicit_wait: Optional[int] = None) -> None:
        wait = generate_explicit_wait(self._driver, self._explicit_wait, explicit_wait)
        element = generate_element_by_locating_visibility(wait, self._BUTTON_LOGIN)
        element.click()

    def verify_successful_login(self, explicit_wait: Optional[int] = None) -> None:
        wait = generate_explicit_wait(self._driver, self._explicit_wait, explicit_wait)
        element = generate_element_by_locating_visibility(wait, self._TITLE_MAIN_PAGE)
        login_title = element.text
        assert_that(login_title).is_equal_to('Swag Labs')
