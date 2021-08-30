from abc import ABC
from dependency_injector.wiring import inject, Provide

from elements.state.desired_state import DesiredState
from application.ioc_config_container import IocConfigContainer


class ElementStateProvider(ABC):
    @inject
    def __init__(self, logger=Provide[IocConfigContainer.logger]):
        self._logger = logger

    @staticmethod
    def _element_is_enabled(element):
        return element.is_enabled()

    @staticmethod
    def _element_is_displayed(element):
        return element.is_displayed()

    def _element_enabled(self, element):
        return DesiredState(self._element_is_enabled(element), 'enabled').with_except_timeout_exception().\
            with_except_no_such_element_exceptions()

    def _element_not_enabled(self, element):
        return DesiredState(self._element_is_enabled(element) is not True, 'not.enabled').\
            with_except_timeout_exception().with_except_no_such_element_exceptions()

    def _element_clickable(self, element):
        return DesiredState(self._element_is_enabled(element) and self._element_is_displayed(), 'clickable')
