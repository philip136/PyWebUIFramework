from core.configurations.base_retry_configuration import BaseRetryConfiguration


class RetryConfiguration(BaseRetryConfiguration):
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
