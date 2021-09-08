from abc import ABC, abstractmethod
from datetime import timedelta

from injector import inject
from core.utilities.base_settings_file import BaseSettingsFile


class BaseRetryConfiguration(ABC):
    """Describes retry configuration."""

    @inject
    def __init__(self, settings_file: BaseSettingsFile):
        self._settings_file = settings_file

    @property
    @abstractmethod
    def number(self) -> int:
        """Get the number of attempts to retry.
        :return: Number or attempts.
        :rtype: int.
        """
        pass

    @property
    @abstractmethod
    def polling_interval(self) -> timedelta:
        """Get the polling interval used in retry.
        :return: Timedelta for polling interval.
        :rtype: timedelta.
        """
        pass
