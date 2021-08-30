from dependency_injector.wiring import inject, Provide
from application.ioc_config_container import IocConfigContainer


class Browser:
    @inject
    def __init__(self, web_driver, logger=Provide[IocConfigContainer.logger]):
        self._web_driver = web_driver
        self._logger = logger

    @property
    def browser_name(self):
        return self._web_driver.name

    def maximize(self):
        self._logger.info('Start browser with maximize size')
        self._web_driver.maximize_window()

    def go_to(self, url: str):
        self._logger.info(f'WebDriver sending request to {url}')
        self._web_driver.get(url=url)

    def go_back(self):
        self._web_driver.back()

    def refresh(self):
        self._web_driver.refresh()

    def go_forward(self):
        self._web_driver.forward()

    def quit(self):
        self._logger.info('WebDriver quit')
        self._web_driver.quit()

    def execute_script(self, script, *arguments):
        return self._web_driver.execute_script(script=script, *arguments)
