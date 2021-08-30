from application.ioc_application_container import IoCApplicationContainer


class PyServices:
    __ioc_container = IoCApplicationContainer

    @classmethod
    def get_browser(cls):
        return cls.__ioc_container.browser()

    @classmethod
    def get_element_factory(cls):
        return cls.__ioc_container.element_factory()

    @classmethod
    def get_element_finder(cls):
        return cls.__ioc_container.element_finder()

    @classmethod
    def get_logger(cls):
        return cls.__ioc_container.logger()

    @classmethod
    def get_config_data(cls):
        return cls.__ioc_container.config_data
