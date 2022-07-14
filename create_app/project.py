from typing import Dict, Optional

from cookiecutter.main import cookiecutter

from create_app.project_configuration import ProjectConfiguration
from create_app.project_configuration_file import ProjectConfigurationFile
from create_app.templates import Template


class Project:
    def __init__(
        self,
        template: Template,
        use_defaults: bool,
        config_file_path: Optional[str],
    ):
        self.template: Template = template
        self.use_defaults: bool = use_defaults
        self.config_file_path: Optional[str] = config_file_path

    def create(self) -> None:
        config: Dict = {}

        use_defaults = self.use_defaults

        if self.config_file_path:
            use_defaults = True
            config = ProjectConfiguration(self.config_file_path).get_config()

        with ProjectConfigurationFile(config) as configuration_file:
            cookiecutter(
                self.template.repo,
                no_input=use_defaults,
                config_file=configuration_file.path,
            )
