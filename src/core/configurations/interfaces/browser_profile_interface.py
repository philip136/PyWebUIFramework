import typing as ty
from abc import ABC, abstractmethod

from src.configuration.driver_settings.base_driver_settings import BaseDriverSettings
from src.core.utilities.interfaces.settings_file_interface import ISettingsFile

DS = ty.TypeVar('DS', bound=BaseDriverSettings)


class IBrowserProfile(ABC):
    """Abstract class responsible for basic browser settings."""
    _driver_settings = None
    _settings_file: ISettingsFile = NotImplemented

    @property
    def settings_file(self) -> ISettingsFile:
        """Get SettingsFile instance.
        :return: Instance of SettingsFile.
        :rtype: ISettingsFile.
        """
        return self._settings_file

    @property
    def browser_name(self) -> str:
        """Get browser name from settings.json.
        :return: Browser name.
        :rtype: str.
        """
        return self.settings_file.get_value('browserName').lower()

    @property
    def is_remote(self) -> bool:
        """Connection is remote or not.
        :return: True if connection is remote else False.
        :rtype: bool.
        """
        return self.settings_file.get_value('isRemote')

    @property
    def is_element_highlight_enabled(self) -> bool:
        """Is element highlight enabled True or False.
        :return: True if enabled else False.
        :rtype: bool.
        """
        return self.settings_file.get_value('isElementHighlightEnabled')

    @abstractmethod
    def get_driver_settings(self) -> DS:
        """Get DriverSettings instance (ChromeSettings, FirefoxSettings and etc).
        :return: DriverSettings instance.
        :rtype: DS.
        """
        pass
