from selenium.webdriver.chrome.options import Options
from configuration.driver_settings.base_driver_settings import BaseDriverSettings


class ChromeSettings(BaseDriverSettings):
    def _set_preferences(self, options: Options):
        """Set preference for Chrome.
        :param options: Instance of Options.
        """
        options.add_experimental_option('prefs', self.browser_options)

    @property
    def download_dir_capability_key(self) -> str:
        """Get dir capability key.
        :return: Dir capability key.
        :rtype: str.
        """
        return 'download.default_directory'
