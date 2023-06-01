from abc import ABC, abstractmethod


class ILoggerConfiguration(ABC):
    """Describes logger configuration."""

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
