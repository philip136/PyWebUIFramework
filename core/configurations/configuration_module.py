from core.configurations.element_cache_configuration import ElementCacheConfiguration
from core.localization.configurations.logger_configuration import LoggerConfiguration
from core.configurations.retry_configuration import RetryConfiguration
from core.configurations.timeout_configuration import TimeoutConfiguration


class ConfigurationModule:
    @staticmethod
    def get_element_cache_configuration():
        return ElementCacheConfiguration

    @staticmethod
    def get_logger_configuration():
        return LoggerConfiguration

    @staticmethod
    def get_action_retry():
        return RetryConfiguration

    @staticmethod
    def get_timeout_configuration():
        return TimeoutConfiguration
