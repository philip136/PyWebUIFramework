from abc import ABC, abstractmethod
from injector import inject

from browser.browser import Browser
from configuration.browser_profile import BrowserProfile
from core.configurations.base_timeout_configuration import BaseTimeoutConfiguration
from core.localization.loggers.base_localized_logger import BaseLocalizedLogger


class BrowserFactory(ABC):
    @inject
    def __init__(self, browser_profile: BrowserProfile, logger: BaseLocalizedLogger,
                 timeouts: BaseTimeoutConfiguration):
        self._browser_profile = browser_profile
        self._logger = logger
        self._timeouts = timeouts

    @abstractmethod
    def get_driver(self):
        pass

    def get_browser(self):
        return Browser(web_driver=self.get_driver(), logger=self._logger, browser_profile=self._browser_profile,
                       timeouts=self._timeouts)
