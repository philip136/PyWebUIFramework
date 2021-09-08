import time
import typing as ty

from core.utilities.base_action_retrier import BaseActionRetrier

T = ty.TypeVar('T')


class ActionRetrier(BaseActionRetrier):
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
                    time.sleep(self._retry_configuration.polling_interval.seconds)
                    retry_attempts_left -= 1
                else:
                    raise
        return result

    @staticmethod
    def __is_exception_handled(exception: Exception, handled_exceptions: ty.List[ty.Type[Exception]]) -> bool:
        return any(isinstance(exception, handled_exception) for handled_exception in handled_exceptions)
