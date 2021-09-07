import typing as ty
from abc import ABC

from selenium.webdriver.common.by import By
from browser.py_quality_services import PyQualityServices


class BaseForm(ABC):
    def __init__(self, locator: ty.Tuple[By, str], name: str):
        self._locator = locator
        self._name = name

    @property
    def locator(self) -> ty.Tuple[By, str]:
        return self._locator

    @property
    def name(self) -> str:
        return self._name

    def _get_form_label(self):
        return PyQualityServices.get_element_factory().get_label(self.locator, self.name)

    @property
    def state(self):
        return self._get_form_label().state

    def is_displayed(self):
        return self.state.wait_for_displayed()

    def scroll_by(self, x: int, y: int):
        self._get_form_label().js_action.scroll_by(x, y)

    @property
    def size(self):
        return self._get_form_label().get_element().size

    @classmethod
    def _get_element_factory(cls):
        return PyQualityServices.get_element_factory()

    @classmethod
    def _get_localized_logger(cls):
        return PyQualityServices.get_localized_logger()
