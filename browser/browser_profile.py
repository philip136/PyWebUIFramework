from utilities.config_file import ConfigFile
from driver_settings.driver_settings_factory import DriverSettingsFactory


class BrowserProfile:
    __settings_file = ConfigFile.read_from_json_file()

    @classmethod
    def get_driver_settings(cls):
        """Get driver settings with capabilities, options and preferences.

        :rtype: DriverSettings.

        """
        browser_name = cls.__settings_file['browserName'].upper()
        return DriverSettingsFactory.get_driver_settings(browser_name=browser_name)
