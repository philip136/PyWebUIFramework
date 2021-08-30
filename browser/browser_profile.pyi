import typing as ty
from logging import Logger

from driver_settings.driver_settings import DriverSettings

T = ty.TypeVar('T', bound=DriverSettings)



class BrowserProfile:
    def __init__(self, driver_settings: T, config_data: ty.Dict[str, ty.Any], logger: Logger) -> None:
        self._driver_settings = driver_settings
        self._config_data = config_data
        self._logger = logger

    @property
    def driver_settings(self) -> T:
        """Get driver settings
        :return: DriverSettings
        :rtype: T.
        """

    @property
    def browser_name(self) -> str:
        """Get browser name
        :return: Browser name.
        :rtype: str.
        """

    def is_remote(self) -> bool:
        """Check if is remote connection
        :return: Is remote connection or not?
        :rtype: bool.
        """

    def get_remote_connection_url(self) -> str:
        """Get remote connection url
        :return: Remote connection url.
        :rtype: str.
        """