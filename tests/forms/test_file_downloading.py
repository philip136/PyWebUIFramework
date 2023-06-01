import os

from src.browser.py_quality_services import PyQualityServices
from selenium.webdriver.common.by import By
from tests.the_internet_forms.file_downloader_form import FileDownloaderForm
from tests.utils.file_util import FileUtil
from tests.constants import UrlConstants


class TestFileDownloading:
    def test_downloading(self, browser):
        browser.go_to(UrlConstants.THE_INTERNET + 'download')

        downloader_form = FileDownloaderForm()
        filename = downloader_form.filename
        filepath = FileUtil.get_target_file_path(filename)

        file = open(filepath, mode='w')
        file.close()

        FileUtil.delete_file(filepath)

        file_address = f'file:{os.sep}{filepath}'
        label_file_content = PyQualityServices.get_element_factory().get_label((By.XPATH, '//pre'), 'text file content')
        downloader_form.get_link_download(filename).js_action.click_and_wait()

        assert PyQualityServices.get_conditional_wait().wait_for(lambda: FileUtil.is_file_downloaded(
            file_address, label_file_content), timeout=10) is True, 'File %s should be downloaded' % filename
