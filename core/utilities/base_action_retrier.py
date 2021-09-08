import typing as ty
from abc import ABC, abstractmethod

from injector import inject
from core.configurations.base_retry_configuration import BaseRetryConfiguration

T = ty.TypeVar('T')


class BaseActionRetrier(ABC):
    @inject
    def __init__(self, retry_configuration: BaseRetryConfiguration):
        """Initialize retrier with configuration."""
        self._retry_configuration = retry_configuration

    @abstractmethod
    def do_with_retry(self, function: ty.Callable[..., T],
                      handled_exceptions: ty.List[ty.Type[Exception]] = []) -> T:
        """
        Try to execute function repeatedly.
        :param function: Function to retry.
        :param handled_exceptions: Exceptions which will be catches during function execution.
        :return: Result of executed function.
        """
        pass
