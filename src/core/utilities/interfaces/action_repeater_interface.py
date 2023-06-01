import typing as ty
from abc import ABC, abstractmethod

T = ty.TypeVar('T')


class IActionRepeater(ABC):
    @abstractmethod
    def do_with_retry(self, function: ty.Callable[..., T],
                      handled_exceptions: ty.List[ty.Type[Exception]] = []) -> T:
        """
        Try to execute function repeatedly.
        :param function: Function to retry.
        :param handled_exceptions: Exceptions which will be catches during function execution.
        :return: Result of executed function.
        :rtype: T.
        """
        pass
