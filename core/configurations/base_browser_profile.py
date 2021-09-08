import typing as ty
from abc import ABC, abstractmethod
from injector import inject

from core.utilities.base_settings_file import BaseSettingsFile
from core.localization.loggers.base_localized_logger import BaseLocalizedLogger

DS = ty.TypeVar('DS')


class BaseBrowserProfile(ABC):
    """Abstract class responsible for basic browser settings."""
    _driver_settings = None

    @inject
    def __init__(self, settings_file: BaseSettingsFile, localization_logger: BaseLocalizedLogger) -> None:
        """Provides a SettingsFile to select the required configuration settings.
        Provides a LocalizedLogger for selecting the required messages in the logs."""
        self.__settings_file = settings_file
        self._localization_logger = localization_logger

    @property
    def settings_file(self) -> BaseSettingsFile:
        """Get SettingsFile instance.
        :return: Instance of SettingsFile.
        :rtype: BaseSettingsFile.
        """
        return self.__settings_file

    @property
    def browser_name(self) -> str:
        """Get browser name from settings.json.
        :return: Browser name.
        :rtype: str.
        """
        return self.__settings_file.get_value('browserName').lower()

    @property
    def is_remote(self) -> bool:
        """Connection is remote or not.
        :return: True if connection is remote else False.
        :rtype: bool.
        """
        return self.__settings_file.get_value('isRemote')

    @property
    def is_element_highlight_enabled(self) -> bool:
        """Is element highlight enabled True or False.
        :return: True if enabled else False.
        :rtype: bool.
        """
        return self.__settings_file.get_value('isElementHighlightEnabled')

    @abstractmethod
    def get_driver_settings(self) -> DS:
        """Get DriverSettings instance (ChromeSettings, FirefoxSettings and etc).
        :return: DriverSettings instance.
        :rtype: DS.
        """
        pass
