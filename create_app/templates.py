from typing import Dict

from requests import get


class TemplatesIndexException(Exception):
    pass


class TemplatesIndexFetchError(TemplatesIndexException):
    pass


class TemplateNotFound(TemplatesIndexException):
    pass


class Template:
    def __init__(self, name: str, repo: str):
        self.name: str = name
        self.repo: str = repo


class TemplatesIndex:
    TIMEOUT = 3

    def __init__(self, index_url: str):
        self.index_url: str = index_url

    def get_template(self, name: str) -> Template:
        templates: Dict[str, str] = self.get_templates()

        if name not in templates:
            raise TemplateNotFound(
                f"Could not find a template named '{name}' "
                f"in the templates index ({self.index_url})"
            )

        return Template(name, templates[name])

    def get_templates(self):
        try:
            return self._get_templates()
        except Exception:
            raise TemplatesIndexFetchError(
                f"Failed to fetch templates from index! ({self.index_url})"
            )

    def _get_templates(self) -> Dict[str, str]:
        response = get(self.index_url, timeout=TemplatesIndex.TIMEOUT)

        if not response.ok:
            raise TemplatesIndexFetchError()

        return response.json()
