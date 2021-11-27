from selenium.webdriver.firefox.options import Options
from configuration.driver_settings.base_driver_settings import BaseDriverSettings


class FirefoxSettings(BaseDriverSettings):
    def get_capabilities(self) -> Options:
        """Set and get options for driver.
        :return: Driver options.
        :rtype: Options.
        """
        self._set_preferences(options=self._options)
        self._set_arguments(options=self._options)
        return super(FirefoxSettings, self).get_capabilities()

    def _set_preferences(self, options: Options) -> None:
        """Set preference for Firefox.
        :param options: Instance of Options.
        """
        for pref_name, pref_value in self.browser_options.items():
            options.set_preference(name=pref_name, value=pref_value)

    @property
    def download_dir_capability_key(self) -> str:
        """Get dir capability key.
        :return: Dir capability key.
        :rtype: str.
        """
        return 'browser.download.dir'
