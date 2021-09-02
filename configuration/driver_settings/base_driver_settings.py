import os
from abc import ABC, abstractmethod

from core.utilities.base_settings_file import BaseSettingsFile


class BaseDriverSettings(ABC):
    def __init__(self, options, settings_file: BaseSettingsFile):
        self._options = options
        self.__settings_file = settings_file

    @property
    def browser_name(self) -> str:
        return self.__settings_file.get_value('browserName')

    @property
    def driver_settings_data(self):
        return self.__settings_file.get_value(f'driverSettings.{self.browser_name}')

    def get_capabilities(self):
        self._set_capabilities(options=self._options)
        self._set_preferences(options=self._options)
        self._set_arguments(options=self._options)
        return self._options

    @property
    def web_driver_version(self):
        return self.driver_settings_data.get('webDriverVersion', 'latest')

    @property
    def browser_options(self):
        return self.driver_settings_data['options']

    @property
    def browser_capabilities(self):
        return self.driver_settings_data['capabilities']

    @property
    def browser_start_arguments(self):
        return self.driver_settings_data['startArguments']

    def _set_capabilities(self, options):
        for key, val in self.browser_capabilities.items():
            options.set_capability(key, val)

    def _set_arguments(self, options):
        for argument in self.browser_start_arguments:
            options.add_argument(argument)

    @abstractmethod
    def _set_preferences(self, options):
        pass

    @property
    @abstractmethod
    def download_dir_capability_key(self) -> str:
        pass

    def get_download_dir(self):
        browser_options = self.browser_options
        key = self.download_dir_capability_key

        if key in browser_options.keys():
            path_in_configuration = browser_options[key]
            return self.__get_absolute_path(path_in_configuration) if '.' in path_in_configuration \
                else path_in_configuration
        raise FileNotFoundError("failed to find %s profiles option for %s", key, self.browser_name)

    @staticmethod
    def __get_absolute_path(path: str):
        return os.path.realpath(path)
