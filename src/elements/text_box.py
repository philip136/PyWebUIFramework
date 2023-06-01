from src.core.elements.base_element import BaseElement
from src.elements.attributes import Attributes
from selenium.webdriver.common.keys import Keys


class TextBox(BaseElement):
    __LOG_TYPING = "loc.text.typing"
    __LOG_CLEARING = "loc.text.clearing"

    @property
    def _element_type(self) -> str:
        return self._localization_manager.get_localized_message('loc.text.field')

    def submit(self):
        self._do_with_retry(lambda: self.get_element().submit())

    def focus(self):
        self._do_with_retry(lambda: self.get_element().send_keys(''))

    @property
    def __log_masked_value(self):
        return self._localization_manager.get_localized_message('loc.text.masked_value')

    def un_focus(self):
        self._do_with_retry(lambda: self.get_element().send_keys(Keys.TAB))

    @property
    def value(self):
        return self.get_attribute(Attributes.VALUE.value)

    def type_secret(self, value: str):
        self.type(value, True)

    def clear_and_type_secret(self, value: str):
        self.clear_and_type(value, True)

    def type(self, value: str, mask_value_in_log: bool = False):
        self._log_element_action(self.__LOG_TYPING, mask_value_in_log if self.__log_masked_value else value)
        self._do_with_retry(lambda: self.get_element().send_keys(value))

    def clear_and_type(self, value: str, mask_value_in_log: bool = False):
        self._log_element_action(self.__LOG_CLEARING)
        self._log_element_action(self.__LOG_TYPING, mask_value_in_log if self.__log_masked_value else value)

        def clear_and_send_keys(element):
            element.clear()
            element.send_keys(value)

        self._do_with_retry(lambda: clear_and_send_keys(self.get_element()))
