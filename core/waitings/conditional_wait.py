import time
import typing as ty

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import StaleElementReferenceException
from core.waitings.base_conditional_wait import BaseConditionalWait

T = ty.TypeVar('T')


class ConditionalWait(BaseConditionalWait):
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
        wait_timeout = self.__resolve_condition_timeout(timeout)
        check_interval = self.__resolve_polling_interval(polling_interval)
        ignored_exceptions = (
            exceptions_to_ignore
            if exceptions_to_ignore
            else [StaleElementReferenceException]
        )
        self._application.set_implicit_wait_timeout(0)
        wait = WebDriverWait(self._application.driver, wait_timeout, check_interval, ignored_exceptions)
        try:
            return wait.until(condition, message)
        finally:
            self._application.set_implicit_wait_timeout(self._timeout_configuration.implicit)

    def wait_for(self, condition: ty.Callable[..., bool], timeout: int = 0, polling_interval: int = 0,
                 exceptions_to_ignore: ty.List[ty.Type[Exception]] = []) -> bool:
        """
        Wait for some condition within timeout.
        :param condition: Function for waiting
        :param timeout: Condition timeout (in seconds). Default value is taken from configuration.
        :param polling_interval: Condition check interval (in milliseconds). Default value is taken from configuration.
        :param exceptions_to_ignore: Possible exceptions that have to be ignored.
        :return: True if condition satisfied and false otherwise.
        """

        def func():
            self.wait_for_true(condition, timeout, polling_interval, exceptions_to_ignore=exceptions_to_ignore)
            return True

        return self.__is_condition_satisfied(func, [TimeoutError])

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
        wait_timeout = self.__resolve_condition_timeout(timeout)
        check_interval = self.__resolve_polling_interval(polling_interval)
        start_time = time.time()

        while True:
            if self.__is_condition_satisfied(condition, exceptions_to_ignore):
                return

            current_time = time.time()
            if (current_time - start_time) > wait_timeout:
                raise TimeoutError(
                    f"Timed out after {wait_timeout} seconds during wait for condition '{message}'"
                )

            time.sleep(check_interval)

    @staticmethod
    def __is_condition_satisfied(condition: ty.Callable[..., bool],
                                 exceptions_to_ignore: ty.List[ty.Type[Exception]] = []) -> bool:
        try:
            return condition()
        except Exception as exception:
            if any(
                    isinstance(exception, ignored_exception)
                    for ignored_exception in exceptions_to_ignore
            ):
                return False
            raise

    def __resolve_condition_timeout(self, timeout: int) -> int:
        return timeout if timeout is not None else self._timeout_configuration.condition

    def __resolve_polling_interval(self, polling_interval: int) -> int:
        return polling_interval if polling_interval is not None else self._timeout_configuration.polling_interval
