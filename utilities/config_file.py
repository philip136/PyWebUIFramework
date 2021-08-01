import json
from pathlib import Path


class ConfigFile:
    __path_to_file = Path(__file__).resolve().parent.parent.joinpath('resources', 'settings.json')

    @classmethod
    def read_from_json_file(cls):
        with open(cls.__path_to_file, 'r') as file:
            return json.load(file)
