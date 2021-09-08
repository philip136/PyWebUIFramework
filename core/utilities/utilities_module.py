from core.utilities.json_settings_file import JsonSettingsFile
from core.utilities.action_retrier import ActionRetrier


class UtilitiesModule:
    @staticmethod
    def get_instance_of_settings_file():
        return JsonSettingsFile('settings.json')

    @staticmethod
    def get_instance_of_retrier():
        return ActionRetrier()
