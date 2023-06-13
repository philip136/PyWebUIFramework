from injector import inject

from core.utilities.interfaces.settings_file_interface import ISettingsFile
from core.configurations.interfaces.timeout_configuration_interface import ITimeoutConfiguration


class TimeoutConfigurationCore(ITimeoutConfiguration):
    """Core class for setting timeouts."""
    @inject
    def __init__(self, settings_file: ISettingsFile):
        """Provides a SettingsFile to select the required configuration settings."""
        self._settings_file = settings_file

    @property
    def implicit(self) -> int:
        """Get WedDriver ImplicitWait timeout."""
        return self._get_config_value('timeouts.timeoutImplicit')

    @property
    def condition(self) -> int:
        """Get default ConditionalWait timeout."""
        return self._get_config_value("timeouts.timeoutCondition")

    @property
    def polling_interval(self) -> int:
        """Get ConditionalWait polling interval."""
        return self._get_config_value("timeouts.timeoutPollingInterval")

    @property
    def command(self) -> int:
        """Get WebDriver Command timeout."""
        return self._get_config_value("timeouts.timeoutCommand")
