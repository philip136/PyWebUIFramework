from injector import inject

from src.core.utilities.interfaces.settings_file_interface import ISettingsFile


class ElementCacheConfiguration:
    __IS_ENABLED_PATH = "elementCache.isEnabled"

    @inject
    def __init__(self, settings_file: ISettingsFile) -> None:
        self.__is_enabled = bool(
            settings_file.is_value_present(self.__IS_ENABLED_PATH) and settings_file.get_value(self.__IS_ENABLED_PATH)
        )

    @property
    def is_enabled(self) -> bool:
        return self.__is_enabled
