from core.elements.base_element import BaseElement
from core.elements.base_element_factory import BaseElementFactory
from elements.element_types import ElementTypes


class Button(BaseElement):
    def __init__(self, locator, name, element_state, element_factory):
        super(Button, self).__init__(locator, name, element_state)
        self.__element_factory = element_factory

    @property
    def _element_factory(self) -> BaseElementFactory:
        return self.__element_factory

    @property
    def _element_type(self) -> str:
        return ElementTypes.BUTTON.value
