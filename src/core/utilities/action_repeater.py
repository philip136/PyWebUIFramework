import time
import typing as ty
from injector import inject

from core.utilities.interfaces.action_repeater_interface import IActionRepeater
from core.configurations.interfaces.retry_configuration_interface import IRetryConfiguration

T = ty.TypeVar('T')


class ActionRepeater(IActionRepeater):
    @inject
    def __init__(self, retry_configuration: IRetryConfiguration):
        """Initialize repeater with configuration."""
        self._retry_configuration = retry_configuration

    def do_with_retry(self, function: ty.Callable[..., T], handled_exceptions: ty.List[ty.Type[Exception]] = []) -> T:
        """
        Try to execute function repeatedly.
        :param function: Function to retry.
        :param handled_exceptions: Exceptions which will be catches during function execution.
        :return: Result of executed function.
        """
        retry_attempts_left = self._retry_configuration.number
        result = None

        while retry_attempts_left >= 0:
            try:
                result = function()
                break
            except Exception as exception:
                if self.__is_exception_handled(exception, handled_exceptions) and retry_attempts_left != 0:
                    time.sleep(self._retry_configuration.polling_interval)
                    retry_attempts_left -= 1
                else:
                    raise
        return result

    @staticmethod
    def __is_exception_handled(exception: Exception, handled_exceptions: ty.List[ty.Type[Exception]]) -> bool:
        return any(isinstance(exception, handled_exception) for handled_exception in handled_exceptions)
