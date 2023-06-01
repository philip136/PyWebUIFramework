import typing as ty
from abc import ABC, abstractmethod

from core.elements.states.element_state import Displayed, ExistsInAnyState
from core.localization.managers.interfaces.localization_interface import ILocalizationManager
from core.localization.configurations.interfaces.logger_configuration_interface import ILoggerConfiguration


class ILocalizedLogger(ABC):
    """Log messages in current language."""
    _localization_manager: ILocalizationManager = NotImplemented
    _configuration: ILoggerConfiguration = NotImplemented

    @abstractmethod
    def info_element_action(self, element_type: ty.Type[ty.Union[Displayed, ExistsInAnyState]],
                            element_name: str, message_key: str, *message_args, **logger_kwargs) -> None:
        """Log localized message for action with INFO level which is applied for element.
        :param element_type: Type of the element.
        :param element_name: Name of the element.
        :param message_key: Key in resource file.
        :param message_args: Arguments, which will be provided to template of localized message.
        :param logger_kwargs: Arguments for logger.
        """
        pass

    @property
    def localization_manager(self) -> ILocalizationManager:
        """Get instance of localization manager.
        :return: Instance of LocalizationManager.
        :rtype: ILocalizationManager.
        """
        return self._localization_manager

    @property
    def configuration(self) -> ILoggerConfiguration:
        """Get logger configuration.
        :return: Instance of logger configuration.
        :rtype: ILoggerConfiguration.
        """
        return self._configuration

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
