from abc import ABC, abstractmethod


class BaseApplication(ABC):
    @property
    @abstractmethod
    def is_started(self):
        pass

    @property
    @abstractmethod
    def driver(self):
        pass

    @abstractmethod
    def set_implicit_wait_timeout(self, timeout):
        pass
