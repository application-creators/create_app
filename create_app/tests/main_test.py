from unittest import TestCase
from unittest.mock import MagicMock, patch

from create_app.main import create_app
from create_app.tests.utils import get_module

MODULE = get_module(__file__)


class MainTestCase(TestCase):
    @patch(f"{MODULE}.click", MagicMock())
    @patch(f"{MODULE}.cookiecutter")
    @patch(f"{MODULE}.get_templates")
    def test_create_app(
        self,
        get_templates_mock: MagicMock,
        cookiecutter_mock: MagicMock,
    ) -> None:
        template_name_mock = MagicMock()
        template_repo_mock = MagicMock()
        templates_mock = {
            template_name_mock: template_repo_mock,
        }

        use_defaults_mock = MagicMock()

        get_templates_mock.return_value = templates_mock

        create_app(template_name_mock, use_defaults_mock)

        get_templates_mock.assert_called_once_with()

        cookiecutter_mock.assert_called_once_with(
            template_repo_mock,
            no_input=use_defaults_mock,
        )
