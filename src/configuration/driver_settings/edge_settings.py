from selenium.webdriver.edge.options import Options
from configuration.driver_settings.base_driver_settings import BaseDriverSettings


class EdgeSettings(BaseDriverSettings):
    def get_capabilities(self) -> Options:
        """Set and get options for driver.
        :return: Driver options.
        :rtype: Options.
        """
        self._set_arguments(options=self._options)
        self.__set_page_load_strategy()
        return super(EdgeSettings, self).get_capabilities()

    def __set_page_load_strategy(self) -> None:
        """Set page load strategy for edge, by default normal."""
        value = self.driver_settings_data.get('pageLoadStrategy', 'normal')
        self._options.page_load_strategy = value.lower()

    @property
    def download_dir_capability_key(self) -> str:
        """Get dir capability key.
        :return: Dir capability key.
        :rtype: str.
        """
        raise ValueError('Download directory for Internet Explorer profiles is not supported')
