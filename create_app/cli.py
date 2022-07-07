from typing import Dict

import click
from cookiecutter.main import cookiecutter

from create_app.settings import DEFAULT_TEMPLATE_NAME
from create_app.templates import get_templates


class Argument:
    TEMPLATE_NAME = "template_name"


templates: Dict[str, str] = get_templates()


@click.command()
@click.argument(
    Argument.TEMPLATE_NAME,
    default=DEFAULT_TEMPLATE_NAME,
    type=click.Choice(templates),
)
def main(template_name: str) -> None:
    return handler(template_name)


def handler(template_name: str) -> None:
    click.echo(f"Basing your app on the '{template_name}' template. ")

    template_repository: str = templates[template_name]

    click.echo(f"\n\nCheck the template out! {template_repository}")

    click.echo("\n\nCreating app...")
    cookiecutter(template_repository)
    click.echo("\nYour app is ready! ✨ 👏 ✨")
