import pytest
from src.browser.py_quality_services import PyQualityServices


@pytest.fixture(scope='session')
def browser():
    browser = PyQualityServices.get_browser()
    browser.maximize()
    yield browser
    browser.quit()
