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
