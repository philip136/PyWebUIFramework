import typing as ty
from logging import Logger
from abc import ABC

from selenium.webdriver.remote.webdriver import WebElement


class ElementStateProvider(ABC):
    def __init__(self, logger: Logger) -> None:
        self._logger = logger

    @staticmethod
    def _element_is_enabled(element: WebElement) -> bool: ...
