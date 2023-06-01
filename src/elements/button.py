from src.core.elements.base_element import BaseElement


class Button(BaseElement):
    @property
    def _element_type(self) -> str:
        return self._localization_manager.get_localized_message('loc.button')
