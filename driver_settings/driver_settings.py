from abc import ABC, abstractmethod

from dependency_injector.wiring import inject, Provide
from application.ioc_config_container import IocConfigContainer


class DriverSettings(ABC):
    @inject
    def __init__(self, options, config_file=Provide[IocConfigContainer.config_file],
                 logger=Provide[IocConfigContainer.logger]):
        self._options = options
        self._config_data = config_file.read_from_json_file()
        self._logger = logger

    @property
    def browser_name(self):
        return self._config_data['browserName']

    @property
    def driver_settings_data(self):
        return self._config_data['driverSettings'][self.browser_name]

    def get_capabilities(self):
        self._set_capabilities(options=self._options)
        self._set_preferences(options=self._options)
        self._set_arguments(options=self._options)
        return self._options

    @property
    def web_driver_version(self):
        return self.driver_settings_data.get('webDriverVersion', 'latest')

    @property
    def browser_options(self):
        return self.driver_settings_data['options']

    @property
    def browser_capabilities(self):
        return self.driver_settings_data['capabilities']

    @property
    def browser_start_arguments(self):
        return self.driver_settings_data['startArguments']

    def _set_capabilities(self, options):
        for key, val in self.browser_capabilities.items():
            options.set_capability(key, val)

    def _set_arguments(self, options):
        for argument in self.browser_start_arguments:
            options.add_argument(argument)

    @abstractmethod
    def _set_preferences(self, options):
        pass
