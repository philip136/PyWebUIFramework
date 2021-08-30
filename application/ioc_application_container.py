import sys
import logging
from dependency_injector import containers, providers

from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.remote_connection import LOGGER
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from browser.browser_profile import BrowserProfile
from browser.browser import Browser
from driver_settings.chrome_driver_settings import ChromeDriverSettings
from driver_settings.firefox_driver_settings import FirefoxDriverSettings

from waitings.conditional_wait import ConditionalWait
from elements.element_finder import ElementFinder
from elements.element_factory import ElementFactory

from utilities.config_file import ConfigFile
from configurations.element_cache_configuration import ElementCacheConfiguration
from application.ioc_config_container import IocConfigContainer


class IoCApplicationContainer(containers.DeclarativeContainer):
    """IoC application container for WebUI Framework."""

    browser_name = IocConfigContainer.browser_name

    config_provider = providers.Configuration()
    config_provider.override({'browser_name': browser_name})

    options = providers.Selector(selector=config_provider.browser_name,
                                 chrome=providers.Singleton(ChromeOptions),
                                 firefox=providers.Singleton(FirefoxOptions))

    logger = providers.Singleton(LOGGER.__class__, name='PyServices logger')
    formatter = logging.Formatter('%(asctime)s | %(name)s |  %(levelname)s: %(message)s')
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(level=logging.DEBUG)
    logger().addHandler(stream_handler)

    driver_settings = providers.Selector(
        selector=config_provider.browser_name,
        chrome=providers.Singleton(ChromeDriverSettings, options=options),
        firefox=providers.Singleton(FirefoxDriverSettings, options=options))

    browser_profile = providers.Singleton(BrowserProfile, driver_settings=driver_settings)

    web_driver_manager = providers.Selector(selector=config_provider.browser_name,
                                            chrome=providers.Singleton(ChromeDriverManager),
                                            firefox=providers.Singleton(GeckoDriverManager))

    executable_path = web_driver_manager().install()
    capabilities = driver_settings().get_capabilities()
    web_driver = providers.Selector(
        selector=config_provider.browser_name,
        chrome=providers.Singleton(Chrome, executable_path=executable_path, options=capabilities),
        firefox=providers.Singleton(Firefox, executable_path=executable_path, options=capabilities))

    timeout_condition = ConfigFile.get_timeouts()['timeoutCondition']
    browser = providers.Singleton(Browser, web_driver=web_driver)
    conditional_wait = ConditionalWait(web_driver=web_driver())
    element_finder = providers.Singleton(ElementFinder, web_driver=web_driver, conditional_wait=conditional_wait)
    element_cache_configuration = ElementCacheConfiguration()
    element_factory = providers.Singleton(ElementFactory, conditional_wait=conditional_wait,
                                          element_finder=element_finder, logger=logger,
                                          element_cache_configuration=element_cache_configuration)
