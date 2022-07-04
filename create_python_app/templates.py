import json
from os.path import abspath, dirname, join
from typing import Dict

from create_python_app.settings import TEMPLATES_FILE

FILE_OPEN_MODE = "r"


def get_templates_file_path() -> str:
    return join(dirname(abspath(__file__)), TEMPLATES_FILE)


def get_all_templates() -> Dict[str, str]:
    with open(get_templates_file_path(), FILE_OPEN_MODE) as json_file:
        return json.load(json_file)
