import typing as ty
from abc import ABC, abstractmethod

from elements.element_finder import ElementFinder
from configurations.element_cache_configuration import ElementCacheConfiguration


class BaseElement(ABC):
    def __init__(self, by, locator, name, state, element_finder) -> None: ...

    @abstractmethod
    def _get_element_finder(self) -> ElementFinder: ...

    @abstractmethod
    def _get_element_cache_configuration(self) -> ty.Type[ElementCacheConfiguration]: ...