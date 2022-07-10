import click

from create_app.main import create_app, list_templates
from create_app.settings import TEMPLATES_FILE_URI


class Argument:
    TEMPLATE_NAME = "template_name"


class Option:
    USE_DEFAULTS = "--use-defaults"
    INDEX = "--index"


HELP = {
    Option.USE_DEFAULTS: "Use default configuration values from the template",
    Option.INDEX: f"Templates index URL. Default: {TEMPLATES_FILE_URI}",
}


@click.group()
def main():
    pass


@main.command()
@click.option(
    Option.USE_DEFAULTS,
    is_flag=True,
    help=HELP[Option.USE_DEFAULTS],
)
@click.option(
    Option.INDEX,
    default=TEMPLATES_FILE_URI,
    help=HELP[Option.INDEX],
)
@click.argument(Argument.TEMPLATE_NAME)
def create(template_name: str, index: str, use_defaults: bool) -> None:
    return create_app(template_name, index, use_defaults)


@main.command()
@click.option(
    Option.INDEX,
    default=TEMPLATES_FILE_URI,
    help=HELP[Option.INDEX],
)
def list(index: str) -> None:
    return list_templates(index)
