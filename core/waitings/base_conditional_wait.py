import typing as ty
from abc import ABC, abstractmethod

from injector import inject
from selenium.webdriver.remote.webdriver import WebDriver
from core.configurations.base_timeout_configuration import BaseTimeoutConfiguration
from core.applications.base_application import BaseApplication

T = ty.TypeVar('T')


class BaseConditionalWait(ABC):
    """Utility used to wait for some condition."""

    @inject
    def __init__(self, timeout_configuration: BaseTimeoutConfiguration, application: BaseApplication):
        """Initialize with configuration."""
        self.__timeout_configuration = timeout_configuration
        self.__application = application

    @abstractmethod
    def wait_for_with_driver(self, condition: ty.Callable[[WebDriver], T], timeout: int = 0,
                             polling_interval: int = 0, message: str = str(),
                             exceptions_to_ignore: ty.List[ty.Type[Exception]] = []) -> T:
        """
        Wait for some condition using WebDriver within timeout.
        :param condition: Function for waiting
        :param timeout: Condition timeout (in seconds). Default value is taken from configuration.
        :param polling_interval: Condition check interval (in milliseconds). Default value is taken from configuration.
        :param message: Part of error message in case of TimeoutException.
        :param exceptions_to_ignore: Possible exceptions that have to be ignored.
        :return: Result of condition.
        :raises: TimeoutException when timeout exceeded and condition not satisfied.
        """
        pass

    @abstractmethod
    def wait_for(self, condition: ty.Callable[..., bool], timeout: int = 0,
                 polling_interval: int = 0, exceptions_to_ignore: ty.List[ty.Type[Exception]] = []) -> bool:
        """
        Wait for some condition within timeout.
        :param condition: Function for waiting
        :param timeout: Condition timeout (in seconds). Default value is taken from configuration.
        :param polling_interval: Condition check interval (in milliseconds). Default value is taken from configuration.
        :param exceptions_to_ignore: Possible exceptions that have to be ignored.
        :return: True if condition satisfied and false otherwise.
        """
        pass

    @abstractmethod
    def wait_for_true(self, condition: ty.Callable[..., bool], timeout: int = 0, polling_interval: int = 0,
                      message: str = str(), exceptions_to_ignore: ty.List[ty.Type[Exception]] = []) -> None:
        """
        Wait for some condition within timeout.
        :param condition: Predicate for waiting.
        :param timeout: Condition timeout (in seconds). Default value is taken from configuration.
        :param polling_interval: Condition check interval (in milliseconds). Default value is taken from configuration.
        :param message: Part of error message in case of Timeout exception.
        :param exceptions_to_ignore: Possible exceptions that have to be ignored.
        """
        pass
