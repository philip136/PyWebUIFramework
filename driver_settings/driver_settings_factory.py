from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from utilities.config_file import ConfigFile
from browser.available_browsers import AvailableBrowsers
from driver_settings.chrome_driver_settings import ChromeDriverSettings
from driver_settings.firefox_driver_settings import FirefoxDriverSettings


class DriverSettingsFactory:
    __settings_file = ConfigFile.read_from_json_file()

    @classmethod
    def get_driver_settings(cls, browser_name):
        browser_profiles = {
            AvailableBrowsers.CHROME.value: (ChromeDriverSettings, ChromeOptions),
            AvailableBrowsers.FIREFOX.value: (FirefoxDriverSettings, FirefoxOptions)
        }
        browser_profile, browser_option = browser_profiles[browser_name]
        return browser_profile(settings_file=cls.__settings_file, options=browser_option)
