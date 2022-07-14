from unittest import TestCase
from unittest.mock import MagicMock, patch

from click import ClickException

from create_app.main import create_app, list_templates
from create_app.tests.utils import get_module

MODULE = get_module(__file__)


class MainTestCase(TestCase):
    @patch(f"{MODULE}.click", MagicMock())
    @patch(f"{MODULE}.Project")
    @patch(f"{MODULE}.TemplatesIndex")
    def test_create_app_success(
        self,
        templates_index_class_mock: MagicMock,
        project_class_mock: MagicMock,
    ) -> None:
        template_name_mock = MagicMock()
        index_url_mock = MagicMock()
        use_defaults_mock = MagicMock()
        config_file_mock = MagicMock()

        templates_index_mock = MagicMock()
        templates_index_class_mock.return_value = templates_index_mock
        template_mock = MagicMock()
        templates_index_mock.get_template.return_value = template_mock

        project_mock = MagicMock()
        project_class_mock.return_value = project_mock

        create_app(
            template_name_mock,
            index_url_mock,
            use_defaults_mock,
            config_file_mock,
        )

        templates_index_class_mock.assert_called_once_with(index_url_mock)
        templates_index_mock.get_template.assert_called_once_with(template_name_mock)

        project_class_mock.assert_called_once_with(
            template_mock,
            use_defaults_mock,
            config_file_mock,
        )

        project_mock.create.assert_called_once()

    @patch(f"{MODULE}.click.echo", MagicMock())
    @patch(f"{MODULE}.Project")
    @patch(f"{MODULE}.TemplatesIndex")
    def test_create_app_when_index_fails(
        self,
        templates_index_class_mock: MagicMock,
        project_class_mock: MagicMock,
    ) -> None:
        template_name_mock = MagicMock()
        index_url_mock = MagicMock()
        use_defaults_mock = MagicMock()
        config_file_mock = MagicMock()

        templates_index_mock = MagicMock()
        templates_index_class_mock.return_value = templates_index_mock
        templates_index_mock.get_template.side_effect = Exception("Failed")

        with self.assertRaises(ClickException):
            create_app(
                template_name_mock,
                index_url_mock,
                use_defaults_mock,
                config_file_mock,
            )

        templates_index_class_mock.assert_called_once_with(index_url_mock)
        templates_index_mock.get_template.assert_called_once_with(template_name_mock)

        project_class_mock.assert_not_called()

    @patch(f"{MODULE}.click.echo", MagicMock())
    @patch(f"{MODULE}.Project")
    @patch(f"{MODULE}.TemplatesIndex")
    def test_create_app_when_project_creation_fails(
        self,
        templates_index_class_mock: MagicMock,
        project_class_mock: MagicMock,
    ) -> None:
        template_name_mock = MagicMock()
        index_url_mock = MagicMock()
        use_defaults_mock = MagicMock()
        config_file_mock = MagicMock()

        templates_index_mock = MagicMock()
        templates_index_class_mock.return_value = templates_index_mock
        template_mock = MagicMock()
        templates_index_mock.get_template.return_value = template_mock

        project_mock = MagicMock()
        project_mock.create.side_effect = Exception("Failed")
        project_class_mock.return_value = project_mock

        with self.assertRaises(ClickException):
            create_app(
                template_name_mock,
                index_url_mock,
                use_defaults_mock,
                config_file_mock,
            )

        templates_index_class_mock.assert_called_once_with(index_url_mock)
        templates_index_mock.get_template.assert_called_once_with(template_name_mock)

        project_class_mock.assert_called_once_with(
            template_mock,
            use_defaults_mock,
            config_file_mock,
        )

        project_mock.create.assert_called_once()

    @patch(f"{MODULE}.click.echo", MagicMock())
    @patch(f"{MODULE}.TemplatesIndex")
    def test_list_templates(self, templates_index_class_mock: MagicMock) -> None:
        templates_index_mock = MagicMock()
        templates_index_class_mock.return_value = templates_index_mock

        templates_mock = MagicMock()
        templates_index_mock.get_templates.return_value = templates_mock

        index_url_mock = MagicMock()

        list_templates(index_url_mock)

        templates_index_class_mock.assert_called_once_with(index_url_mock)
        templates_mock.items.assert_called_once_with()
