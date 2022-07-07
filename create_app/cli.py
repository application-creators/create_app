import click
from cookiecutter.main import cookiecutter

from create_app.settings import DEFAULT_TEMPLATE_NAME
from create_app.templates import get_templates


class Argument:
    TEMPLATE_NAME = "template_name"


def handler(templates, template_name):
    click.echo(f"Basing your app on the '{template_name}' template. ")

    template_repository = templates[template_name]

    click.echo(f"\n\nCheck the template out! {template_repository}")

    click.echo("\n\nCreating app...")
    cookiecutter(template_repository)
    click.echo("\nYou've created your new app! ✨ 👏 ✨")


def build_main():
    templates = get_templates()

    @click.command()
    @click.argument(
        Argument.TEMPLATE_NAME,
        default=DEFAULT_TEMPLATE_NAME,
        type=click.Choice(templates),
    )
    def _main(template_name):
        handler(templates, template_name)

    return _main


main = build_main()
