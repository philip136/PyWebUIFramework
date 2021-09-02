from core.localization.configurations.base_logger_configuration import BaseLoggerConfiguration


class LoggerConfiguration(BaseLoggerConfiguration):
    """Implementation for BaseLoggerConfiguration."""

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

