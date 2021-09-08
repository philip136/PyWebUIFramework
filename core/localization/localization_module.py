from core.localization.managers.localization_manager import LocalizationManager
from core.localization.loggers.localized_logger import LocalizationLogger


class LocalizationModule:
    @staticmethod
    def get_localization_manager():
        return LocalizationManager

    @staticmethod
    def get_localization_logger():
        return LocalizationLogger
