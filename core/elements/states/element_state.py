from selenium.webdriver.remote.webelement import WebElement


class ExistsInAnyState:
    """Determines any element's state."""

    def __call__(self, element: WebElement):
        """Return True in any case."""
        return True

    def __repr__(self):
        return "Element is exist in any state"


class Displayed:
    """Determines element's displayed state."""

    def __call__(self, element: WebElement):
        """Return true if elements is displayed and false otherwise."""
        return element.is_displayed()

    def __repr__(self):
        return "Element is displayed"
