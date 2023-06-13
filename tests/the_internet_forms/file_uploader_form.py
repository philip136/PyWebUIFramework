from forms.base_form import BaseForm

from selenium.webdriver.common.by import By


class FileUploaderForm(BaseForm):
    __default_file_name = 'some-file.txt'

    def __init__(self) -> None:
        super(FileUploaderForm, self).__init__((By.ID, 'content'), 'File Uploader')

    def select_file(self, filename):
        choose_btn = self._element_factory.get_button((By.ID, 'file-upload'), 'Choice file')
        choose_btn.send_keys(filename)

    def upload_file(self) -> None:
        upload_btn = self._element_factory.get_button((By.ID, 'file-submit'), 'Upload')
        upload_btn.click()

    def uploaded_files(self):
        return self._element_factory.get_label((By.ID, 'uploaded-files'), 'Uploaded files')

    @property
    def filename(self) -> str:
        return self.__default_file_name
