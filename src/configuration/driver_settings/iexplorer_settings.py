from selenium.webdriver.ie.options import Options
from configuration.driver_settings.base_driver_settings import BaseDriverSettings


class IExplorerSettings(BaseDriverSettings):
    def get_capabilities(self) -> Options:
        """Set and get options for driver.
        :return: Driver options.
        :rtype: Options.
        """
        self._set_arguments(options=self._options)
        return super(IExplorerSettings, self).get_capabilities()

    @property
    def download_dir_capability_key(self) -> str:
        """Get dir capability key.
        :return: Dir capability key.
        :rtype: str.
        """
        raise ValueError('Download directory for Internet Explorer profiles is not supported')
