from injector import inject
from logging import Logger

from src.core.localization.loggers.interfaces.localized_logger_interface import ILocalizedLogger
from src.core.localization.managers.interfaces.localization_interface import ILocalizationManager
from src.core.localization.configurations.interfaces.logger_configuration_interface import ILoggerConfiguration


class LocalizationLogger(ILocalizedLogger):
    @inject
    def __init__(self, localization_manager: ILocalizationManager, logger: Logger,
                 configuration: ILoggerConfiguration) -> None:
        """Initialize with localization manager and logger."""
        self._localization_manager = localization_manager
        self._configuration = configuration
        self._logger = logger
    
    def __localize_message(self, message_key: str, *message_args) -> str:
        """Get localization message from json file.
        :param message_key: Key in resource file.
        :param message_args: Arguments, which will be provided to template of localized message.
        :return: Required message for logging.
        :rtype: str.
        """
        return self._localization_manager.get_localized_message(message_key, *message_args)

    def info_element_action(self, element_type: str, element_name: str, message_key: str,
                            *message_args, **logger_kwargs) -> None:
        """Log localized message for action with INFO level which is applied for element.
        :param element_type: Type of the element.
        :param element_name: Name of the element.
        :param message_key: Key in resource file.
        :param message_args: Arguments, which will be provided to template of localized message.
        :param logger_kwargs: Arguments for logger.
        """
        message = f"{element_type} '{element_name}' :: {self.__localize_message(message_key, *message_args)}"
        self._logger.info(message, **logger_kwargs)

    def debug(self, message, *message_args, **logger_kwargs) -> None:
        """Log message with level debug.
        :param message: Message from resource file.
        :param message_args: Additional arguments for message.
        :param logger_kwargs: Additional arguments for logger.
        """
        self._logger.debug(self.__localize_message(message, *message_args))

    def info(self, message, *message_args, **logger_kwargs) -> None:
        """Log message with level info.
        :param message: Message from resource file.
        :param message_args: Additional arguments for message.
        :param logger_kwargs: Additional arguments for logger.
        """
        self._logger.info(self.__localize_message(message, *message_args))

    def warning(self, message, *message_args, **logger_kwargs) -> None:
        """Log message with level warning.
        :param message: Message from resource file.
        :param message_args: Additional arguments for message.
        :param logger_kwargs: Additional arguments for logger.
        """
        self._logger.warning(self.__localize_message(message, *message_args))

    def error(self, message, *message_args, **logger_kwargs) -> None:
        """Log message with level error.
        :param message: Message from resource file.
        :param message_args: Additional arguments for message.
        :param logger_kwargs: Additional arguments for logger.
        """
        self._logger.error(self.__localize_message(message, *message_args))

    def fatal(self, message, *message_args, **logger_kwargs) -> None:
        """Log message with level fatal.
        :param message: Message from resource file.
        :param message_args: Additional arguments for message.
        :param logger_kwargs: Additional arguments for logger.
        """
        self._logger.fatal(self.__localize_message(message, *message_args))

