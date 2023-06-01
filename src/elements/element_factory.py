import typing as ty

from selenium.webdriver.common.by import By
from src.core.elements.element_factory import ElementFactory as ElementFactoryCore
from src.core.elements.states.element_state import Displayed
from src.elements.button import Button
from src.elements.link import Link
from src.elements.label import Label
from src.elements.check_box import CheckBox
from src.elements.combo_box import ComboBox
from src.elements.text_box import TextBox
from src.elements.radio_button import RadioButton



class ElementFactory(ElementFactoryCore):
    def get_button(self, locator: ty.Tuple[By, str], name: str, element_state=Displayed()) -> Button:
        return Button(locator, name, element_state, self)

    def get_radio_button(self, locator: ty.Tuple[By, str], name: str, element_state=Displayed()) -> RadioButton:
        return RadioButton(locator, name, element_state, self)

    def get_label(self, locator: ty.Tuple[By, str], name: str, element_state=Displayed()) -> Label:
        return Label(locator, name, element_state, self)

    def get_link(self, locator: ty.Tuple[By, str], name: str, element_state=Displayed()) -> Link:
        return Link(locator, name, element_state, self)

    def get_check_box(self, locator: ty.Tuple[By, str], name: str, element_state=Displayed()) -> CheckBox:
        return CheckBox(locator, name, element_state, self)

    def get_combo_box(self, locator: ty.Tuple[By, str], name: str, element_state=Displayed()) -> ComboBox:
        return ComboBox(locator, name, element_state, self)

    def get_text_box(self, locator: ty.Tuple[By, str], name: str, element_state=Displayed()) -> TextBox:
        return TextBox(locator, name, element_state, self)
