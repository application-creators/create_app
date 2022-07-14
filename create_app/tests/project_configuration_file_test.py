from unittest import TestCase
from unittest.mock import MagicMock, patch

from create_app.project_configuration_file import ProjectConfigurationFile
from create_app.tests.utils import get_module

MODULE = get_module(__file__)


class ProjectConfigurationFileTestCase(TestCase):
    @patch(f"{MODULE}.json")
    @patch(f"{MODULE}.os")
    @patch(f"{MODULE}.mkstemp")
    def test_context_manager(
        self,
        mkstemp_mock: MagicMock,
        os_mock: MagicMock,
        json_mock: MagicMock,
    ) -> None:
        config_mock = MagicMock()

        tmp_file_file_descriptor = MagicMock()
        tmp_file_path = MagicMock()

        mkstemp_mock.return_value = (tmp_file_file_descriptor, tmp_file_path)

        opened_tmp_file = MagicMock()
        os_mock.fdopen.return_value = opened_tmp_file

        with ProjectConfigurationFile(config_mock) as project_configuration_file:
            self.assertIs(project_configuration_file.path, tmp_file_path)

            mkstemp_mock.assert_called_once_with()

            os_mock.fdopen.assert_called_once_with(
                tmp_file_file_descriptor,
                ProjectConfigurationFile.MODE,
            )

            json_mock.dump.assert_called_once_with(config_mock, opened_tmp_file)

            opened_tmp_file.close.assert_called_once()

        os_mock.remove.assert_called_once_with(tmp_file_path)
