from src.forms.base_form import BaseForm
from src.elements import Link
from selenium.webdriver.common.by import By


class FileDownloaderForm(BaseForm):
    __default_file_name = 'some-file.txt'
    __link_template = "//a[contains(@href,'%s')]"

    def __init__(self) -> None:
        super(FileDownloaderForm, self).__init__((By.ID, 'content'), 'File Downloader')

    def get_link_download(self, filename: str) -> Link:
        return self._get_element_factory().get_link((By.XPATH, self.__link_template % filename),
                                                    'Download file %s' % filename)

    @property
    def filename(self) -> str:
        return self.__default_file_name
