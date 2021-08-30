from elements.element_state import ElementState


class ElementCacheHandler:
    __remote_element = None

    def __init__(self, locator, state, finder):
        self._locator = locator
        self._state = state
        self._finder = finder

    def is_refresh_needed(self, custom_state):
        if self.was_cached() is not True:
            return True

        try:
            is_displayed = self.__remote_element.is_displayed()
            required_state = self.__get_required_state(custom_state)
            return required_state == ElementState.DISPLAYED.value and is_displayed is not True
        except Exception:
            return True

    def __get_required_state(self, custom_state):
        return self._state if custom_state is None else custom_state

    def was_cached(self):
        return True if self.__remote_element is not None else False

    def get_element(self, timeout, custom_state=None):
        required_state = self.__get_required_state(custom_state)
        if self.is_refresh_needed(required_state):
            self.__remote_element = self._finder.find_element(self._locator, required_state, timeout)
        return self.__remote_element
