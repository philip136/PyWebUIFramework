import typing as ty
from logging import Logger

from elements.element_type import ElementType
from elements.element_state import ElementState
from elements.base_element import BaseElement
from elements.element_finder import ElementFinder
from waitings.conditional_wait import ConditionalWait

T = ty.TypeVar('T', bound=BaseElement)


class ElementFactory:
    def __init__(self, conditional_wait: ConditionalWait, element_finder: ElementFinder, logger: Logger) -> None:
        self._conditional_wait = conditional_wait
        self._logger = logger

    def __get_element(self, element_type: ElementType, locator: str, name: str, state: ElementState)\
            -> ty.Type[ElementType]: ...
    def get_button(self, locator: str, name: str, state: ElementState) -> ElementType.BUTTON: ...
    def __get_custom_element(self, cls: T, locator: str, name: str, state: ElementState) -> ty.Type[ElementType]: ...