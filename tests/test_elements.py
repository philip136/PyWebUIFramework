from tests.constants import UrlConstants

from browser.py_quality_services import PyQualityServices
from selenium.webdriver.common.by import By


class TestElements:
    def test_check_box_element(self, browser):
        browser.go_to(UrlConstants.CHECK_BOX_W3SCHOOLS)
        iframe_element = PyQualityServices.get_element_factory().get_label((By.ID, 'iframeResult'), 'iFrameResult')
        browser.switch_to_frame(iframe_element.get_element())

        check_box_element = PyQualityServices.get_element_factory().get_check_box((By.ID, 'vehicle1'), 'VEHICLE1')
        default_state_of_check_box = check_box_element.is_checked()
        assert default_state_of_check_box is False

        check_box_element.check()
        assert check_box_element.is_checked() is True

        check_box_element.uncheck()
        assert check_box_element.is_checked() is False

    def test_button_element(self, browser):
        browser.go_to(UrlConstants.BUTTON_W3SCHOOLS)
        iframe_element = PyQualityServices.get_element_factory().get_label((By.ID, 'iframeResult'), 'iFrameResult')
        browser.switch_to_frame(iframe_element.get_element())

        button_element = PyQualityServices.get_element_factory().get_button(
            (By.XPATH, "//button[contains(text(),'Click Me!')]"), 'Click Me BUTTON')
        button_element.click()
        browser.handle_alert('accept')

    def test_link_element(self, browser):
        browser.go_to(UrlConstants.LINK_W3SCHOOL)
        iframe_element = PyQualityServices.get_element_factory().get_label((By.ID, 'iframeResult'), 'iFrameResult')
        browser.switch_to_frame(iframe_element.get_element())

        link_element = PyQualityServices.get_element_factory().get_link(
            (By.XPATH, '//a[@href="https://www.w3schools.com/"]'), 'LINK')

        link_element.click()

        login_btn = PyQualityServices.get_element_factory().get_button(
            (By.ID, 'w3loginbtn'), 'Login BUTTON AFTER CLICK ON LINK')

        assert login_btn.state.is_displayed is True
