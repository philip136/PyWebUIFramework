from logging import Logger
from browser.browser import Browser
from elements.element_factory import ElementFactory
from elements.element_finder import ElementFinder
from application.ioc_application_container import IoCApplicationContainer


class PyServices:
    __ioc_container: IoCApplicationContainer

    @classmethod
    def get_browser(cls) -> Browser:
        """Get browser instance.
        :return: Browser instance.
        :rtype: Browser.
        """

    @classmethod
    def get_element_factory(cls) -> ElementFactory:
        """Get element factory for choice needed element."""

    @classmethod
    def get_element_finder(cls) -> ElementFinder:
        """Get finder for finding elements."""

    @classmethod
    def get_logger(cls) -> Logger:
        """Get logger."""

    @classmethod
    def get_config_data(cls) -> dict:
        """Get JSON schema for setup default settings in browser."""