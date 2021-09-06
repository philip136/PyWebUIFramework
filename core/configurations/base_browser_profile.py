from abc import ABC, abstractmethod
from injector import inject

from core.utilities.base_settings_file import BaseSettingsFile
from core.localization.loggers.base_localized_logger import BaseLocalizedLogger


class BaseBrowserProfile(ABC):
    @inject
    def __init__(self, settings_file: BaseSettingsFile, logger: BaseLocalizedLogger) -> None:
        self.__settings_file = settings_file
        self.__logger = logger

    @property
    def settings_file(self):
        return self.__settings_file

    @property
    def browser_name(self) -> str:
        return self.__settings_file.get_value('browserName').lower()

    @property
    def is_remote(self) -> bool:
        return self.__settings_file.get_value('isRemote')

    @property
    def is_element_highlight_enabled(self) -> bool:
        return self.__settings_file.get_value('isElementHighlightEnabled')

    @abstractmethod
    def get_driver_settings(self):
        pass
