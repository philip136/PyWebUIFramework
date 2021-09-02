import typing as ty

from selenium.webdriver import Chrome, Firefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from browser.browser_factory import BrowserFactory

WD = ty.TypeVar('WD', bound=RemoteWebDriver)


class LocalBrowserFactory(BrowserFactory):
    __driver: ty.Optional[WD] = None

    def get_driver(self):
        browser_name = self._browser_profile.get_browser_name()
        driver_settings = self._browser_profile.get_driver_settings()
        capabilities = driver_settings.get_capabilities()
        if browser_name == 'chrome':
            executable_path = ChromeDriverManager().install()
            self.__driver = Chrome(executable_path=executable_path, options=capabilities)

        elif browser_name.lower() == 'firefox':
            executable_path = GeckoDriverManager().install()
            self.__driver = Firefox(executable_path=executable_path, options=capabilities)

        return self.__driver
