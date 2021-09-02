from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from configuration.driver_settings.chrome_settings import ChromeSettings
from configuration.driver_settings.firefox_settings import FirefoxSettings
from core.configurations.base_browser_profile import BaseBrowserProfile


class BrowserProfile(BaseBrowserProfile):
    __driver_settings = None

    def get_driver_settings(self):
        browser_name = self.get_browser_name()
        if browser_name == 'chrome':
            options = ChromeOptions()
            self.__driver_settings = ChromeSettings(options=options, settings_file=self.settings_file)

        elif browser_name.lower() == 'firefox':
            options = FirefoxOptions()
            self.__driver_settings = FirefoxSettings(options=options, settings_file=self.settings_file)

        return self.__driver_settings
