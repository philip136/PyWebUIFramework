from abc import ABC, abstractmethod


class DriverSettings(ABC):
    """Abstract DriverSettings class. Setup capabilities, preferences and options for browser."""

    def __init__(self, settings_file, options):
        """

        :param settings_file: Settings file for fetch settings data.
        :param options: ChromeOption, FirefoxOptions and etc.

        """
        self.__settings_file = settings_file
        self.__browser_name = self.__settings_file['browserName']
        self.__driver_settings = self.__settings_file['driverSettings'][self.__browser_name]
        self.__options = options()

    def get_capabilities(self):
        """Get and set preference, capabilities, arguments for browser.

        :return: ChromeOption, FirefoxOptions and etc with additional data.

        """
        self._set_capabilities(options=self.__options)
        self._set_preferences(options=self.__options)
        self._set_arguments(options=self.__options)
        return self.__options

    @property
    def web_driver_version(self):
        """Get WebDriver version.

        :return: WebDriverVersion.
        """
        return self.__driver_settings.get('webDriverVersion', 'latest')

    @property
    def browser_options(self):
        """Get options.

        :return: Dictionary with options.
        """
        return self.__driver_settings['options']

    @property
    def browser_capabilities(self):
        """Get capabilities.

        :return: Dictionary with capabilities.
        """
        return self.__driver_settings['capabilities']

    @property
    def browser_start_arguments(self):
        """Get arguments.

        :return: List with arguments.
        """
        return self.__driver_settings['startArguments']

    def _set_capabilities(self, options):
        """Set capabilities.

        :param options: Instance of ChromeOption, FirefoxOptions.
        """
        for key, val in self.browser_capabilities.items():
            options.set_capability(key, val)

    def _set_arguments(self, options):
        """Set arguments.

        :param options: Instance of ChromeOption, FirefoxOptions.
        """
        for argument in self.browser_start_arguments:
            options.add_argument(argument)

    @abstractmethod
    def _set_preferences(self, options):
        """Abstract method for setup preferences."""
        pass
