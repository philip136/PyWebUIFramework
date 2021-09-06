from abc import ABC

from injector import Injector
from core.applications.base_application import BaseApplication
from core.applications.quality_module import QualityModule


class QualityServices(BaseApplication, ABC):
    __app = None
    __injector = None

    def __init__(self, application_provider, service_module):
        self._module = QualityModule(application_provider) if service_module is None else service_module
        self.__injector = Injector([self._module])

    @property
    def is_started(self):
        return self.__app.is_started if self.__app is not None else None

    @property
    def driver(self):
        return self.__app.driver if self.__app is not None else None

    def set_implicit_wait_timeout(self, timeout):
        pass

    @property
    def _is_app_started(self):
        return self.__app is not None and self.is_started

    def _set_app(self, application):
        self.__app = application

    def get_app(self, start_application_function):
        if not self._is_app_started:
            self._set_app(start_application_function())
        return self.__app

    def get_injector(self):
        return self.__injector
