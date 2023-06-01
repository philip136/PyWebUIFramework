import os
from enum import Enum

from src.core.utilities.resource_file import ResourceFile


class JavaScript(Enum):
    IS_PAGE_LOADED = 'pageLoaded.js'
    CLICK_ELEMENT = 'clickElement.js'
    SET_VALUE = 'setValue.js'
    GET_ELEMENT_TEXT = 'getElementText.js.js'
    GET_CHECKBOX_STATE = 'getCheckBoxState.js'
    SCROLL_BY = 'scrollBy.js'
    SCROLL_WINDOW_BY = 'scrollWindowBy.js'
    OPEN_NEW_TAB = 'openNewTab.js'
    OPEN_IN_NEW_TAB = 'openInNewTab.js'
    BORDER_ELEMENT = 'borderElement.js'

    def __init__(self, filename):
        self.__filename = filename

    def get_script(self) -> str:
        script_path = os.path.join('js', self.__filename)
        resource_file = ResourceFile(script_path)
        return resource_file.file_content
