import logging
import typing as ty

from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


T = ty.TypeVar('T', bound=RemoteWebDriver)

class Browser:
    def __init__(self, web_driver: T, logger: logging.Logger) -> None:
        self._web_driver = web_driver
        self._logger = logger

    @property
    def browser_name(self) -> str:
        """Get browser name.

        :return: Browser name.
        :rtype: str.
        """

    def maximize(self) -> None:
        """Maximizes the current window."""

    def go_to(self, url: str) -> None:
        """Get request.

        :param url: Url address for send GET request.
        """

    def go_back(self) -> None:
        """Goes one step back in the browser history."""

    def refresh(self) -> None:
        """Refreshes the current page."""

    def go_forward(self) -> None:
        """Goes one step forward in the browser history."""

    def quit(self) -> None:
        """Close all tabs and terminates WebDriver session."""

    def execute_script(self, script: str, *arguments: ty.Any) -> dict:
        """Execute JavaScript.

        :param script: JavaScript.
        :param arguments: Arguments for js script.
        :return: Dictionary with response data.
        """