import os
from itertools import chain
from logging import Logger
from injector import inject

from core.localization.managers.interfaces.localization_interface import ILocalizationManager
from core.localization.configurations.interfaces.logger_configuration_interface import ILoggerConfiguration
from core.utilities.interfaces.settings_file_interface import ISettingsFile
from core.utilities.json_settings_file import JsonSettingsFile
from core.utilities.resource_file import ResourceFile


class LocalizationManager(ILocalizationManager):
    """This class is used for translation messages."""
    __resource_template = 'localization/%s'

    @inject
    def __init__(self, logger_configuration: ILoggerConfiguration, logger: Logger):
        self.__resource_name = self.__resource_template % logger_configuration.language
        self.__localization_file = self.__get_localization_file(f'{logger_configuration.language}.json')
        self.__logger = logger

    @staticmethod
    def __get_localization_file(filename: str) -> ISettingsFile:
        """Get localization file from core package or another.
        :param filename: Name of file.
        :rtype: ISettingsFile.
        """
        path = os.path.join('localization', filename)
        return JsonSettingsFile(path) if ResourceFile(path).exist else None

    def get_localized_message(self, message_key, *message_args) -> str:
        """Get localized message from resources.
        :param message_key: Key in resource file.
        :param message_args: Params which will be provided to template of localized message.

        :return: Localized message.
        :rtype: str.
        """
        key_in_json, localized_message = f'"{message_key}"', message_key
        if self.__localization_file and self.__localization_file.is_value_present(key_in_json):
            localized_message = self.__localization_file.get_value(key_in_json)
        else:
            self.__logger.warning('Cannot find localized message by key %s in resource file %s' % (
                key_in_json, self.__resource_name))
        message_args = tuple(chain(*message_args)) if len(message_args) > 1 else message_args
        return localized_message % message_args
