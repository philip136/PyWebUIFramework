import os
import typing as ty
from abc import ABC, abstractmethod

from core.utilities.base_settings_file import BaseSettingsFile

OPT = ty.TypeVar('OPT')


class BaseDriverSettings(ABC):
    def __init__(self, options: OPT, settings_file: BaseSettingsFile) -> None:
        self._options = options
        self.__settings_file = settings_file

    @property
    def browser_name(self) -> str:
        """Get browser name.
        :return: Browser name.
        :rtype: str.
        """
        return self.__settings_file.get_value('browserName')

    @property
    def driver_settings_data(self) -> ty.Dict[str, ty.Any]:
        """Get driver settings from settings.json.
        :return: Dictionary with driver settings.
        :return: ty.Dict[str, ty.Any].
        """
        return self.__settings_file.get_value(f'driverSettings.{self.browser_name}')

    def get_capabilities(self) -> OPT:
        """Set and get options for driver.
        :return: Driver options.
        :rtype: OPT.
        """
        self._set_capabilities(options=self._options)
        self._set_preferences(options=self._options)
        self._set_arguments(options=self._options)
        return self._options

    @property
    def web_driver_version(self) -> str:
        """Get WebDriver version, by default: latest.
        :return: WebDriver version.
        :rtype: str.
        """
        return self.driver_settings_data.get('webDriverVersion', 'latest')

    @property
    def browser_options(self) -> ty.Dict[str, ty.Any]:
        """Property for get browser options.
        :return: Browser options.
        :rtype: ty.Dict[str, ty.Any].
        """
        return self.driver_settings_data['options']

    @property
    def browser_capabilities(self) -> ty.Dict[str, ty.Any]:
        """Property for get browser capabilities.
        :return: Browser capabilities.
        :rtype: ty.Dict[str, ty.Any].
        """
        return self.driver_settings_data['capabilities']

    @property
    def browser_start_arguments(self) -> ty.Dict[str, ty.Any]:
        """Property for get start browser arguments.
        :return: Browser arguments.
        :rtype: ty.Dict[str, ty.Any].
        """
        return self.driver_settings_data['startArguments']

    def _set_capabilities(self, options: OPT) -> None:
        """Set capabilities.
        :param options: Instance of Options (Chrome, Firefox and etc).
        """
        for key, val in self.browser_capabilities.items():
            options.set_capability(key, val)

    def _set_arguments(self, options) -> None:
        """Set arguments.
        :param options: Instance of Options (Chrome, Firefox and etc).
        """
        for argument in self.browser_start_arguments:
            options.add_argument(argument)

    @abstractmethod
    def _set_preferences(self, options):
        """Abstract method for set preference, settings interfaces work differently.
        :param options: Instance of Options (Chrome, Firefox and etc)."""
        pass

    @property
    @abstractmethod
    def download_dir_capability_key(self) -> str:
        """Abstract method for dir capability key settings interfaces work differently.
        :return: Dir capability key.
        :rtype: str.
        """
        pass

    def get_download_dir(self) -> ty.AnyStr:
        """Get download dir path.
        :raise FileNotFoundError: File not found.
        :return: Path to download dir else raise exception.
        :rtype: str.
        """
        browser_options = self.browser_options
        key = self.download_dir_capability_key

        if key in browser_options.keys():
            path_in_configuration = browser_options[key]
            return self.__get_absolute_path(path_in_configuration) if '.' in path_in_configuration \
                else path_in_configuration
        raise FileNotFoundError("failed to find %s profiles option for %s", key, self.browser_name)

    @staticmethod
    def __get_absolute_path(path: str) -> ty.AnyStr:
        return os.path.realpath(path)
