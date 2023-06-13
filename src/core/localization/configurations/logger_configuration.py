from injector import inject

from core.utilities.interfaces.settings_file_interface import ISettingsFile
from core.localization.configurations.interfaces.logger_configuration_interface import ILoggerConfiguration


class LoggerConfiguration(ILoggerConfiguration):
    """Implementation for ILoggerConfiguration."""

    @inject
    def __init__(self, settings_file: ISettingsFile):
        self._settings_file = settings_file

    @property
    def language(self) -> str:
        """Get language of framework.
        :return: Language.
        :rtype: str.
        """
        return str(self._settings_file.get_value_or_default("logger.language", "en"))

    @property
    def log_page_source(self) -> bool:
        """Perform page source logging in case of catastrophic failures or not.
        :return: Perform page source or not.
        :rtype: bool.
        """
        return bool(self._settings_file.get_value_or_default('logger.logPageSource', True))
