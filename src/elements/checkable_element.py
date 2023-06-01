from abc import ABC

from core.elements.base_element import BaseElement


class CheckableElement(BaseElement, ABC):
    def is_checked(self):
        self._log_element_action('loc.checkable.get.state')
        state = self.get_state()
        self._log_element_action('loc.checkable.state', state)
        return state

    def get_state(self):
        return self._do_with_retry(lambda: self.get_element().is_selected())
