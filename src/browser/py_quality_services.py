import typing as ty
from threading import local

from injector import Injector
from src.browser.browser import Browser
from src.browser.browser_module import BrowserModule
from src.browser.base_browser_factory import BaseBrowserFactory
from src.browser.local_browser_factory import LocalBaseBrowserFactory
from src.configuration.browser_profile import BrowserProfile
from src.core.applications.quality_services import QualityServices
from src.core.waitings.conditional_wait import ConditionalWait
from src.elements.element_factory import ElementFactory
from src.core.localization.loggers.interfaces.localized_logger_interface import ILocalizedLogger

T = ty.TypeVar('T', bound=QualityServices)
BF = ty.TypeVar('BF', bound=BaseBrowserFactory)

LOCAL = local()


class PyQualityServices(QualityServices):
    def __init__(self) -> None:
        """Create BrowserModule which bound main objects."""
        service_module = BrowserModule(self.get_browser)
        super(PyQualityServices, self).__init__(application_provider=self.get_browser, service_module=service_module)

    @classmethod
    def get_browser(cls) -> Browser:
        """Get browser instance.
        :return: Browser instance.
        :rtype: Browser.
        """
        return cls.get_instance().get_app(cls.__start_browser)

    @classmethod
    def __start_browser(cls) -> Browser:
        """Choose interface for future browser.
        :return: Browser instance.
        :rtype: Browser.
        """
        return cls.get_browser_factory().get_browser()

    @classmethod
    def get_browser_factory(cls) -> BF:
        """Select a factory for browsers if it does not exist, install it.
        :return: Factory that implements BaseBrowserFactory.
        :rtype: BF.
        """
        if getattr(cls.get_instance(), 'browser_factory', None) is None:
            cls.set_default_browser_factory()
        return cls.get_instance().browser_factory

    @classmethod
    def set_browser_factory(cls, browser_factory: BF) -> None:
        """Set factory in current instance that implements BaseBrowserFactory.
        :param browser_factory: Factory implementing the interface BaseBrowserFactory.
        """
        setattr(cls.get_instance().__class__, 'browser_factory', browser_factory)

    @classmethod
    def set_default_browser_factory(cls) -> None:
        """Choose interface for browser factory."""
        browser_factory = cls.get_local_browser_factory()
        cls.set_browser_factory(browser_factory=browser_factory)

    @classmethod
    def get_instance(cls) -> T:
        """Get or create current instance.
        :return: Get or create current class.
        :rtype: T.
        """
        if getattr(LOCAL, '_instance_container', None) is None:
            setattr(LOCAL, '_instance_container', cls())
        return getattr(LOCAL, '_instance_container', None)

    @classmethod
    def get_service_provider(cls) -> Injector:
        """Get injector instance.
        :return: Injector object.
        :rtype: Injector.
        """
        return cls.get_instance().get_injector()

    @classmethod
    def get(cls, clz: ty.Any) -> ty.Any:
        """Get instance from injector instance.
        :param clz: Class that is associated.
        :return: Instance which is registered in injector.
        :rtype: ty.Any.
        """
        return cls.get_service_provider().get(clz)

    @classmethod
    def get_local_browser_factory(cls) -> LocalBaseBrowserFactory:
        """Get LocalBaseBrowserFactory from injector instance which implements BaseBrowserFactory.
        :return: Get LocalBaseBrowserFactory instance.
        :rtype: LocalBaseBrowserFactory.
        """
        return cls.get(LocalBaseBrowserFactory)

    @classmethod
    def get_element_factory(cls) -> ElementFactory:
        return cls.get(ElementFactory)

    @classmethod
    def get_browser_profile(cls) -> BrowserProfile:
        """Get BrowserProfile from injector instance which implements IBrowserProfile.
        :return: Get BrowserProfile instance.
        :rtype: BrowserProfile.
        """
        return cls.get(BrowserProfile)

    @classmethod
    def get_conditional_wait(cls) -> ConditionalWait:
        """Get ConditionalWait from injector instance.
        :return: Get ConditionalWait instance.
        :rtype: ConditionalWait.
        """
        return cls.get(ConditionalWait)

    @classmethod
    def get_localized_logger(cls) -> ILocalizedLogger:
        """Get LocalizationLogger from injector instance.
        :return: Get LocalizationLogger instance.
        :rtype: LocalizationLogger.
        """
        return cls.get(ILocalizedLogger)
