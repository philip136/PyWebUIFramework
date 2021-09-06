import typing as ty

from selenium.webdriver.common.by import By
from core.elements.element_factory import ElementFactory as ElementFactoryCore
from core.elements.states.element_state import ElementState
from elements.button import Button


class ElementFactory(ElementFactoryCore):
    def get_button(self, locator: ty.Tuple[By, str], name: str, element_state=ElementState.DISPLAYED.value):
        return Button(locator, name, element_state, self)
