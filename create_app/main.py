from typing import Dict, Optional

import click

from create_app.project import Project
from create_app.settings import TEMPLATES_FILE_URI
from create_app.templates import Template, TemplatesIndex


def create_app(
    template_name: str,
    index: str = TEMPLATES_FILE_URI,
    use_defaults: bool = False,
    config_file: Optional[str] = None,
) -> None:
    click.echo("Fetching template...")
    template: Template = _get_template(index, template_name)
    click.echo(f"Template '{template.name}' is available at {template.repo}\n")

    click.echo("Creating project...")
    _create_project(template, use_defaults, config_file)
    click.echo("Project created! ✨ 👏 ✨")


def _get_template(index: str, template_name: str) -> Template:
    try:
        return TemplatesIndex(index).get_template(template_name)
    except Exception as e:
        raise click.ClickException(str(e))


def _create_project(
    template: Template,
    use_defaults: bool,
    config_file: Optional[str],
) -> None:
    try:
        return Project(template, use_defaults, config_file).create()
    except Exception as e:
        raise click.ClickException(str(e))


def list_templates(index: str) -> None:
    templates: Dict[str, str] = TemplatesIndex(index).get_templates()

    click.echo("\nTemplates in index:")

    for template_name, template_repo in templates.items():
        click.echo(f"  * {template_name} ({template_repo})")
