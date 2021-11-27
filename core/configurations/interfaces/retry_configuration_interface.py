from abc import ABC, abstractmethod


class IRetryConfiguration(ABC):
    """Describes retry configuration."""

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
    def polling_interval(self) -> int:
        """Get the polling interval used in retry.
        :return: Timedelta for polling interval.
        :rtype: int.
        """
        pass
