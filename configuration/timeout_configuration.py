from injector import inject
from configuration.timeout import Timeout
from core.utilities.base_settings_file import BaseSettingsFile
from core.configurations.timeout_configuration import TimeoutConfigurationCore


class TimeoutConfiguration(TimeoutConfigurationCore):
    @inject
    def __init__(self, settings_file: BaseSettingsFile):
        super(TimeoutConfiguration, self).__init__(settings_file)
        self.__script = self.__get_duration(Timeout.SCRIPT.value)
        self.__page_load = self.__get_duration(Timeout.PAGE_LOAD.value)

    def __get_duration(self, timeout: str) -> int:
        return self._settings_file.get_value(f'timeouts.{timeout}')

    @property
    def script(self):
        return self.__script

    @property
    def page_load(self):
        return self.__page_load
