import typing as ty

from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from core.applications.base_application import BaseApplication
from core.configurations.base_browser_profile import BaseBrowserProfile
from core.localization.loggers.base_localized_logger import BaseLocalizedLogger
from core.waitings.conditional_wait import ConditionalWait
from configuration.timeout_configuration import TimeoutConfiguration
from browser.browser_tab_navigation import BrowserTabNavigation
from browser.java_script import JavaScript
from browser.alert_actions import AlertActions

WD = ty.TypeVar('WD', bound=RemoteWebDriver)


class Browser(BaseApplication):
    def __init__(self, driver: WD, logger: BaseLocalizedLogger, browser_profile: BaseBrowserProfile,
                 timeouts: TimeoutConfiguration) -> None:
        self.__driver = driver
        self.__logger = logger
        self.__browser_profile = browser_profile
        self.__timeouts = timeouts
        self.__implicit_timeout = timeouts.implicit
        self.__conditional_wait = ConditionalWait(timeouts, self)
        self.driver.implicitly_wait(self.__implicit_timeout)

    @property
    def driver(self):
        return self.__driver

    @property
    def browser_name(self):
        return self.__driver.name

    def maximize(self):
        self.__logger.info('loc.browser.maximize')
        self.__driver.maximize_window()

    def set_window_size(self, width: int, height: int):
        self.__driver.set_window_size(width, height)

    @property
    def current_url(self):
        self.__logger.warning('loc.browser.getUrl')
        url = self.driver.current_url
        self.__logger.info('loc.browser.url.value', url)
        return url

    def go_to(self, url: str):
        self.__driver.get(url=url)

    def go_back(self):
        self.__driver.back()

    def refresh(self):
        self.__driver.refresh()

    def go_forward(self):
        self.__driver.forward()

    def execute_script(self, script, *args):
        return self.__driver.execute_script(script, *args)

    @property
    def implicit_wait_timeout(self):
        return self.__implicit_timeout

    def handle_alert(self, alert_action: str):
        self.handler_promt_alert(alert_action, str())

    def handler_promt_alert(self, alert_action, text=str()):
        message_key = 'loc.browser.alert.%s' % alert_action
        self.__logger.info(message_key)
        try:
            alert = self.__driver.switch_to.alert
            if text:
                self.__logger.info('loc.send.text', text)
                alert.send_keys(text)

            if alert_action == 'accept':
                alert.accept()
            else:
                alert.dismiss()
        except NoAlertPresentException as e:
            self.__logger.fatal('loc.browser.alert.fail', e)
            raise e

    def scroll_window_by(self, x: int, y: int):
        self.execute_script(JavaScript.SCROLL_WINDOW_BY.get_script(), x, y)

    def set_implicit_wait_timeout(self, timeout: int):
        self.__logger.debug("loc.browser.implicit.timeout", timeout)
        self.__driver.implicitly_wait(timeout)

    def set_script_timeout(self, timeout: int):
        self.__logger.debug('loc.browser.script.timeout', timeout)
        self.__driver.set_script_timeout(timeout)

    def wait_for_page_to_load(self):
        self.__logger.info('loc.browser.page.wait')
        self.__conditional_wait.wait_for(
            condition=lambda: self.execute_script(JavaScript.IS_PAGE_LOADED.get_script()),
            timeout=self.__timeouts.page_load, polling_interval=self.__timeouts.polling_interval)

        self.__logger.localization_manager.get_localized_message('loc.browser.page.timeout')

    def switch_to_frame(self, element):
        self.__driver.switch_to.frame(element)

    @property
    def tabs(self):
        return BrowserTabNavigation(self.__driver, self.__logger)

    def quit(self):
        self.__logger.warning("loc.browser.driver.quit")
        self.__driver.quit()

    @property
    def is_started(self):
        return self.__driver.session_id is not None

    @property
    def download_directory(self):
        return self.__browser_profile.get_driver_settings().get_download_dir()
