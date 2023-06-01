import typing as ty

from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.remote.webdriver import WebDriver
from src.core.applications.interfaces.application_interface import IApplication
from src.core.configurations.interfaces.browser_profile_interface import IBrowserProfile
from src.core.localization.loggers.interfaces.localized_logger_interface import ILocalizedLogger
from src.core.configurations.interfaces.timeout_configuration_interface import ITimeoutConfiguration
from src.core.waitings.conditional_wait import ConditionalWait
from src.browser.browser_tab_navigation import BrowserTabNavigation
from src.browser.java_script import JavaScript
from src.browser.alert_actions import AlertActions

WD = ty.TypeVar('WD', bound=WebDriver)


class Browser(IApplication):
    def __init__(self, driver: WD, localized_logger: ILocalizedLogger, browser_profile: IBrowserProfile,
                 timeouts: ITimeoutConfiguration) -> None:
        self.__driver = driver
        self.__localized_logger = localized_logger
        self.__browser_profile = browser_profile
        self.__timeouts = timeouts
        self.__implicit_timeout = timeouts.implicit
        self.__conditional_wait = ConditionalWait(timeouts, self)
        self.__driver.implicitly_wait(self.__implicit_timeout)

    @property
    def browser_profile(self) -> IBrowserProfile:
        """Get browser profile instance.
        :return: BrowserProfile instance.
        :rtype: IBrowserProfile.
        """
        return self.__browser_profile

    @property
    def browser_profile(self):
        return self.__browser_profile

    @property
    def driver(self) -> WD:
        """Provides Selenium WebDriver instance for current browser session.
        :return: WebDriver manager.
        :rtype: WD.
        """
        return self.__driver

    @property
    def browser_name(self) -> str:
        """Get browser name.
        :return: Browser name.
        :rtype: str.
        """
        return self.__driver.name

    def maximize(self) -> None:
        """Executes browser window maximizing."""
        self.__localized_logger.info('loc.browser.maximize')
        self.__driver.maximize_window()

    def set_window_size(self, width: int, height: int) -> None:
        """Sets given window size.
        :param width: Desired window width.
        :param height: Desired window height.
        """
        self.__driver.set_window_size(width, height)

    @property
    def current_url(self) -> str:
        """Returns current page's URL.
        :return: Current page's URL.
        :rtype: str.
        """
        self.__localized_logger.warning('loc.browser.getUrl')
        url = self.driver.current_url
        self.__localized_logger.info('loc.browser.url.value', url)
        return url

    def go_to(self, url: str) -> None:
        """Executes navigating by passed URL."""
        self.__driver.get(url=url)

    def go_back(self) -> None:
        """Executes navigating back."""
        self.__driver.back()

    def go_forward(self) -> None:
        """Executes navigating forward."""
        self.__driver.forward()

    def refresh(self) -> None:
        """Executes refreshing of current page."""
        self.__driver.refresh()

    def execute_script(self, script, *args) -> ty.Any:
        """Executes JS (jQuery) script from the File.
        :param script: JavaScript.
        :param args: List of script arguments.
        :return: Result object of script execution.
        :rtype: object.
        """
        return self.__driver.execute_script(script, *args)

    @property
    def implicit_wait_timeout(self) -> int:
        """Get implicit wait timeout."""
        return self.__implicit_timeout

    def set_implicit_wait_timeout(self, timeout: int) -> None:
        """Sets web driver implicit wait timeout.
        :param timeout: Duration of time to wait.
        """
        self.__localized_logger.debug("loc.browser.implicit.timeout", timeout)
        self.__driver.implicitly_wait(timeout)

    def handle_alert(self, alert_action: ty.Union[AlertActions, str]) -> None:
        """Accepts or declines appeared alert.
        :param alert_action: Accept or decline.
        """
        alert_action = alert_action if isinstance(alert_action, str) else alert_action.value
        self.handle_promt_alert(alert_action, str())

    def handle_promt_alert(self, alert_action: ty.Union[AlertActions, str], text=str()) -> None:
        """ Accepts or declines prompt with sending message.
        :param alert_action: Accept or decline.
        :param text: Message to send.
        :raise NoAlertPresentException: Raise when switching to no presented alert.
        """
        alert_action = alert_action if isinstance(alert_action, str) else alert_action.value
        message_key = 'loc.browser.alert.%s' % alert_action
        self.__localized_logger.info(message_key)
        try:
            alert = self.__driver.switch_to.alert
            if text:
                self.__localized_logger.info('loc.send.text', text)
                alert.send_keys(text)

            if alert_action == 'accept':
                alert.accept()
            else:
                alert.dismiss()
        except NoAlertPresentException as e:
            self.__localized_logger.fatal('loc.browser.alert.fail', e)
            raise e

    def scroll_window_by(self, x: int, y: int) -> None:
        """Executes scrolling of the page to given coordinates x and y.
        :param x: Coordinate x.
        :param y: Coordinate y.
        """
        self.execute_script(JavaScript.SCROLL_WINDOW_BY.get_script(), x, y)

    def set_script_timeout(self, timeout: int) -> None:
        """Sets timeout to async javascript executions.
        :param timeout: Timeout in seconds.
        """
        self.__localized_logger.debug('loc.browser.script.timeout', timeout)
        self.__driver.set_script_timeout(timeout)

    def wait_for_page_to_load(self) -> None:
        """Waits until page is loaded.
        :raise TimeoutException: Will be thrown if page is not loaded during timeout.
        """
        self.__localized_logger.info('loc.browser.page.wait')
        self.__conditional_wait.wait_for(condition=lambda: self.execute_script(JavaScript.IS_PAGE_LOADED.get_script()),
                                         timeout=self.__timeouts.page_load,
                                         polling_interval=self.__timeouts.polling_interval)

        self.__localized_logger.localization_manager.get_localized_message('loc.browser.page.timeout')

    def switch_to_frame(self, element: WebElement) -> None:
        """Switch to iframe.
        :param element: IFrame element.
        """
        self.__driver.switch_to.frame(element)

    @property
    def tabs(self) -> BrowserTabNavigation:
        """Provides interface to manage of browser tabs.
        :return: Instance of BrowserTabNavigation.
        :rtype: BrowserTabNavigation.
        """
        return BrowserTabNavigation(self.__driver, self.__localized_logger, self)

    def quit(self) -> None:
        """Browser quit, closes all windows and dispose session."""
        self.__localized_logger.warning("loc.browser.driver.quit")
        self.__driver.quit()

    def get_screenshot(self, filename: str) -> bool:
        """Makes screenshot of the current page.
        :return: False if there is any IOError, else returns True.
        :rtype: bool.
        """
        return self.__driver.get_screenshot_as_file(filename)

    @property
    def is_started(self) -> bool:
        """Browser is started.
        :return: True if browser started else False.
        :rtype: bool.
        """
        return self.__driver.session_id is not None

    @property
    def download_directory(self) -> str:
        """Get path to download directory.
        :return: Path to download directory.
        :rtype: str.
        """
        return self.__browser_profile.get_driver_settings().get_download_dir()
