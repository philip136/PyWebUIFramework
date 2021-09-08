from injector import ClassProvider, singleton, InstanceProvider, Binder

from core.applications.quality_module import QualityModule
from core.configurations.base_browser_profile import BaseBrowserProfile
from core.configurations.element_cache_configuration import ElementCacheConfiguration
from core.elements.base_element_factory import BaseElementFactory
from core.configurations.timeout_configuration import TimeoutConfigurationCore
from configuration.timeout_configuration import TimeoutConfiguration
from elements.element_factory import ElementFactory


class BrowserModule(QualityModule):
    """Class for register providers."""

    def configure(self, binder: Binder) -> None:
        """Bind interfaces to implementations.
        :param binder: Binder object.
        """
        super(BrowserModule, self).configure(binder)
        binder.bind(TimeoutConfigurationCore, to=ClassProvider(TimeoutConfiguration), scope=singleton)
        binder.bind(BaseBrowserProfile, to=ClassProvider(ElementCacheConfiguration), scope=singleton)
        binder.bind(BaseElementFactory, to=InstanceProvider(ElementFactory))
