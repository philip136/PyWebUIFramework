from driver_settings.driver_settings import DriverSettings
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class FirefoxDriverSettings(DriverSettings):
    """Driver settings for Firefox."""

    def _set_preferences(self, options: FirefoxOptions) -> None:
        """Setup preferences.
        :param options: Instance of FirefoxOptions.
        """

