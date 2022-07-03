from json import load
from os.path import abspath, dirname, join

from create_python_app.settings import TEMPLATES_FILE

FILE_OPEN_MODE = "r"


def get_templates_file_path():
    return join(dirname(abspath(__file__)), TEMPLATES_FILE)


def get_all_templates():
    with open(get_templates_file_path(), FILE_OPEN_MODE) as json_file:
        return load(json_file)
