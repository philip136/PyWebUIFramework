from dependency_injector.wiring import inject, Provide

from elements.element_type import ElementType
from elements.element_state import ElementState
from application.ioc_config_container import IocConfigContainer


class ElementFactory:
    @inject
    def __init__(self, conditional_wait, element_finder, element_cache_configuration,
                 logger=Provide[IocConfigContainer.logger]):
        self._conditional_wait = conditional_wait
        self._element_finder = element_finder
        self._logger = logger
        self._element_cache_configuration = element_cache_configuration

    def __get_element(self, element_type, locator, name, state):
        return self.__get_custom_element(element_type.value, locator, name, state)

    def __get_custom_element(self, element_class, locator, name, state):
        return element_class(element_finder=self._element_finder,
                             element_cache_configuration=self._element_cache_configuration,
                             logger=self._logger, locator=locator, name=name, state=state).get_element(
            self._conditional_wait.timeout)

    def get_button(self, locator, name, state=ElementState.EXISTS_IN_ANY_STATE.value):
        return self.__get_element(ElementType.BUTTON, locator, name, state)
