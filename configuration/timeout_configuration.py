from injector import inject
from configuration.timeout import Timeout
from core.utilities.base_settings_file import BaseSettingsFile
from core.configurations.timeout_configuration import TimeoutConfigurationCore


class TimeoutConfiguration(TimeoutConfigurationCore):
    """Class for settings timeouts."""

    @inject
    def __init__(self, settings_file: BaseSettingsFile):
        """Provides a SettingsFile to select the required configuration settings and get durations
        for script and page load.
        """
        super(TimeoutConfiguration, self).__init__(settings_file)
        self.__script = self.__get_duration(Timeout.SCRIPT.value)
        self.__page_load = self.__get_duration(Timeout.PAGE_LOAD.value)

    def __get_duration(self, timeout: str) -> int:
        """Get duration from settings.json.
        :return: Duration time.
        :rtype: int.
        """
        return self._settings_file.get_value(f'timeouts.{timeout}')

    @property
    def script(self) -> int:
        """Property for get script duration.
        :return: Duration time.
        :rtype: int.
        """
        return self.__script

    @property
    def page_load(self) -> int:
        """Property for get page load duration.
        :return: Duration time.
        :rtype: int.
        """
        return self.__page_load
