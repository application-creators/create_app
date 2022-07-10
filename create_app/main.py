from typing import Dict

import click
from cookiecutter.main import cookiecutter

from create_app.templates import get_templates


def create_app(template_name: str, index: str, use_defaults: bool) -> None:
    template_repository: str = _get_template_repository(index, template_name)

    click.echo(f"\n\nCheck the template out! {template_repository}")

    if use_defaults:
        click.echo("\n\nUsing default values from the template. ")

    click.echo("\n\nCreating app...\n")
    cookiecutter(template_repository, no_input=use_defaults)
    click.echo("\n\nYour app is ready! ✨ 👏 ✨")


def _get_template_repository(index: str, template_name: str) -> str:
    templates: Dict[str, str] = _try_to_get_templates(index)

    if template_name not in templates:
        raise click.ClickException(
            f"Could not find a template named '{template_name}' "
            f"in the templates index ({index})"
        )

    return templates[template_name]


def _try_to_get_templates(index: str) -> Dict[str, str]:
    try:
        click.echo("Fetching index...")
        templates: Dict[str, str] = get_templates(index)
        click.echo("Fetch successful.")
        return templates
    except Exception:
        raise click.ClickException(f"Failed to fetch templates from index! ({index})")


def list_templates(index: str) -> None:
    templates: Dict[str, str] = _try_to_get_templates(index)

    click.echo("\nTemplates in index:")

    for template_name, template_repository in templates.items():
        click.echo(f"  * {template_name} ({template_repository})")
