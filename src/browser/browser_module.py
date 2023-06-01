from injector import ClassProvider, singleton, InstanceProvider, Binder

from src.core.applications.quality_module import QualityModule
from src.core.configurations.interfaces.browser_profile_interface import IBrowserProfile
from src.configuration.browser_profile import BrowserProfile
from src.core.elements.base_element_factory import BaseElementFactory
from src.core.configurations.interfaces.timeout_configuration_interface import ITimeoutConfiguration
from src.configuration.timeout_configuration import TimeoutConfiguration
from src.elements.element_factory import ElementFactory


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
