from typing import Dict

from requests import get


class AvailableTemplatesFetchError(Exception):
    pass


def get_templates(index_uri: str) -> Dict[str, str]:
    response = get(index_uri)

    if not response.ok:
        raise AvailableTemplatesFetchError()

    return response.json()
