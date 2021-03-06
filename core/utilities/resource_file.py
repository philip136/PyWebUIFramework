import os
import typing as ty

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ResourceFile:
    """Class which defines getting data from file."""

    def __init__(self, resource_name: str, root_dir: ty.Optional[str] = None):
        self.__resource_name = resource_name
        self.__root_dir = ROOT_DIR if root_dir is None else root_dir
        self.__path_to_file = self.get_resource_path(resource_name)

    def get_resource_path(self, resource_name: str):
        """
        Get path to resource by its name.
        :param resource_name: Name of resource file with extension.
        :return: Path to resource.
        :rtype: Path.
        """
        return os.path.join(self.__root_dir, 'resources', resource_name)

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
        with open(self.__path_to_file, mode='r', encoding='utf-8') as file_data:
            return file_data.read()

    @property
    def resource_name(self) -> str:
        """Get name of resource.
        :return: Name of resource file.
        :rtype: str.
        """
        return self.__resource_name
