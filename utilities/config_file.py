import json
from pathlib import Path


class ConfigFile:
    __path_to_resources = Path(__file__).resolve().parent.parent.joinpath('resources')

    @classmethod
    def read_from_json_file(cls):
        with open(cls.__path_to_resources.joinpath('settings.json'), 'r') as file:
            return json.load(file)

    @classmethod
    def get_browser_name(cls):
        return cls.read_from_json_file()['browserName'].lower()

    @classmethod
    def get_timeouts(cls):
        return cls.read_from_json_file()['timeouts']
