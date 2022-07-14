from unittest import TestCase
from unittest.mock import MagicMock, patch

from create_app.project import Project
from create_app.tests.utils import get_module

MODULE = get_module(__file__)


class ProjectTestCase(TestCase):
    @patch(f"{MODULE}.cookiecutter")
    @patch(f"{MODULE}.ProjectConfigurationFile")
    @patch(f"{MODULE}.ProjectConfiguration")
    def test_create_without_default_and_without_config_file_path(
        self,
        project_configuration_class_mock: MagicMock,
        project_configuration_file_class_mock: MagicMock,
        cookiecutter_mock: MagicMock,
    ) -> None:
        template_mock = MagicMock()
        use_defaults = False
        config_file_path = None

        project_configuration_file_mock = MagicMock()
        project_configuration_file_mock.__enter__.return_value = (
            project_configuration_file_mock
        )
        project_configuration_file_class_mock.return_value = (
            project_configuration_file_mock
        )

        Project(template_mock, use_defaults, config_file_path).create()

        project_configuration_class_mock.assert_not_called()

        default_config = {}
        project_configuration_file_class_mock.assert_called_once_with(default_config)
        project_configuration_file_mock.__enter__.assert_called_once()

        cookiecutter_mock.assert_called_once_with(
            template_mock.repo,
            no_input=False,
            config_file=project_configuration_file_mock.path,
        )

    @patch(f"{MODULE}.cookiecutter")
    @patch(f"{MODULE}.ProjectConfigurationFile")
    @patch(f"{MODULE}.ProjectConfiguration")
    def test_create_with_default_and_without_config_file_path(
        self,
        project_configuration_class_mock: MagicMock,
        project_configuration_file_class_mock: MagicMock,
        cookiecutter_mock: MagicMock,
    ) -> None:
        template_mock = MagicMock()
        use_defaults = True
        config_file_path = None

        project_configuration_file_mock = MagicMock()
        project_configuration_file_mock.__enter__.return_value = (
            project_configuration_file_mock
        )
        project_configuration_file_class_mock.return_value = (
            project_configuration_file_mock
        )

        Project(template_mock, use_defaults, config_file_path).create()

        project_configuration_class_mock.assert_not_called()

        default_config = {}
        project_configuration_file_class_mock.assert_called_once_with(default_config)
        project_configuration_file_mock.__enter__.assert_called_once()

        cookiecutter_mock.assert_called_once_with(
            template_mock.repo,
            no_input=True,
            config_file=project_configuration_file_mock.path,
        )

    @patch(f"{MODULE}.cookiecutter")
    @patch(f"{MODULE}.ProjectConfigurationFile")
    @patch(f"{MODULE}.ProjectConfiguration")
    def test_create_without_default_and_with_config_file_path(
        self,
        project_configuration_class_mock: MagicMock,
        project_configuration_file_class_mock: MagicMock,
        cookiecutter_mock: MagicMock,
    ) -> None:
        template_mock = MagicMock()
        use_defaults = False
        config_file_path = MagicMock()

        config_mock = MagicMock()
        project_configuration_mock = MagicMock()
        project_configuration_mock.get_config.return_value = config_mock
        project_configuration_class_mock.return_value = project_configuration_mock

        project_configuration_file_mock = MagicMock()
        project_configuration_file_mock.__enter__.return_value = (
            project_configuration_file_mock
        )
        project_configuration_file_class_mock.return_value = (
            project_configuration_file_mock
        )

        Project(template_mock, use_defaults, config_file_path).create()

        project_configuration_class_mock.assert_called_once_with(config_file_path)

        project_configuration_file_class_mock.assert_called_once_with(config_mock)
        project_configuration_file_mock.__enter__.assert_called_once()

        cookiecutter_mock.assert_called_once_with(
            template_mock.repo,
            no_input=True,
            config_file=project_configuration_file_mock.path,
        )
