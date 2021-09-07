from core.elements.base_element import BaseElement

from selenium.webdriver.support.ui import Select


class ComboBox(BaseElement):
    @property
    def _element_type(self) -> str:
        return self._localization_manager.get_localized_message('loc.combobox')

    def click_and_select_by_value(self, value: str):
        self.click()