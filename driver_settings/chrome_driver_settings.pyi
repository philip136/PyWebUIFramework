from driver_settings.driver_settings import DriverSettings
from selenium.webdriver.chrome.options import Options as ChromeOptions


class ChromeDriverSettings(DriverSettings):
    """Driver settings for Chrome."""

    def _set_preferences(self, options: ChromeOptions) -> None:
        """Setup preferences.
        :param options: Instance of ChromeOptions.
        """