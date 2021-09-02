import os
from injector import inject

from core.localization.managers.base_localization_manager import BaseLocalizationManager
from core.localization.configurations.base_logger_configuration import BaseLoggerConfiguration
from core.utilities.base_settings_file import BaseSettingsFile
from core.utilities.json_settings_file import JsonSettingsFile
from core.utilities.resource_file import ResourceFile


class LocalizationManager(BaseLocalizationManager):
    """Implementation for BaseLocalizationManager."""

    @inject
    def __init__(self, logger_configuration: BaseLoggerConfiguration):
        language = logger_configuration.language
        self.__core_localization_file = self.__get_localization_file(f'core.{language}.json')
        self.__localization_file = self.__get_localization_file(f'{language}.json')

    @staticmethod
    def __get_localization_file(filename: str) -> BaseSettingsFile:
        path = os.path.join('localization', filename)
        return JsonSettingsFile(path) if ResourceFile(path).is_exist else None

    def get_localized_message(self, message_key, *message_args) -> str:
        """Get localized message from resources.
        :param message_key: Key in resource file.
        :param message_args: Params which will be provided to template of localized message.

        :return: Localized message.
        :rtype: str.
        """
        json_path = f'"{message_key}"'
        localized_message = message_key
        if self.__localization_file and self.__localization_file.is_value_present(json_path):
            localized_message = self.__localization_file.get_value(json_path)
        elif self.__core_localization_file.is_value_present(json_path):
            localized_message = self.__core_localization_file.get_value(json_path)
        return localized_message % message_args
