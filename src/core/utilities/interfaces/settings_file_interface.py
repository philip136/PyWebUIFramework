import typing as ty
from abc import ABC, abstractmethod


class ISettingsFile(ABC):
    @abstractmethod
    def get_value(self, path: str) -> ty.Any:
        """Get single value by specified path from settings file.
        :param path: Path to value.

        :return: Value from file.
        :rtype: str.
        """
        pass

    @abstractmethod
    def is_value_present(self, path: str) -> bool:
        """Check that value present in settings file.
        :param path: Path to value.

        :return: Presence of value.
        :rtype: bool.
        """
        pass

    def get_value_or_default(self, path: str, default: ty.Any) -> ty.Any:
        """Get single value by specified path from settings file or default if not present.
        :param path: Path to value.
        :param default: Default value.

        :return: Value from file or default if not present.
        :rtype: Any.
        """
        return self.get_value(path) if self.is_value_present(path) else default

    @abstractmethod
    def get_dictionary(self, path: str) -> ty.Dict[str, ty.Any]:
        """Get dictionary of values by specified path from settings file.
        :param path: Path to dict.

        :return: Dict of values from file.
        :rtype: Dict[str, Any].
        """
        pass

    @abstractmethod
    def get_list(self, path: str) -> ty.List[ty.Any]:
        """Get list of values by specified path from settings file.
        :param path: Path to list.

        :return: List of values from file.
        :rtype: List[Any].
        """
        pass
