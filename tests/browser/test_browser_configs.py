from tests.constants import UrlConsts, TitleConsts


class TestBrowserConfigs:
    def test_browser_request(self, browser):
        browser.go_to(url=UrlConsts.GOOGLE)
        assert browser._web_driver.title == TitleConsts.GOOGLE
