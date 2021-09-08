import typing as ty
from abc import ABC

from injector import Injector
from core.applications.base_application import BaseApplication
from core.applications.quality_module import QualityModule

WD = ty.TypeVar('WD')


class QualityServices(BaseApplication, ABC):
    __app = None
    __injector = None

    def __init__(self, application_provider: BaseApplication, service_module: QualityModule) -> None:
        """Create QualityModule which bound core objects."""
        self._module = QualityModule(application_provider) if service_module is None else service_module
        self.__injector = Injector([self._module])

    @property
    def is_started(self) -> bool:
        """App is started or not.
        :return: True if app is started else False.
        :rtype: bool.
        """
        return self.__app.is_started if self.__app is not None else None

    @property
    def driver(self) -> ty.Optional[WD]:
        """Get driver.
        :return: Driver instance if app is started else None.
        :rtype: """
        return self.__app.driver if self.__app is not None else None

    # TODO: Определить более строгий интерфейс, так как данные метод реализуется только в сущности Browser
    def set_implicit_wait_timeout(self, timeout):
        pass

    @property
    def _is_app_started(self) -> bool:
        """App is started.
        :return: True if app is started else False.
        :rtype: bool.
        """
        return self.__app is not None and self.is_started

    def _set_app(self, application: BaseApplication) -> None:
        """Set application
        :param application: Class that implements the interface BaseApplication.
        """
        self.__app = application

    def get_app(self, start_application_function: ty.Callable) -> BaseApplication:
        """Get application, if app is not set then set using the install function.
        :param start_application_function: Function to install the app.
        :return: Instance of application.
        :rtype: BaseApplication.
        """
        if not self._is_app_started:
            self._set_app(start_application_function())
        return self.__app

    def get_injector(self) -> Injector:
        """Get injector instance.
        :return: Instance of injector.
        :rtype: Injector.
        """
        return self.__injector
