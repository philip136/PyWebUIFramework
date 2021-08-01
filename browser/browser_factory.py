from selenium.webdriver import Chrome, Firefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from browser.available_browsers import AvailableBrowsers
from browser.browser_profile import BrowserProfile
from browser.browser import Browser


class BrowserFactory:
    """Class to get browser."""

    __driver_settings = BrowserProfile.get_driver_settings()

    @classmethod
    def get_browser_instance(cls, browser_name):
        """Get browser instance.

        :param browser_name: Browser name.

        :return: Browser instance.
        :rtype: Browser

        """
        available_browsers = {
            AvailableBrowsers.CHROME.value: (Chrome, ChromeDriverManager),
            AvailableBrowsers.FIREFOX.value: (Firefox, GeckoDriverManager)
        }
        web_driver, web_driver_manager = available_browsers[browser_name.upper()]
        return Browser(web_driver=web_driver, web_driver_manager=web_driver_manager)
