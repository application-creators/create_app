from unittest import TestCase
from unittest.mock import MagicMock, patch

from create_app.project_configuration import (
    ProjectConfiguration,
    TemplateConfigFileError,
    TemplateConfigFileNotFound,
)
from create_app.tests.utils import get_module

MODULE = get_module(__file__)


class ProjectConfigurationTestCase(TestCase):
    @patch(f"{MODULE}.ProjectConfiguration._get_template_config")
    def test_get_config(self, get_template_config_mock: MagicMock) -> None:
        template_config_file_path_mock = MagicMock()

        template_config_mock = MagicMock()
        get_template_config_mock.return_value = template_config_mock

        project_configuration = ProjectConfiguration(template_config_file_path_mock)
        returned_config = project_configuration.get_config()

        expected_config = {
            ProjectConfiguration.DEFAULT_CONTEXT_KEY: template_config_mock,
        }

        self.assertEqual(returned_config, expected_config)

    @patch(f"{MODULE}.json")
    @patch(f"{MODULE}.open")
    def test_get_template_config_success(
        self, open_mock: MagicMock, json_mock: MagicMock
    ) -> None:
        template_config_file_path_mock = MagicMock()

        file_mock = MagicMock()
        file_mock.__enter__.return_value = file_mock
        open_mock.return_value = file_mock

        json_config = MagicMock()
        json_mock.load.return_value = json_config

        project_configuration = ProjectConfiguration(template_config_file_path_mock)
        returned_template_config = project_configuration._get_template_config()

        open_mock.assert_called_once_with(template_config_file_path_mock)

        json_mock.load.assert_called_once_with(file_mock)

        self.assertIs(returned_template_config, json_config)

    @patch(f"{MODULE}.json")
    @patch(f"{MODULE}.open")
    def test_get_template_config_when_file_does_not_exist(
        self, open_mock: MagicMock, json_mock: MagicMock
    ) -> None:
        template_config_file_path_mock = MagicMock()

        open_mock.side_effect = FileNotFoundError("File does not exist")

        project_configuration = ProjectConfiguration(template_config_file_path_mock)

        with self.assertRaises(TemplateConfigFileNotFound):
            project_configuration._get_template_config()

        open_mock.assert_called_once_with(template_config_file_path_mock)
        json_mock.load.assert_not_called()

    @patch(f"{MODULE}.json")
    @patch(f"{MODULE}.open")
    def test_get_template_config_when_unexpected_error_is_raised(
        self, open_mock: MagicMock, json_mock: MagicMock
    ) -> None:
        template_config_file_path_mock = MagicMock()

        file_mock = MagicMock()
        file_mock.__enter__.return_value = file_mock
        open_mock.return_value = file_mock

        json_mock.load.side_effect = Exception("Unexpected error")

        project_configuration = ProjectConfiguration(template_config_file_path_mock)

        with self.assertRaises(TemplateConfigFileError):
            project_configuration._get_template_config()

        open_mock.assert_called_once_with(template_config_file_path_mock)
        json_mock.load.assert_called_once_with(file_mock)
