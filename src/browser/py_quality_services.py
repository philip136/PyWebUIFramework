import typing as ty
from threading import local

from injector import Injector
from browser.browser import Browser
from browser.browser_module import BrowserModule
from browser.base_browser_factory import BaseBrowserFactory
from browser.local_browser_factory import LocalBaseBrowserFactory
from configuration.browser_profile import BrowserProfile
from core.applications.quality_services import QualityServices
from core.waitings.conditional_wait import ConditionalWait
from elements.element_factory import ElementFactory
from core.localization.loggers.interfaces.localized_logger_interface import ILocalizedLogger

T = ty.TypeVar('T', bound=QualityServices)
BF = ty.TypeVar('BF', bound=BaseBrowserFactory)

LOCAL = local()


class classproperty(property):
    def __get__(self, obj, obj_type=None):
        return super(classproperty, self).__get__(obj_type)

    def __set__(self, obj, value):
        super(classproperty, self).__set__(type(obj), value)

    def __delete__(self, obj):
        super(classproperty, self).__delete__(type(obj))


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
        return cls.instance.get_app(cls.__start_browser)

    @classmethod
    def __start_browser(cls) -> Browser:
        """Choose interface for future browser.
        :return: Browser instance.
        :rtype: Browser.
        """
        return cls.browser_factory.get_browser()

    @classproperty
    def browser_factory(cls) -> BaseBrowserFactory:
        """Select a factory for browsers if it does not exist, install it.
        :return: Factory that implements BaseBrowserFactory.
        :rtype: BF.
        """
        if not getattr(cls.instance, '_browser_factory', None):
            cls.set_default_browser_factory()
        return cls.instance.browser_factory

    @browser_factory.setter
    def browser_factory(cls, browser_factory: BF) -> None:
        """Set factory in current instance that implements BaseBrowserFactory.
        :param browser_factory: Factory implementing the interface BaseBrowserFactory.
        """
        setattr(cls.instance.__class__, '_browser_factory', browser_factory)

    @classmethod
    def set_default_browser_factory(cls) -> None:
        """Choose interface for browser factory."""
        browser_factory = cls.local_browser_factory
        cls.browser_factory = browser_factory

    @classproperty
    def instance(cls) -> T:
        """Get or create current instance.
        :return: Get or create current class.
        :rtype: T.
        """
        if getattr(LOCAL, '_instance_container', None) is None:
            setattr(LOCAL, '_instance_container', cls())
        return getattr(LOCAL, '_instance_container', None)

    @classproperty
    def service_provider(cls) -> Injector:
        """Get injector instance.
        :return: Injector object.
        :rtype: Injector.
        """
        return cls.instance.get_injector()

    @classmethod
    def get(cls, clz: ty.Any) -> ty.Any:
        """Get instance from injector instance.
        :param clz: Class that is associated.
        :return: Instance which is registered in injector.
        :rtype: ty.Any.
        """
        return cls.service_provider.get(clz)

    @classproperty
    def local_browser_factory(cls) -> LocalBaseBrowserFactory:
        """Get LocalBaseBrowserFactory from injector instance which implements BaseBrowserFactory.
        :return: Get LocalBaseBrowserFactory instance.
        :rtype: LocalBaseBrowserFactory.
        """
        return cls.get(LocalBaseBrowserFactory)

    @classproperty
    def element_factory(cls) -> ElementFactory:
        return cls.get(ElementFactory)

    @classproperty
    def browser_profile(cls) -> BrowserProfile:
        """Get BrowserProfile from injector instance which implements IBrowserProfile.
        :return: Get BrowserProfile instance.
        :rtype: BrowserProfile.
        """
        return cls.get(BrowserProfile)

    @classproperty
    def conditional_wait(cls) -> ConditionalWait:
        """Get ConditionalWait from injector instance.
        :return: Get ConditionalWait instance.
        :rtype: ConditionalWait.
        """
        return cls.get(ConditionalWait)

    @classproperty
    def localized_logger(cls) -> ILocalizedLogger:
        """Get LocalizationLogger from injector instance.
        :return: Get LocalizationLogger instance.
        :rtype: LocalizationLogger.
        """
        return cls.get(ILocalizedLogger)
