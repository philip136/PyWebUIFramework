from abc import ABC, abstractmethod
from logging import Logger

from injector import inject
from core.localization.managers.base_localization_manager import BaseLocalizationManager
from core.localization.configurations.base_logger_configuration import BaseLoggerConfiguration


class BaseLocalizedLogger(ABC):
    """Log messages in current language."""

    @inject
    def __init__(self, localization_manager: BaseLocalizationManager, logger: Logger,
                 configuration: BaseLoggerConfiguration) -> None:
        """Initialize with localization manager and logger."""
        self.__localization_manager = localization_manager
        self.__configuration = configuration
        self._logger = logger

    @abstractmethod
    def info_element_action(self, element_type: str, element_name: str, message_key: str,
                            *message_args, **logger_kwargs) -> None:
        """Log localized message for action with INFO level which is applied for element.
        :param element_type: Type of the element.
        :param element_name: Name of the element.
        :param message_key: Key in resource file.
        :param message_args: Arguments, which will be provided to template of localized message.
        :param logger_kwargs: Arguments for logger.
        """
        pass

    @property
    def configuration(self) -> BaseLoggerConfiguration:
        """Get logger configuration."""
        return self.__configuration

    @abstractmethod
    def info(self, message_key: str, *message_args, **logger_kwargs) -> None:
        """
        Log localized message with INFO level.
        :param message_key: Key in resource file.
        :param message_args: Arguments, which will be provided to template of localized message.
        :param logger_kwargs: Arguments for logger.
        """
        pass

    @abstractmethod
    def debug(self, message_key: str, *message_args, **logger_kwargs) -> None:
        """
        Log localized message with DEBUG level.
        :param message_key: Key in resource file.
        :param message_args: Arguments, which will be provided to template of localized message.
        :param logger_kwargs: Arguments for logger.
        """
        pass

    @abstractmethod
    def warning(self, message_key: str, *message_args, **logger_kwargs) -> None:
        """
        Log localized message with WARN level.
        :param message_key: Key in resource file.
        :param message_args: Arguments, which will be provided to template of localized message.
        :param logger_kwargs: Arguments for logger.
        """
        pass

    @abstractmethod
    def error(self, message_key: str, *message_args, **logger_kwargs) -> None:
        """
        Log localized message with ERROR level.
        :param message_key: Key in resource file.
        :param message_args: Arguments, which will be provided to template of localized message.
        :param logger_kwargs: Arguments for logger.
        """
        pass

    @abstractmethod
    def fatal(self, message_key: str, *message_args, **logger_kwargs) -> None:
        """
        Log localized message with FATAL(exception) level.
        :param message_key: Key in resource file.
        :param message_args: Arguments, which will be provided to template of localized message.
        :param logger_kwargs: Arguments for logger.
        """
        pass
