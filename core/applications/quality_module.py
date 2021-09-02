from logging import Logger, getLogger
from injector import Module, ClassProvider, InstanceProvider, singleton

from core.applications.application import Application
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

# TODO: Logger no print because logging always return new instance without StreamHandler(sys.stderr)


class QualityModule(Module):
    __application_provider = None

    def __init__(self, application_provider):
        self.__application_provider = application_provider

    def configure(self, binder):
        binder.bind(Application, to=self.__application_provider)
        binder.bind(BaseSettingsFile, to=InstanceProvider(UtilitiesModule.get_instance_of_settings_file()))
        binder.bind(Logger, to=InstanceProvider(getLogger()), scope=singleton)
        binder.bind(BaseLoggerConfiguration, to=ClassProvider(ConfigurationModule.get_logger_configuration()),
                    scope=singleton)
        binder.bind(BaseTimeoutConfiguration, to=ClassProvider(ConfigurationModule.get_timeout_configuration()),
                    scope=singleton)
        binder.bind(BaseRetryConfiguration, to=ClassProvider(ConfigurationModule.get_action_retry()),
                    scope=singleton)
        binder.bind(ElementCacheConfiguration, to=ClassProvider(ConfigurationModule.get_element_cache_configuration()),
                    scope=singleton)
        binder.bind(BaseLocalizationManager, to=ClassProvider(LocalizationModule.get_localization_manager()),
                    scope=singleton)
        binder.bind(BaseLocalizedLogger, to=ClassProvider(LocalizationModule.get_localization_logger()),
                    scope=singleton)
        binder.bind(ConditionalWait, to=ClassProvider(ConditionalWait))
