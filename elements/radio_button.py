from elements.checkable_element import CheckableElement


class RadioButton(CheckableElement):
    @property
    def _element_type(self) -> str:
        return self._localization_manager.get_localized_message('loc.radio')
