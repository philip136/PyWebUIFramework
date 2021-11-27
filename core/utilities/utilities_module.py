from core.utilities.json_settings_file import JsonSettingsFile
from core.utilities.action_repeater import ActionRepeater


class UtilitiesModule:
    @staticmethod
    def get_instance_of_settings_file() -> JsonSettingsFile:
        return JsonSettingsFile('settings.json')

    @staticmethod
    def get_instance_of_repeater() -> ActionRepeater:
        return ActionRepeater()
