import click
from cookiecutter.main import cookiecutter

from create_app.settings import DEFAULT_TEMPLATE_NAME
from create_app.templates import get_all_templates


class Argument:
    TEMPLATE_NAME = "template_name"


TEMPLATES = get_all_templates()


@click.command()
@click.argument(
    Argument.TEMPLATE_NAME,
    default=DEFAULT_TEMPLATE_NAME,
    type=click.Choice(TEMPLATES),
)
def main(template_name):
    click.echo(f"Using '{template_name}' template. ")

    template_repository = TEMPLATES[template_name]

    click.echo(f"Template repository: {template_repository}")

    click.echo("Creating app...")
    cookiecutter(template_repository)
    click.echo("Finished up creating the app! ✨ 👏 ✨")
