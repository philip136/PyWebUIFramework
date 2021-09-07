from core.configurations.base_timeout_configuration import BaseTimeoutConfiguration


class TimeoutConfigurationCore(BaseTimeoutConfiguration):
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

