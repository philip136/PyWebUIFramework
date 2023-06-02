import typing as ty

from selenium.webdriver import Chrome, Firefox, Ie, Edge

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from browser.browser_name import BrowserName
from browser.base_browser_factory import BaseBrowserFactory

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
            service = ChromeService(executable_path)
            self.__driver = Chrome(service=service, options=capabilities)

        elif browser_name.lower() == BrowserName.FIREFOX.value.lower():
            executable_path = GeckoDriverManager(version=driver_version).install()
            service = FirefoxService(executable_path=executable_path)
            self.__driver = Firefox(service=service, options=capabilities)

        elif browser_name.lower() == BrowserName.INTERNET_EXPLORER.value.lower():
            executable_path = IEDriverManager(version=driver_version).install()
            service = IEService(executable_path=executable_path)
            self.__driver = Ie(service=service)

        elif browser_name.lower() == BrowserName.EDGE.value.lower():
            executable_path = EdgeChromiumDriverManager(version=driver_version).install()
            service = EdgeService(executable_path=executable_path)
            self.__driver = Edge(service=service)

        return self.__driver
