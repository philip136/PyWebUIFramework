from injector import inject

from core.utilities.interfaces.settings_file_interface import ISettingsFile
from core.configurations.interfaces.retry_configuration_interface import IRetryConfiguration


class RetryConfiguration(IRetryConfiguration):
    @inject
    def __init__(self, settings_file: ISettingsFile):
        self._settings_file = settings_file
        
    @property
    def number(self) -> int:
        """Get the number of attempts to retry.
        :return: Number or attempts.
        :rtype: int.
        """
        return int(self._settings_file.get_value('retry.number'))

    @property
    def polling_interval(self) -> int:
        """Get the polling interval used in retry.
        :return: Timedelta for polling interval.
        :rtype: timedelta.
        """
        return self._settings_file.get_value('retry.pollingInterval')
