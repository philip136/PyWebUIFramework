from driver_settings.driver_settings import DriverSettings


class ChromeDriverSettings(DriverSettings):
    def _set_preferences(self, options):
        options.add_experimental_option('prefs', self.browser_options)
