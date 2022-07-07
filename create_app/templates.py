from typing import Dict

from requests import get

from create_app.settings import TEMPLATES_FILE_URI


class AvailableTemplatesFetchError(Exception):
    pass


def get_templates() -> Dict[str, str]:
    response = get(TEMPLATES_FILE_URI)

    if not response.ok:
        raise AvailableTemplatesFetchError()

    return response.json()
