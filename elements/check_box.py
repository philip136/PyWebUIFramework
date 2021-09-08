from elements.checkable_element import CheckableElement


class CheckBox(CheckableElement):
    @property
    def _element_type(self) -> str:
        return self._localization_manager.get_localized_message('loc.checkbox')

    def set_state(self, state: bool):
        self._log_element_action('loc.setting.value', state)
        if state != self.get_state():
            self.click()

    def check(self):
        self.set_state(True)

    def uncheck(self):
        self.set_state(False)

    def is_checked(self):
        self._log_element_action('loc.checkable.get.state')
        state = self.get_state()
        self._log_element_action('loc.checkable.state', state)
        return state

    def get_state(self):
        return self._do_with_retry(lambda: self.get_element().is_selected())
