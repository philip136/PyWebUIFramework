from selenium.webdriver.chrome.options import Options
from configuration.driver_settings.base_driver_settings import BaseDriverSettings


class ChromeSettings(BaseDriverSettings):
    def get_capabilities(self) -> Options:
        """Set and get options for driver.
        :return: Driver options.
        :rtype: Options.
        """
        self._set_preferences(options=self._options)
        self._set_arguments(options=self._options)
        return super(ChromeSettings, self).get_capabilities()

    def _set_preferences(self, options: Options) -> None:
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
