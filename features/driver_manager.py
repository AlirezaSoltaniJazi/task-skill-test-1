from _pytest.fixtures import FixtureFunction
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.webdriver import WebDriver
from pytest import fixture

from configs import AppConfig, AppServer
from utils import LOGGER


@fixture(scope='session')
def appium_service():
    service = AppiumService()
    service.start(
        args=['--address', AppServer.APPIUM_HOST, '-p', str(AppServer.APPIUM_PORT)],
        timeout_ms=20000,
    )
    yield service
    service.stop()


def create_android_driver(custom_opts=None) -> WebDriver:
    capabilities = AppConfig.CHROME_CONFIG
    options = UiAutomator2Options().load_capabilities(capabilities)
    LOGGER.info(
        'Android driver',
        extra={
            'capabilities': capabilities,
            'options_capabilities': options.capabilities,
            'appium_host': AppServer.APPIUM_HOST,
            'appium_port': AppServer.APPIUM_PORT,
        },
    )
    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    return webdriver.Remote(
        f'http://{AppServer.APPIUM_HOST}:{AppServer.APPIUM_PORT}', options=options
    )


@fixture
def android_driver_factory(
    appium_service: FixtureFunction,  # pylint: disable=W0621,W0613
):
    return create_android_driver
