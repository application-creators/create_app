from unittest import TestCase
from unittest.mock import MagicMock, patch

from click import ClickException

from create_app.main import create_app, list_templates
from create_app.tests.utils import get_module

MODULE = get_module(__file__)


class MainTestCase(TestCase):
    @patch(f"{MODULE}.click", MagicMock())
    @patch(f"{MODULE}.cookiecutter")
    @patch(f"{MODULE}.get_templates")
    def test_create_app_success(
        self,
        get_templates_mock: MagicMock,
        cookiecutter_mock: MagicMock,
    ) -> None:
        template_name_mock = MagicMock()
        template_repo_mock = MagicMock()
        templates_mock = {
            template_name_mock: template_repo_mock,
        }

        get_templates_mock.return_value = templates_mock

        index_mock = MagicMock()

        use_defaults_mock = MagicMock()

        create_app(template_name_mock, index_mock, use_defaults_mock)

        get_templates_mock.assert_called_once_with(index_mock)

        cookiecutter_mock.assert_called_once_with(
            template_repo_mock,
            no_input=use_defaults_mock,
        )

    @patch(f"{MODULE}.click.echo", MagicMock())
    @patch(f"{MODULE}.cookiecutter")
    @patch(f"{MODULE}.get_templates")
    def test_create_app_when_index_fetch_fails(
        self,
        get_templates_mock: MagicMock,
        cookiecutter_mock: MagicMock,
    ) -> None:
        get_templates_mock.side_effect = Exception()

        template_name_mock = MagicMock()
        index_mock = MagicMock()
        use_defaults_mock = MagicMock()

        with self.assertRaises(ClickException):
            create_app(template_name_mock, index_mock, use_defaults_mock)

        get_templates_mock.assert_called_once_with(index_mock)

        cookiecutter_mock.assert_not_called()

    @patch(f"{MODULE}.click.echo", MagicMock())
    @patch(f"{MODULE}.cookiecutter")
    @patch(f"{MODULE}.get_templates")
    def test_create_app_when_template_does_not_exist_in_index(
        self,
        get_templates_mock: MagicMock,
        cookiecutter_mock: MagicMock,
    ) -> None:
        templates_mock = {}
        get_templates_mock.return_value = templates_mock

        template_name_mock = MagicMock()
        index_mock = MagicMock()
        use_defaults_mock = MagicMock()

        with self.assertRaises(ClickException):
            create_app(template_name_mock, index_mock, use_defaults_mock)

        get_templates_mock.assert_called_once_with(index_mock)

        cookiecutter_mock.assert_not_called()

    @patch(f"{MODULE}.click.echo", MagicMock())
    @patch(f"{MODULE}.get_templates")
    def test_list_templates(self, get_templates_mock: MagicMock) -> None:
        index_mock = MagicMock()

        template_name_mock = MagicMock()
        template_repo_mock = MagicMock()
        templates_mock = {
            template_name_mock: template_repo_mock,
        }

        get_templates_mock.return_value = templates_mock

        list_templates(index_mock)

        get_templates_mock.assert_called_once_with(index_mock)
