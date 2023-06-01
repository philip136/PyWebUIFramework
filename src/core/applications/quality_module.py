import logging
import typing as ty
from injector import Module, ClassProvider, InstanceProvider, singleton, Binder

from core.applications.interfaces.application_interface import IApplication
from core.utilities.interfaces.settings_file_interface import ISettingsFile
from core.utilities.utilities_module import UtilitiesModule
from core.waitings.interfaces.conditional_wait_interface import IConditionalWait
from core.waitings.conditional_wait import ConditionalWait
from core.configurations.element_cache_configuration import ElementCacheConfiguration
from core.configurations.configuration_module import ConfigurationModule
from core.configurations.interfaces.retry_configuration_interface import IRetryConfiguration
from core.configurations.interfaces.timeout_configuration_interface import ITimeoutConfiguration
from core.localization.localization_module import LocalizationModule
from core.localization.managers.interfaces.localization_interface import ILocalizationManager
from core.localization.loggers.interfaces.localized_logger_interface import ILocalizedLogger
from core.localization.configurations.interfaces.logger_configuration_interface import ILoggerConfiguration
from core.localization.loggers.logger_config import Logger
from core.utilities.interfaces.action_repeater_interface import IActionRepeater
from core.utilities.action_repeater import ActionRepeater
from core.elements.element_finder_interface import IElementFinder
from core.elements.element_finder import ElementFinder


class QualityModule(Module):
    """Default class for register providers."""

    def __init__(self, application_provider: ty.Callable[..., IApplication]):
        """Initial link for binding."""
        self.__application_provider = application_provider

    def configure(self, binder: Binder):
        """Bind interfaces to implementations.
        :param binder: Binder object.
        """
        binder.bind(IApplication, to=self.__application_provider, scope=singleton)
        binder.bind(logging.Logger, to=InstanceProvider(Logger), scope=singleton)
        binder.bind(ISettingsFile, to=InstanceProvider(UtilitiesModule.get_instance_of_settings_file()))
        binder.bind(ILoggerConfiguration, to=ClassProvider(ConfigurationModule.get_logger_configuration()),
                    scope=singleton)
        binder.bind(ITimeoutConfiguration, to=ClassProvider(ConfigurationModule.get_timeout_configuration()),
                    scope=singleton)
        binder.bind(IRetryConfiguration, to=ClassProvider(ConfigurationModule.get_action_retry()),
                    scope=singleton)
        binder.bind(IActionRepeater, to=ClassProvider(ActionRepeater)),
        binder.bind(ElementCacheConfiguration, to=ClassProvider(ConfigurationModule.get_element_cache_configuration()),
                    scope=singleton)
        binder.bind(ILocalizationManager, to=ClassProvider(LocalizationModule.get_localization_manager()),
                    scope=singleton)
        binder.bind(ILocalizedLogger, to=ClassProvider(LocalizationModule.get_localization_logger()),
                    scope=singleton)
        binder.bind(IElementFinder, to=ClassProvider(ElementFinder)),
        binder.bind(IConditionalWait, to=ClassProvider(ConditionalWait))
