import typing as ty
from abc import ABC, abstractmethod

from src.browser.browser import Browser

WD = ty.TypeVar('WD')


class IBaseBrowserFactory(ABC):
    @abstractmethod
    def get_browser(self) -> Browser:
        """Get browser instance
        :return: Browser instance.
        :rtype: Browser.
        """
        pass
    
    @abstractmethod
    def get_driver(self) -> WD:
        """Abstract method for selecting the required driver (Firefox, Chrome and etc).
        :return: WebDriver.
        :rtype: WD.
        """
        pass
