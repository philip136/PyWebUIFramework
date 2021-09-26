import logging
import typing as ty
from injector import Module, ClassProvider, InstanceProvider, singleton, Binder

from core.applications.base_application import BaseApplication
from core.utilities.base_settings_file import BaseSettingsFile
from core.utilities.utilities_module import UtilitiesModule
from core.waitings.conditional_wait import ConditionalWait
from core.configurations.element_cache_configuration import ElementCacheConfiguration
from core.configurations.configuration_module import ConfigurationModule
from core.configurations.base_retry_configuration import BaseRetryConfiguration
from core.configurations.base_timeout_configuration import BaseTimeoutConfiguration
from core.localization.localization_module import LocalizationModule
from core.localization.managers.base_localization_manager import BaseLocalizationManager
from core.localization.loggers.base_localized_logger import BaseLocalizedLogger
from core.localization.configurations.base_logger_configuration import BaseLoggerConfiguration
from core.localization.loggers.logger_config import Logger
from core.utilities.base_action_retrier import BaseActionRetrier
from core.utilities.action_retrier import ActionRetrier
from core.elements.base_element_finder import BaseElementFinder
from core.elements.element_finder import ElementFinder


class QualityModule(Module):
    """Default class for register providers."""

    def __init__(self, application_provider: ty.Callable[..., BaseApplication]):
        """Initial link for binding."""
        self.__application_provider = application_provider

    def configure(self, binder: Binder):
        """Bind interfaces to implementations.
        :param binder: Binder object.
        """
        binder.bind(BaseApplication, to=self.__application_provider, scope=singleton)
        binder.bind(logging.Logger, to=InstanceProvider(Logger), scope=singleton)
        binder.bind(BaseSettingsFile, to=InstanceProvider(UtilitiesModule.get_instance_of_settings_file()))
        binder.bind(BaseLoggerConfiguration, to=ClassProvider(ConfigurationModule.get_logger_configuration()),
                    scope=singleton)
        binder.bind(BaseTimeoutConfiguration, to=ClassProvider(ConfigurationModule.get_timeout_configuration()),
                    scope=singleton)
        binder.bind(BaseRetryConfiguration, to=ClassProvider(ConfigurationModule.get_action_retry()),
                    scope=singleton)
        binder.bind(BaseActionRetrier, to=ClassProvider(ActionRetrier)),
        binder.bind(ElementCacheConfiguration, to=ClassProvider(ConfigurationModule.get_element_cache_configuration()),
                    scope=singleton)
        binder.bind(BaseLocalizationManager, to=ClassProvider(LocalizationModule.get_localization_manager()),
                    scope=singleton)
        binder.bind(BaseLocalizedLogger, to=ClassProvider(LocalizationModule.get_localization_logger()),
                    scope=singleton)
        binder.bind(BaseElementFinder, to=ClassProvider(ElementFinder)),
        binder.bind(ConditionalWait, to=ClassProvider(ConditionalWait))
