from unittest import TestCase
from unittest.mock import MagicMock, patch

from create_app.tests.utils import get_module

MODULE = get_module(__file__)


class TemplatesTestCase(TestCase):
    def setUp(self) -> None:
        self.click_command_mock = patch("click.command").start()
        self.click_argument_mock = patch("click.argument").start()
        self.click_choice_mock = patch("click.Choice").start()

        self.cookiecutter_mock = patch("cookiecutter.main.cookiecutter").start()

        self.get_templates_mock = patch("create_app.templates.get_templates").start()

    def tearDown(self) -> None:
        self.click_command_mock.stop()
        self.click_argument_mock.stop()
        self.click_choice_mock.stop()

        self.cookiecutter_mock.stop()

        self.get_templates_mock.stop()

    def test_main(self) -> None:
        template_name_mock = MagicMock()
        template_repository_mock = MagicMock()

        templates_mock = {
            template_name_mock: template_repository_mock,
        }

        self.get_templates_mock.return_value = templates_mock

        from create_app.cli import handler

        self.get_templates_mock.assert_called_once()

        self.click_choice_mock.assert_called_once_with(templates_mock)
        self.click_argument_mock.assert_called_once()
        self.click_command_mock.assert_called_once()

        handler(template_name_mock)

        self.cookiecutter_mock.assert_called_once_with(template_repository_mock)
