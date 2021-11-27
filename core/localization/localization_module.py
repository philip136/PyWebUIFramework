import typing as ty

from core.localization.managers.interfaces.localization_interface import ILocalizationManager
from core.localization.loggers.interfaces.localized_logger_interface import ILocalizedLogger
from core.localization.managers.localization_manager import LocalizationManager
from core.localization.loggers.localized_logger import LocalizationLogger


class LocalizationModule:
    @staticmethod
    def get_localization_manager() -> ty.Type[ILocalizationManager]:
        """Get localization manager.
        :return: LocalizationManager class.
        :rtype: ty.Type[ILocalizationManager].
        """
        return LocalizationManager

    @staticmethod
    def get_localization_logger() -> ty.Type[ILocalizedLogger]:
        """Get localized logger.
        :return: LocalizedLogger class.
        :rtype: ty.Type[ILocalizedLogger].
        """
        return LocalizationLogger
