from dependency_injector.wiring import inject, Provide
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from application.ioc_config_container import IocConfigContainer
from elements.state.desired_state import DesiredState
from elements.element_state import ElementState


class ElementFinder:
    __was_any_element_found = False

    @inject
    def __init__(self, conditional_wait, web_driver, logger=Provide[IocConfigContainer.logger]):
        self._conditional_wait = conditional_wait
        self._web_driver = web_driver
        self._logger = logger

    @staticmethod
    def resolve_state(element_state):
        if element_state == ElementState.DISPLAYED.value:
            element_state_condition = 'is_displayed'
        else:
            if element_state != ElementState.EXISTS_IN_ANY_STATE.value:
                raise AttributeError('State is not recognized')

            else:
                element_state_condition = True
        return DesiredState(element_state_condition, element_state)

    def find_element(self, locator, element_state, timeout):
        desired_state = self.resolve_state(element_state).with_except_no_such_element_exceptions()
        return self.find_elements(locator, desired_state, timeout)[0]

    def find_elements(self, locator, desired_state, timeout):
        result_elements = []
        try:
            is_founded = self._try_to_find_elements(locator, desired_state, result_elements)
            if not is_founded:
                self._conditional_wait.wait_for(exp_condition=is_founded, timeout=timeout, locator=locator)
        except TimeoutException as e:
            self._handle_timeout_exceptions(e, locator, desired_state)
        return result_elements

    def _try_to_find_elements(self, locator, desired_state, result_elements):
        by, value = locator
        current_found_elements = self._web_driver.find_elements(by=by, value=value)
        self.__was_any_element_found = True if current_found_elements else False
        for element in current_found_elements:
            if desired_state.state_name == ElementState.DISPLAYED.value:
                desired_state_method = getattr(element, 'is_' + desired_state.state_name)
                if desired_state_method():
                    result_elements.append(element)
            else:
                result_elements.append(element)
        return True if current_found_elements else False

    def _handle_timeout_exceptions(self, exception, locator, desired_state):
        message = "No elements with locator %s were found in %s state" % (locator, desired_state.state_name)
        if desired_state.is_except_timeout_exception:
            if self.__was_any_element_found:
                self._logger.debug("Element found but not in state")
            else:
                if desired_state.is_except_no_such_element_exception:
                    raise NoSuchElementException(message)
                self._logger.debug("Element not found in this state %s" % desired_state.state_name)
        else:
            combined_message = message + ": " + exception.msg
            if desired_state.is_except_no_such_element_exception and self.__was_any_element_found is False:
                raise NoSuchElementException(combined_message)
            raise TimeoutException(combined_message)
