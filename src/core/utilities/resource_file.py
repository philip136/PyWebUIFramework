import os
import shutil
import typing as ty

from get_project_root import root_path


RESOURCE_DIR_NAME = "resources"


class ResourceFile:
    """Class which defines getting data from file."""

    def __init__(self, resource_name: str, root_dir: ty.Optional[str] = None):
        self.__resource_name = resource_name
        self.__root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) if root_dir is None else root_dir
        self.__resource_dir = self.__get_resource_dir_path()
        self.__path_to_file = self.get_resource_path(resource_name)

    def __get_resource_dir_path(self) -> str:
        """
        Get resource directory path, if your project has a folder named resources,
        then the files from the base package will be copied to your resource folder.
        :return: Path to resource directory.
        :rtype: str.
        """
        own_resource_dir = os.path.join(root_path(ignore_cwd=True), RESOURCE_DIR_NAME)
        default_resource_dir = os.path.join(self.__root_dir, RESOURCE_DIR_NAME)

        if os.path.isdir(own_resource_dir):
            for dir_path, dir_names, filenames in os.walk(default_resource_dir):
                destination_dir = dir_path.replace(default_resource_dir, own_resource_dir, 1)
                if not os.path.exists(destination_dir):
                    os.makedirs(destination_dir)

                for filename in filenames:
                    source_file = os.path.join(dir_path, filename)
                    destination_file = os.path.join(destination_dir, filename)
                    if os.path.exists(destination_file):
                        continue
                    shutil.copyfile(source_file, destination_file)
        return own_resource_dir if os.path.isdir(own_resource_dir) else default_resource_dir

    def get_resource_path(self, resource_name: str) -> str:
        """
        Get path to resource by its name.
        :param resource_name: Name of resource file with extension.
        :return: Path to resource.
        :rtype: Path.
        """
        return os.path.join(self.__resource_dir, resource_name)

    @property
    def exist(self) -> bool:
        """Check resource file exist or not.
        :return: Boolean value.
        :rtype: bool.
        """
        return os.path.exists(self.__path_to_file)

    @property
    def file_content(self) -> str:
        """Get file content.
        :return: File content as string.
        :rtype: str.
        """
        if not self.exist:
            self.__root_dir = root_path(ignore_cwd=True)
            self.__path_to_file = self.get_resource_path(self.__resource_name)

        with open(self.__path_to_file, mode='r', encoding='utf-8') as file_data:
            return file_data.read()

    @property
    def resource_name(self) -> str:
        """Get name of resource.
        :return: Name of resource file.
        :rtype: str.
        """
        return self.__resource_name
