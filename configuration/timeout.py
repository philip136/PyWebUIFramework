from enum import Enum


class Timeout(Enum):
    """Enum timeouts."""

    SCRIPT = 'timeoutScript'
    PAGE_LOAD = 'timeoutPageLoad'
