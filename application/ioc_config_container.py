import sys
import logging
from dependency_injector import containers, providers
from selenium.webdriver.remote.remote_connection import LOGGER

from utilities.config_file import ConfigFile


class IocConfigContainer(containers.DeclarativeContainer):
    config_file = providers.Singleton(ConfigFile)
    browser_name = config_file().get_browser_name()

    config_provider = providers.Configuration()
    config_provider.override({'browser_name': browser_name})

    logger = providers.Singleton(LOGGER.__class__, name='PyServices logger')
    formatter = logging.Formatter('%(asctime)s | %(name)s |  %(levelname)s: %(message)s')
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(level=logging.DEBUG)
    logger().addHandler(stream_handler)



