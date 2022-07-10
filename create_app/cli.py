import click

from create_app.main import create_app
from create_app.settings import DEFAULT_TEMPLATE_NAME


class Argument:
    TEMPLATE_NAME = "template_name"


class Option:
    USE_DEFAULTS = "--use-defaults"


HELP = {
    Option.USE_DEFAULTS: "Use default configuration values from the template",
}


@click.command()
@click.option(
    Option.USE_DEFAULTS,
    is_flag=True,
    help=HELP[Option.USE_DEFAULTS],
)
@click.argument(
    Argument.TEMPLATE_NAME,
    default=DEFAULT_TEMPLATE_NAME,
)
def main(template_name: str, use_defaults: bool) -> None:
    return create_app(template_name, use_defaults)
