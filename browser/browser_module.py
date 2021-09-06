from injector import ClassProvider, singleton, InstanceProvider

from core.applications.quality_module import QualityModule
from core.configurations.base_browser_profile import BaseBrowserProfile
from core.configurations.element_cache_configuration import ElementCacheConfiguration
from core.elements.base_element_factory import BaseElementFactory
from elements.element_factory import ElementFactory


class BrowserModule(QualityModule):
    def configure(self, binder):
        super(BrowserModule, self).configure(binder)
        binder.bind(BaseBrowserProfile, to=ClassProvider(ElementCacheConfiguration), scope=singleton)
        binder.bind(BaseElementFactory, to=InstanceProvider(ElementFactory))
