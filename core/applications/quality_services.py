from abc import ABC

from injector import Injector

from core.applications.quality_module import QualityModule


class QualityServices(ABC):
    __app = None
    __injector = None

    def __init__(self, application_provider, services_module):
        self._module = QualityModule(application_provider)
        self.__injector = Injector([self._module])

    def _is_app_started(self):
        return self.__app is not None and self.__app.is_started()

    def _set_app(self, application):
        self.__app = application

    def get_app(self, application):
        if not self._is_app_started():
            self._set_app(application)
        return self.__app

    def get_injector(self):
        return self.__injector
