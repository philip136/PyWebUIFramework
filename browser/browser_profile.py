from dependency_injector.wiring import inject, Provide
from application.ioc_config_container import IocConfigContainer


class BrowserProfile:
    @inject
    def __init__(self, driver_settings, config_data=Provide[IocConfigContainer.config_file],
                 logger=Provide[IocConfigContainer.logger]):
        self._driver_settings = driver_settings
        self._config_data = config_data
        self._logger = logger

    @property
    def driver_settings(self):
        return self._driver_settings

    @property
    def browser_name(self):
        return self._config_data['browserName'].lower()

    def is_remote(self):
        browser_is_remote = self._config_data['isRemote']
        self._logger.info(f'Browser is remote: {browser_is_remote}')
        return browser_is_remote

    def get_remote_connection_url(self):
        connection_url = self._config_data['remoteConnectionUrl']
        self._logger.info(f'Remote connection url: {connection_url}')
        return connection_url
