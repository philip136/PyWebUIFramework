import os

from elements.label import Label
from browser.py_quality_services import PyQualityServices
from selenium.common.exceptions import WebDriverException


class FileUtil:
    @staticmethod
    def delete_file(path_to_file: str):
        if os.path.exists(path_to_file):
            os.remove(path_to_file)
        else:
            raise FileNotFoundError("File %s not found")

    @staticmethod
    def is_file_downloaded(file_address: str, label_file_content: Label):
        try:
            PyQualityServices.get_browser().go_to(file_address)
            return label_file_content.state.is_displayed
        except WebDriverException:
            return False

    @staticmethod
    def get_target_file_path(filename: str):
        download_dir = PyQualityServices.get_browser().download_directory
        dirs_split_by_sep = download_dir.split('/') if '/' in download_dir else download_dir.split('\\')
        dirs_name = [dir_name for dir_name in dirs_split_by_sep if dir_name != '']
        dirs_name.append(filename)
        return os.sep.join(dirs_name)

