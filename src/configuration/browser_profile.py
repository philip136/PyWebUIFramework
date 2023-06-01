from injector import inject

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.ie.options import Options as IExplorerOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from src.browser.browser_name import BrowserName
from src.configuration.driver_settings.base_driver_settings import BaseDriverSettings
from src.configuration.driver_settings.chrome_settings import ChromeSettings
from src.configuration.driver_settings.firefox_settings import FirefoxSettings
from src.configuration.driver_settings.iexplorer_settings import IExplorerSettings
from src.configuration.driver_settings.edge_settings import EdgeSettings
from src.core.configurations.interfaces.browser_profile_interface import IBrowserProfile
from src.core.utilities.interfaces.settings_file_interface import ISettingsFile
from src.core.localization.loggers.interfaces.localized_logger_interface import ILocalizedLogger


class BrowserProfile(IBrowserProfile):
    """Class responsible for basic browser settings."""

    @inject
    def __init__(self, settings_file: ISettingsFile, localization_logger: ILocalizedLogger) -> None:
        """Provides a SettingsFile to select the required configuration settings.
        Provides a LocalizedLogger for selecting the required messages in the logs."""
        self._settings_file = settings_file
        self._localization_logger = localization_logger

    def get_driver_settings(self) -> BaseDriverSettings:
        """Get DriverSettings instance (ChromeSettings, FirefoxSettings and etc).
        :return: DriverSettings instance.
        :rtype: BaseDriverSettings.
        """
        browser_name = self.browser_name
        if browser_name == BrowserName.CHROME.value.lower():
            options = ChromeOptions()
            self._driver_settings = ChromeSettings(options=options, settings_file=self.settings_file)

        elif browser_name.lower() == BrowserName.FIREFOX.value.lower():
            options = FirefoxOptions()
            self._driver_settings = FirefoxSettings(options=options, settings_file=self.settings_file)

        elif browser_name.lower() == BrowserName.INTERNET_EXPLORER.value.lower():
            options = IExplorerOptions()
            self._driver_settings = IExplorerSettings(options=options, settings_file=self.settings_file)

        elif browser_name.lower() == BrowserName.EDGE.value.lower():
            options = EdgeOptions()
            self._driver_settings = EdgeSettings(options=options, settings_file=self.settings_file)

        else:
            raise ValueError('There are no assigned behaviour for retrieving driver driver settings for browser %s'
                             % browser_name)

        return self._driver_settings
