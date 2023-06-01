import typing as ty

from injector import Injector
from src.core.applications.interfaces.application_interface import IApplication
from src.core.applications.quality_module import QualityModule

WD = ty.TypeVar('WD')


class QualityServices(IApplication):
    __app = None
    __injector = None

    def __init__(self, application_provider: ty.Callable[..., IApplication],
                 service_module: QualityModule) -> None:
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
        :rtype: Optional[WD].
        """
        return self.__app.driver if self.__app is not None else None

    @property
    def _is_app_started(self) -> bool:
        """App is started.
        :return: True if app is started else False.
        :rtype: bool.
        """
        return self.__app is not None and self.is_started

    def _set_app(self, application: IApplication) -> None:
        """Set application
        :param application: Class that implements the interface IApplication.
        """
        self.__app = application

    def get_app(self, start_application_function: ty.Callable) -> IApplication:
        """Get application, if app is not set then set using the install function.
        :param start_application_function: Function to install the app.
        :return: Instance of application.
        :rtype: IApplication.
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
