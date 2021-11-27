from abc import ABC, abstractmethod


class IApplication(ABC):
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
