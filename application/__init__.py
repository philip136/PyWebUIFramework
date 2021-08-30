from browser import browser
from browser import browser_profile
from driver_settings import driver_settings
from driver_settings import chrome_driver_settings, firefox_driver_settings
from elements import element_finder
from configurations import element_cache_configuration
from elements import element_factory
from waitings import conditional_wait
from elements.state import element_state_provider

from application.ioc_config_container import IocConfigContainer

config_container = IocConfigContainer()

config_container.wire(modules=[browser, browser_profile, driver_settings, element_finder, element_cache_configuration,
                               element_factory, chrome_driver_settings, firefox_driver_settings, conditional_wait,
                               element_state_provider])


