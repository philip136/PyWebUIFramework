from abc import ABC, abstractmethod

from core.utilities.interfaces.settings_file_interface import ISettingsFile


class ITimeoutConfiguration(ABC):
    """Abstraction for timeout configuration."""
    _settings_file: ISettingsFile = NotImplemented

    def _get_config_value(self, key: str) -> int:
        """Get value from settings.json.
        :param key: Key to get the value from settings.json.
        :return: Value from settings.json.
        :rtype: int.
        """
        return int(self._settings_file.get_value(key))

    @property
    @abstractmethod
    def implicit(self) -> int:
        """Get WedDriver ImplicitWait timeout.
        :return: Get timeout for implicit wait as integer.
        :rtype: int.
        """
        pass

    @property
    @abstractmethod
    def condition(self) -> int:
        """Get default ConditionalWait timeout.
        :return: Get timeout for conditional wait as integer.
        :rtype: int.
        """
        pass

    @property
    @abstractmethod
    def polling_interval(self) -> int:
        """Get ConditionalWait polling interval.
        :return: Get polling interval timeout as integer.
        :rtype: int.
        """
        pass

    @property
    @abstractmethod
    def command(self) -> int:
        """Get WebDriver Command timeout.
        :return: Get web driver command timeout as integer.
        :rtype: int.
        """
        pass
