import typing as ty

from selenium.webdriver import Chrome, Firefox, Ie, Edge
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from src.browser.browser_name import BrowserName
from src.browser.base_browser_factory import BaseBrowserFactory

WD = ty.TypeVar('WD', bound=RemoteWebDriver)


class LocalBaseBrowserFactory(BaseBrowserFactory):
    """Class that implements the BaseBrowserFactory interface."""

    __driver: ty.Optional[WD] = None

    def get_driver(self) -> WD:
        """Selecting the required driver (Firefox, Chrome and etc).
        :return: WebDriver.
        :rtype: WD.
        """
        browser_name = self._browser_profile.browser_name
        driver_settings = self._browser_profile.get_driver_settings()
        driver_version = self._browser_profile.get_driver_settings().web_driver_version
        capabilities = driver_settings.get_capabilities()
        if browser_name == BrowserName.CHROME.value.lower():
            executable_path = ChromeDriverManager(version=driver_version).install()
            self.__driver = Chrome(executable_path=executable_path, options=capabilities)

        elif browser_name.lower() == BrowserName.FIREFOX.value.lower():
            executable_path = GeckoDriverManager(version=driver_version).install()
            self.__driver = Firefox(executable_path=executable_path, options=capabilities)

        elif browser_name.lower() == BrowserName.INTERNET_EXPLORER.value.lower():
            executable_path = IEDriverManager(version=driver_version).install()
            self.__driver = Ie(executable_path=executable_path)

        elif browser_name.lower() == BrowserName.EDGE.value.lower():
            executable_path = EdgeChromiumDriverManager(version=driver_version).install()
            self.__driver = Edge(executable_path)

        return self.__driver
