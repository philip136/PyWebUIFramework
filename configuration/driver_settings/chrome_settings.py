from configuration.driver_settings.base_driver_settings import BaseDriverSettings


class ChromeSettings(BaseDriverSettings):
    def _set_preferences(self, options):
        options.add_experimental_option('prefs', self.browser_options)

    @property
    def download_dir_capability_key(self) -> str:
        return 'download.default_directory'
