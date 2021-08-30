from dependency_injector.wiring import inject, Provide

from application.ioc_config_container import IocConfigContainer


class ElementCacheConfiguration:
    __is_enabled = False

    @inject
    def __init__(self, config_data=Provide[IocConfigContainer.config_file]):
        self.__is_enabled = config_data.read_from_json_file()['elementCache']['isEnabled']

    @property
    def is_enabled(self):
        return self.__is_enabled

