from core.elements.base_element import BaseElement


class Link(BaseElement):
    @property
    def _element_type(self) -> str:
        return self._localization_manager.get_localized_message('loc.link')

    @property
    def href(self):
        return self.get_attribute('href')
