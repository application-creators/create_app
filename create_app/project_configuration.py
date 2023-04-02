import json
from typing import Dict


class TemplateConfigFileError(Exception):
    pass


class TemplateConfigFileNotFound(TemplateConfigFileError):
    pass


class ProjectConfiguration:
    DEFAULT_CONTEXT_KEY = "default_context"

    def __init__(self, template_config_file_path: str):
        self.template_config_file_path: str = template_config_file_path

    def get_config(self) -> Dict:
        return {ProjectConfiguration.DEFAULT_CONTEXT_KEY: self._get_template_config()}

    def _get_template_config(self) -> Dict:
        try:
            with open(self.template_config_file_path) as user_template_config_file:
                return json.load(user_template_config_file)
        except FileNotFoundError:
            raise TemplateConfigFileNotFound(
                f"File {self.template_config_file_path} does not exist"
            )
        except Exception:
            raise TemplateConfigFileError(
                f"An unexpected error has occurred while attempting to read "
                f"the contents of file {self.template_config_file_path}"
            )
