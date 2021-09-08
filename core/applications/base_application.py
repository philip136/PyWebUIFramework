from abc import ABC, abstractmethod


class BaseApplication(ABC):
    """Abstraction for base application."""

    @property
    @abstractmethod
    def is_started(self):
        """App is started or not."""
        pass

    @property
    @abstractmethod
    def driver(self):
        """Get driver."""
        pass

    @abstractmethod
    def set_implicit_wait_timeout(self, timeout: int):
        """Set implicit wait timeout."""
        pass
