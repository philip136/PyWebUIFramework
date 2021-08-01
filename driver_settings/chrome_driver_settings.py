from driver_settings.driver_settings import DriverSettings


class ChromeDriverSettings(DriverSettings):
    """Driver settings for Chrome."""

    def _set_preferences(self, options):
        """Setup preferences.

        :param options: Instance of ChromeOptions.
        """
        options.add_experimental_option('prefs', self.browser_options)
