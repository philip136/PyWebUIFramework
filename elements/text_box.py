from core.elements.base_element import BaseElement


class TextBox(BaseElement):
    @property
    def _element_type(self) -> str:
        return self._localization_manager.get_localized_message('loc.button')
