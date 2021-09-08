from abc import ABC, abstractmethod


class BaseLocalizationManager(ABC):
    """This class is used for translation messages."""

    @abstractmethod
    def get_localized_message(self, message_key, *message_args) -> str:
        """Get localized message from resources.
        :param message_key: Key in resource file.
        :param message_args: Params which will be provided to template of localized message.

        :return: Localized message.
        :rtype: str.
        """
        pass
