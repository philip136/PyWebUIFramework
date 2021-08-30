from elements.state.element_state_provider import ElementStateProvider


class DefaultElementStateProvider(ElementStateProvider):
    def __init__(self, locator, conditional_wait, element_finder, logger):
        super(DefaultElementStateProvider, self).__init__(logger=logger)
        self._locator = locator
        self._conditional_wait = conditional_wait
        self._element_finder = element_finder

    def is_clickable(self):
        return self.__wait_for_is_clickable(timeout=0, timeout_exception=True)

    def __wait_for_is_clickable(self, timeout, timeout_exception):
        desired_state = self._element_clickable()
        desired_state = timeout_exception if desired_state.with_except_timeout_exception() else desired_state
        return self.__is_element_in_desired_condition(element_state_condition=desired_state, timeout=timeout)

    def __is_element_in_desired_condition(self, element_state_condition, timeout):
        return self._element_finder.find_elements(self._locator, element_state_condition, timeout)