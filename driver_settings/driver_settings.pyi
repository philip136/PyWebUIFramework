import typing as ty
from logging import Logger
from abc import ABC, abstractmethod


T = ty.TypeVar('T')


class DriverSettings(ABC):
    """Abstract DriverSettings class. Setup capabilities, preferences and options for browser."""

    def __init__(self, options: T, config_data: ty.Dict[str, ty.Any], logger: Logger) -> None:
        self._options = options
        self._config_data = config_data
        self._logger = logger

    @property
    def browser_name(self) -> str:
        """Get browser name.
        :return: Browser name.
        :rtype: str.
        """

    @property
    def driver_settings_data(self) -> ty.Dict[str, ty.Any]:
        """Get dictionary with default driver settings.
        :return: Driver settings.
        :rtype: ty.Dict[str, ty.Any].
        """

    def get_capabilities(self) -> T:
        """Get and set preference, capabilities, arguments for browser.
        :return: ChromeOption, FirefoxOptions and etc with additional data.
        :rtype: T
        """

    @property
    def web_driver_version(self) -> str:
        """Get WebDriver version.
        :return: WebDriverVersion.
        :rtype: str.
        """

    @property
    def browser_options(self) -> ty.Dict[str, ty.Any]:
        """Get options.
        :return: Dictionary with options.
        :rtype: ty.Dict[str, ty.Any].
        """

    @property
    def browser_capabilities(self) -> ty.Dict[str, bool]:
        """Get capabilities.
        :return: Dictionary with capabilities.
        :rtype: ty.Dict[str, bool].
        """

    @property
    def browser_start_arguments(self) -> list:
        """Get arguments.
        :return: List with arguments.
        :rtype: list.
        """

    def _set_capabilities(self, options: T) -> None:
        """Set capabilities.
        :param options: Instance of ChromeOption, FirefoxOptions.
        """

    def _set_arguments(self, options: T) -> None:
        """Set arguments.
        :param options: Instance of ChromeOption, FirefoxOptions.
        """

    @abstractmethod
    def _set_preferences(self, options: T) -> None:
        """Abstract method for setup preferences."""