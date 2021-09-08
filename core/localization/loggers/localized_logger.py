from core.localization.loggers.base_localized_logger import BaseLocalizedLogger


class LocalizationLogger(BaseLocalizedLogger):
    def __localize_message(self, message_key: str, *message_args) -> str:
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
        self._logger.debug(self.__localize_message(message, *message_args))

    def info(self, message, *message_args, **logger_kwargs) -> None:
        self._logger.info(self.__localize_message(message, *message_args))

    def warning(self, message, *message_args, **logger_kwargs) -> None:
        self._logger.warning(self.__localize_message(message, *message_args))

    def error(self, message, *message_args, **logger_kwargs) -> None:
        self._logger.error(self.__localize_message(message, *message_args))

    def fatal(self, message, *message_args, **logger_kwargs) -> None:
        self._logger.fatal(self.__localize_message(message, *message_args))

