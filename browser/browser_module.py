from injector import ClassProvider, singleton

from core.applications.quality_module import QualityModule
from core.configurations.base_browser_profile import BaseBrowserProfile
from core.configurations.element_cache_configuration import ElementCacheConfiguration


class BrowserModule(QualityModule):
    def configure(self, binder):
        super(BrowserModule, self).configure(binder)
        binder.bind(BaseBrowserProfile, to=ClassProvider(ElementCacheConfiguration),
                    scope=singleton)
