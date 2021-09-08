from injector import inject
from abc import ABC, abstractmethod

from core.utilities.base_settings_file import BaseSettingsFile


class BaseLoggerConfiguration(ABC):
    """Describes logger configuration."""

    @inject
    def __init__(self, settings_file: BaseSettingsFile):
        self._settings_file = settings_file

    @property
    @abstractmethod
    def language(self) -> str:
        """Get language of framework.
        :return: Language.
        :rtype: str.
        """
        pass

    @property
    @abstractmethod
    def log_page_source(self) -> bool:
        """Perform page source logging in case of catastrophic failures or not.
        :return: Perform page source or not.
        :rtype: bool.
        """
        pass
