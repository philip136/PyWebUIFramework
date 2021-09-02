from configuration.driver_settings.base_driver_settings import BaseDriverSettings


class FirefoxSettings(BaseDriverSettings):
    def _set_preferences(self, options):
        for pref_name, pref_value in self.browser_options.items():
            options.set_preference(name=pref_name, value=pref_value)

    @property
    def download_dir_capability_key(self) -> str:
        return 'browser.download.dir'
