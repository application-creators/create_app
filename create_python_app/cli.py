import click
from cookiecutter.main import cookiecutter

from create_python_app.settings import DEFAULT_TEMPLATE_NAME, TEMPLATES


class Argument:
    TEMPLATE_NAME = "template_name"


@click.command()
@click.argument(
    Argument.TEMPLATE_NAME, default=DEFAULT_TEMPLATE_NAME, type=click.Choice(TEMPLATES)
)
def main(template_name):
    click.echo(f"Using '{template_name}' template. ")

    template_repo = TEMPLATES[template_name]

    cookiecutter(template_repo)
