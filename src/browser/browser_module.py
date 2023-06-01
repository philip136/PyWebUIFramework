from injector import ClassProvider, singleton, InstanceProvider, Binder

from core.applications.quality_module import QualityModule
from core.configurations.interfaces.browser_profile_interface import IBrowserProfile
from configuration.browser_profile import BrowserProfile
from core.elements.base_element_factory import BaseElementFactory
from core.configurations.interfaces.timeout_configuration_interface import ITimeoutConfiguration
from configuration.timeout_configuration import TimeoutConfiguration
from elements.element_factory import ElementFactory


class BrowserModule(QualityModule):
    """Class for register providers."""

    def configure(self, binder: Binder) -> None:
        """Bind interfaces to implementations.
        :param binder: Binder object.
        """
        super(BrowserModule, self).configure(binder)
        binder.bind(ITimeoutConfiguration, to=ClassProvider(TimeoutConfiguration), scope=singleton)
        binder.bind(IBrowserProfile, to=ClassProvider(BrowserProfile), scope=singleton)
        binder.bind(BaseElementFactory, to=InstanceProvider(ElementFactory))
