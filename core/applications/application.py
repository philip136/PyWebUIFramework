from abc import ABC, abstractmethod


class Application(ABC):
    @property
    @abstractmethod
    def is_started(self):
        pass
