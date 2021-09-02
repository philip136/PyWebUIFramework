import os
import json
import typing as ty

from jsonpath_ng import DatumInContext
from jsonpath_ng import parse

from core.utilities.base_settings_file import BaseSettingsFile
from core.utilities.resource_file import ResourceFile


class JsonSettingsFile(BaseSettingsFile):
    """Class which defines work with .json settings file."""
    __resource_path = None

    def __init__(self, resource_name: str, root_dir: str = None):
        self.__resource_file = ResourceFile(resource_name, root_dir)
        self.__content = json.loads(self.__resource_file.file_content)

    @staticmethod
    def __use_env_value_or_default(node: ty.List[DatumInContext], env_value: ty.Any) -> ty.Any:
        return env_value if env_value else node[0].value

    @staticmethod
    def __get_env_value(json_path: str) -> ty.Optional[str]:
        return os.getenv(json_path)

    def __get_json_node(self, json_path: str, raise_exception_if_empty: bool):
        node = parse(f'$.{json_path}').find(self.__content)
        if not node and raise_exception_if_empty:
            raise ValueError(f'Json field by json-path {json_path} was not found')
        return node

    def __get_env_value_or_default(self, json_path: str, raise_exception_if_empty: bool = False) -> ty.Any:
        env_var = self.__get_env_value(json_path)
        node = self.__get_json_node(json_path, raise_exception_if_empty and not env_var)
        return self.__use_env_value_or_default(node, env_var) if node else env_var

    def get_value(self, path: str) -> ty.Any:
        """Get single value by specified path from settings file.
        :param path: Path to value.

        :return: Value from file.
        :rtype: str.
        """
        return self.__get_env_value_or_default(path, raise_exception_if_empty=True)

    def get_list(self, path: str) -> ty.List[ty.Any]:
        """Get list of values by specified path from settings file.
        :param path: Path to list.

        :return: List of values from file.
        :rtype: List[Any].
        """
        env_var = self.__get_env_value(path)
        data = (env_var.split(",") if env_var else self.__get_json_node(path, raise_exception_if_empty=True)[0].value)
        return [value.strip() for value in data]

    def get_dictionary(self, path: str) -> ty.Dict[str, ty.Any]:
        """Get dictionary of values by specified path from settings file.
        :param path: Path to dict.

        :return: Dict of values from file.
        :rtype: Dict[str, Any].
        """
        node = self.__get_json_node(path, raise_exception_if_empty=True)
        return {key: self.get_value(f'{path}.{key}') for key, val in node[0].value}

    def is_value_present(self, path: str) -> bool:
        """Check that value present in settings file.
        :param path: Path to value.

        :return: Presence of value.
        :rtype: bool.
        """
        return (self.__get_env_value(path) is not None or len(self.__get_json_node(
            path, raise_exception_if_empty=True)) > 0)
