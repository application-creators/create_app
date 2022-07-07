from unittest import TestCase
from unittest.mock import MagicMock, patch

from create_app.cli import build_main, handler
from create_app.tests.utils import get_module

MODULE = get_module(__file__)


class TemplatesTestCase(TestCase):
    @patch(f"{MODULE}.click")
    @patch(f"{MODULE}.get_templates")
    def test_build_main(
        self,
        get_templates_mock: MagicMock,
        click_mock: MagicMock,
    ) -> None:
        templates_mock = MagicMock()
        get_templates_mock.return_value = templates_mock

        build_main()

        get_templates_mock.assert_called_once()
        click_mock.Choice.assert_called_once_with(templates_mock)

    @patch(f"{MODULE}.click", MagicMock())
    @patch(f"{MODULE}.cookiecutter")
    def test_handler(self, cookiecutter_mock: MagicMock) -> None:
        template_name_mock = MagicMock()
        template_repository_mock = MagicMock()

        templates_mock = {
            template_name_mock: template_repository_mock,
        }

        handler(templates_mock, template_name_mock)

        cookiecutter_mock.assert_called_once_with(template_repository_mock)
