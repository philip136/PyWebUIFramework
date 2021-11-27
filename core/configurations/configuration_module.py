import typing as ty

from core.configurations.element_cache_configuration import ElementCacheConfiguration
from core.localization.configurations.logger_configuration import LoggerConfiguration
from core.configurations.retry_configuration import RetryConfiguration
from core.configurations.timeout_configuration import TimeoutConfigurationCore


class ConfigurationModule:
    @staticmethod
    def get_element_cache_configuration() -> ty.Type[ElementCacheConfiguration]:
        """Get element cache configuration class for further injection.
        :return: ElementCacheConfiguration class.
        :rtype: ElementCacheConfiguration.
        """
        return ElementCacheConfiguration

    @staticmethod
    def get_logger_configuration() -> ty.Type[LoggerConfiguration]:
        """Get logger configuration configuration for further injection.
        :return: ElementCacheConfiguration class.
        :rtype: ElementCacheConfiguration.
        """
        return LoggerConfiguration

    @staticmethod
    def get_action_retry() -> ty.Type[RetryConfiguration]:
        """"Get retry configuration for further injection.
        :return: RetryConfiguration class.
        :rtype: RetryConfiguration.
        """
        return RetryConfiguration

    @staticmethod
    def get_timeout_configuration() -> ty.Type[TimeoutConfigurationCore]:
        """Get timeout configuration for further injection.
        :return: TimeoutConfigurationCore class.
        :rtype: TimeoutConfigurationCore.
        """
        return TimeoutConfigurationCore
