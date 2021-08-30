from driver_settings.driver_settings import DriverSettings


class FirefoxDriverSettings(DriverSettings):
    def _set_preferences(self, options):
        for pref_name, pref_value in self.browser_options.items():
            options.set_preference(name=pref_name, value=pref_value)
