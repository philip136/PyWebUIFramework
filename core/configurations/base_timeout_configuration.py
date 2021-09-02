from abc import ABC, abstractmethod
from injector import inject

from core.utilities.base_settings_file import BaseSettingsFile


class BaseTimeoutConfiguration(ABC):
    """Abstraction for timeout configuration."""

    @inject
    def __init__(self, settings_file: BaseSettingsFile):
        self._settings_file = settings_file

    def _get_config_value(self, key: str) -> int:
        return int(self._settings_file.get_value(key))

    @property
    @abstractmethod
    def implicit(self) -> int:
        """Get WedDriver ImplicitWait timeout."""
        pass

    @property
    @abstractmethod
    def condition(self) -> int:
        """Get default ConditionalWait timeout."""
        pass

    @property
    @abstractmethod
    def polling_interval(self) -> int:
        """Get ConditionalWait polling interval."""
        pass

    @property
    @abstractmethod
    def command(self) -> int:
        """Get WebDriver Command timeout."""
        pass
