from tests.constants import UrlConstants
from tests.utils.file_util import FileUtil
from tests.the_internet_forms.file_uploader_form import FileUploaderForm


class TestFileUploading:
    def test_uploading(self, browser):
        browser.go_to(f"{UrlConstants.THE_INTERNET}upload")

        file_uploader_form = FileUploaderForm()
        filename = file_uploader_form.filename
        filepath = FileUtil.get_target_file_path(filename)

        file_uploader_form.select_file(filepath)
        file_uploader_form.upload_file()

        uploaded_files = file_uploader_form.uploaded_files()
        assert uploaded_files.text == filename
