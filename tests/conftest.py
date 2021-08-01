import pytest

from browser.py_services import PyServices


@pytest.fixture(scope='session')
def browser():
    """Getting browser instance and teardown connection after tests."""
    browser = PyServices.get_browser()
    yield browser
    browser.quit()
