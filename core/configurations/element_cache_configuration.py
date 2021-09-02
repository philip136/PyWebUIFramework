from injector import inject

from core.utilities.base_settings_file import BaseSettingsFile


class ElementCacheConfiguration:
    __IS_ENABLED_PATH = "elementCache.isEnabled"

    @inject
    def __init__(self, settings_file: BaseSettingsFile) -> None:
        self.__is_enabled = bool(settings_file.is_value_present(self.__IS_ENABLED_PATH) and \
                                 settings_file.get_value(self.__IS_ENABLED_PATH))

    @property
    def is_enabled(self) -> bool:
        return self.__is_enabled
