from typing import Dict

import click
from cookiecutter.main import cookiecutter

from create_app.templates import get_templates


def create_app(template_name: str, use_defaults: bool) -> None:
    templates: Dict[str, str] = get_templates()

    click.echo(f"Basing your app on the '{template_name}' template. ")

    template_repository: str = templates[template_name]

    click.echo(f"\n\nCheck the template out! {template_repository}")

    if use_defaults:
        click.echo("\n\nUsing default values from the template. ")

    click.echo("\n\nCreating app...")
    cookiecutter(template_repository, no_input=use_defaults)
    click.echo("\nYour app is ready! ✨ 👏 ✨")
