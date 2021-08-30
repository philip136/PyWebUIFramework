import time

from dependency_injector.wiring import inject, Provide

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import TimeoutException

from application.ioc_config_container import IocConfigContainer


class ConditionalWait:
    @inject
    def __init__(self, web_driver, config_data=Provide[IocConfigContainer.config_file]):
        self._web_driver = web_driver
        self._config_data = config_data
        self._timeout = self._config_data.get_timeouts()['timeoutCondition']

    @property
    def timeout(self):
        return self._timeout

    def wait_for(self, exp_condition, timeout, locator=None, polling_interval=None, message='', exception_to_ignore=None):
        if exp_condition:
            self.wait_for_true(exp_condition, timeout, polling_interval, message, exception_to_ignore)
        else:
            self.wait_for_exp_condition(timeout, locator, polling_interval, message, exception_to_ignore)

    def wait_for_true(self, bool_condition, timeout, polling_interval=None, message='', exceptions_to_ignore=None):
        supplier = bool_condition
        if not isinstance(bool_condition, bool):
            raise TypeError

        timeout_in_seconds = self.__resolve_conditional_timeout(timeout=timeout)
        polling_interval = self.__resolve_polling_interval(polling_interval=polling_interval)
        ex_message = self.__resolve_message(message)
        start_time = time.time()
        while True:
            if self.__is_conditional_satisfied(supplier, exceptions_to_ignore):
                return

            current_time = time.time()
            if (current_time - start_time) > timeout_in_seconds:
                exception_message = f"Timed out after {timeout_in_seconds}s seconds during wait for condition " \
                                    f"'{ex_message}s'"
                raise TimeoutException(exception_message)

            time.sleep(polling_interval)

    def wait_for_exp_condition(self, timeout, locator, polling_interval=None, message='',
                               exceptions_to_ignore=None):
        self._web_driver.implicitly_wait(0)
        timeout_in_seconds = self.__resolve_conditional_timeout(timeout)
        actual_polling_interval = self.__resolve_polling_interval(polling_interval)
        ex_message = self.__resolve_message(message)
        wait = WebDriverWait(driver=self._web_driver, timeout=timeout_in_seconds,
                             poll_frequency=actual_polling_interval, ignored_exceptions=exceptions_to_ignore)
        try:
            by, value = locator
            return wait.until(method=presence_of_element_located((by, value)), message=ex_message)
        finally:
            self._web_driver.implicitly_wait(self._config_data['timeouts']['timeoutImplicit'])

    @staticmethod
    def __is_conditional_satisfied(boolean_condition, exceptions_to_ignore=None):
        try:
            return boolean_condition
        except Exception as e:
            if exceptions_to_ignore is None or e not in exceptions_to_ignore:
                raise
            return False

    def __resolve_conditional_timeout(self, timeout=None):
        if timeout is None:
            return self._config_data['timeouts']['timeoutCondition"']
        return timeout

    def __resolve_polling_interval(self, polling_interval=None):
        if polling_interval is None:
            return self._config_data['timeouts']['timeoutPollingInterval']
        return polling_interval

    @staticmethod
    def __resolve_message(message):
        return message if len(message) > 0 else str()
