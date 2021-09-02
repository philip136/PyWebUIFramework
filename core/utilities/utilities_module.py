from core.utilities.json_settings_file import JsonSettingsFile


class UtilitiesModule:
    @staticmethod
    def get_instance_of_settings_file():
        return JsonSettingsFile('settings.json')
