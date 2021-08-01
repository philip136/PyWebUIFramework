from browser.browser_profile import BrowserProfile


class Browser:
    __instance = None
    __browser_profile = BrowserProfile.get_driver_settings()

    def __new__(cls, *args, **kwargs):
        """Create singleton for browser."""
        if cls.__instance is None:
            cls.__instance = super(Browser, cls).__new__(cls)
        return cls.__instance

    def __init__(self, web_driver, web_driver_manager):
        """Create browser instance with settings from settings file.

        :param web_driver: WebDriver instance (Firefox, Chrome, ...).
        :param web_driver_manager: WebDriverManager.

        """
        self._executable_path = web_driver_manager().install()
        self._web_driver = web_driver(executable_path=self._executable_path,
                                      options=self.__browser_profile.get_capabilities())

    @property
    def browser_name(self):
        """Get browser name.

        :rtype: str.

        """
        return self._web_driver.name

    def go_to(self, url):
        """Get request.

        :param url: Url address for send GET request.

        """
        self._web_driver.get(url=url)

    def quit(self):
        """Close all tabs and terminates WebDriver session."""
        self._web_driver.quit()
