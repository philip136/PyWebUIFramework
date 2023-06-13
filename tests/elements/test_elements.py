import pytest
import random

from tests.constants import UrlConstants
from browser.py_quality_services import PyQualityServices
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def accept_cookies(browser):
    browser.go_to(UrlConstants.LINK_W3SCHOOL)
    browser.wait_for_page_to_load()
    accept_btn = PyQualityServices.element_factory.get_button((By.ID, 'accept-choices'), 'AcceptCookies')
    accept_btn.state.wait_for_clickable()
    accept_btn.click()


@pytest.mark.usefixtures("accept_cookies")
class TestElements:
    element_factory = PyQualityServices.element_factory

    def test_check_box_element(self, browser):
        browser.go_to(UrlConstants.CHECK_BOX_W3SCHOOLS)
        iframe_element = self.element_factory.get_label((By.ID, 'iframeResult'), 'iFrameResult')
        browser.switch_to_frame(iframe_element)

        check_box_element = self.element_factory.get_check_box((By.ID, 'vehicle1'), 'VEHICLE1')
        default_state_of_check_box = check_box_element.is_checked()
        assert default_state_of_check_box is False, 'CheckBox element is checked'

        check_box_element.check()
        assert check_box_element.is_checked() is True, 'CheckBox element is not checked'

        check_box_element.uncheck()
        assert check_box_element.is_checked() is False, 'CheckBox element is checked'

    def test_button_element(self, browser):
        browser.go_to(UrlConstants.BUTTON_W3SCHOOLS)
        iframe_element = self.element_factory.get_label((By.ID, 'iframeResult'), 'iFrameResult')
        browser.switch_to_frame(iframe_element)

        button_element = self.element_factory.get_button(
            (By.XPATH, "//button[contains(text(),'Click Me!')]"), 'Click Me BUTTON')
        button_element.click()
        browser.handle_alert('accept')

    def test_link_element(self, browser):
        browser.go_to(UrlConstants.LINK_W3SCHOOL)

        iframe_element = self.element_factory.get_label((By.ID, 'iframeResult'), 'iFrameResult')
        browser.switch_to_frame(iframe_element)

        link_element = self.element_factory.get_link((By.XPATH, '//a[@href="https://www.w3schools.com/"]'), 'LINK')
        link_element.click()

        login_btn = self.element_factory.get_button((By.ID, 'w3loginbtn'), 'Login BUTTON AFTER CLICK ON LINK')
        login_btn.state.wait_for_clickable(timeout=10)

        assert login_btn.state.is_displayed is True, 'Login button is not displayed'

    def test_text_box_element(self, browser):
        browser.go_to(UrlConstants.TEXT_BOX_W3SCHOOL)
        iframe_element = self.element_factory.get_label((By.ID, 'iframeResult'), 'iFrameResult')
        browser.switch_to_frame(iframe_element)

        first_name_field = self.element_factory.get_text_box((By.ID, 'fname'), 'First Name')
        first_random_val, second_random_val = str(random.random()), str(random.random())

        first_name_field.type(first_random_val)
        assert first_name_field.value == first_random_val, 'Text box does not contain text %s' % first_random_val

        first_name_field.clear_and_type(second_random_val)
        assert first_name_field.value == second_random_val, 'Text box does not contain text %s' % second_random_val

    def test_radio_button(self, browser):
        browser.go_to(UrlConstants.RADIO_BUTTON_W3SCHOOL)
        iframe_element = self.element_factory.get_label((By.ID, 'iframeResult'), 'iFrameResult')
        browser.switch_to_frame(iframe_element)

        radio_button = self.element_factory.get_radio_button(
            (By.XPATH, '//input[@name="fav_language"]'), 'Radio Button')
        radio_button.click()

        assert radio_button.is_checked() is True, 'Radio Button is not checked'
