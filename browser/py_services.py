from browser.browser_factory import BrowserFactory
from utilities.config_file import ConfigFile


class PyServices:
    """Class from which you need to work with WebUIFramework."""

    __settings_file = ConfigFile.read_from_json_file()
    __browser_instance = None

    @classmethod
    def get_browser(cls):
        """Get browser instance.

        :return: Browser instance.
        """
        cls.__browser_instance = BrowserFactory.get_browser_instance(browser_name=cls.__settings_file['browserName'])
        return cls.__browser_instance
