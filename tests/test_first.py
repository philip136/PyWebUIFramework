from browser.py_quality_services import PyQualityServices

from selenium.webdriver.common.by import By

def test_1():
    browser = PyQualityServices.get_browser()
    browser.maximize()
    browser.wait_for_page_to_load()
    browser.go_to('https://store.steampowered.com/')

    btn = PyQualityServices.get_element_factory().get_button((By.XPATH, "//a[@class='pulldown_desktop']"), 'BTN')
    btn.click()
    browser.quit()




