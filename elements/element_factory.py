import typing as ty

from selenium.webdriver.common.by import By
from core.elements.element_factory import ElementFactory as ElementFactoryCore
from core.elements.states.element_state import ElementState
from elements.button import Button
from elements.link import Link
from elements.label import Label
from elements.check_box import CheckBox
from elements.combo_box import ComboBox
from elements.text_box import TextBox


# TODO: Возможно лучше будет завести отдельную сущность из которой можно будет получить любого провайдера.


class ElementFactory(ElementFactoryCore):
    def get_button(self, locator: ty.Tuple[By, str], name: str, element_state=ElementState.DISPLAYED.value):
        return Button(locator, name, element_state, self)

    def get_label(self, locator: ty.Tuple[By, str], name: str, element_state=ElementState.DISPLAYED.value):
        return Label(locator, name, element_state, self)

    def get_link(self, locator: ty.Tuple[By, str], name: str, element_state=ElementState.DISPLAYED.value):
        return Link(locator, name, element_state, self)

    def get_check_box(self, locator: ty.Tuple[By, str], name: str, element_state=ElementState.DISPLAYED.value):
        return CheckBox(locator, name, element_state, self)

    def get_combo_box(self, locator: ty.Tuple[By, str], name: str, element_state=ElementState.DISPLAYED.value):
        return ComboBox(locator, name, element_state, self)

    def get_text_box(self, locator: ty.Tuple[By, str], name: str, element_state=ElementState.DISPLAYED.value):
        return TextBox(locator, name, element_state, self)
