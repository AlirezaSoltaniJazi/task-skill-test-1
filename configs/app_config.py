from typing import Final


class AppConfig:
    FIREFOX_CONFIG: Final[dict] = {
        'automationName': 'UiAutomator2',
        'platformName': 'Android',
        'appium:platformVersion': '13.0',
        # 'appPackage': 'org.mozilla.firefox',
        # 'appActivity': 'org.mozilla.firefox.App',
        'browserName': 'Firefox',
        'appium:grantPermissions': True,
        'appium:ensureWebviewsHavePages': True,
        'appium:nativeWebScreenshot': True,
        'appium:newCommandTimeout': 3600,
        'appium:connectHardwareKeyboard': True,
        'resetKeyboard': True,
    }
    CHROME_CONFIG: Final[dict] = {
        'automationName': 'UiAutomator2',
        'platformName': 'Android',
        'appium:platformVersion': '12.0',
        # 'appPackage': 'com.android.chrome',
        # 'appActivity': 'com.google.android.apps.chrome.Main',
        'browserName': 'Chrome',
        'appium:grantPermissions': True,
        'appium:ensureWebviewsHavePages': True,
        'appium:nativeWebScreenshot': True,
        'appium:newCommandTimeout': 3600,
        'appium:connectHardwareKeyboard': True,
        'resetKeyboard': True,
    }


class AppServer:
    APPIUM_PORT = 4727
    APPIUM_HOST = '127.0.0.1'
