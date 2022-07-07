from os.path import join
from unittest import TestCase
from unittest.mock import MagicMock, patch

from create_app.settings import PACKAGE_NAME, TEMPLATES_FILE
from create_app.templates import (
    FILE_OPEN_MODE,
    get_all_templates,
    get_templates_file_path,
)
from create_app.tests.utils import get_module

MODULE = get_module(__file__)


class TemplatesTestCase(TestCase):
    def test_get_templates_file_path(self) -> None:
        path = get_templates_file_path()
        expected = join(PACKAGE_NAME, PACKAGE_NAME, TEMPLATES_FILE)

        self.assertTrue(path.endswith(expected))

    @patch(f"{MODULE}.json")
    @patch(f"{MODULE}.open")
    @patch(f"{MODULE}.get_templates_file_path")
    def test_get_all_templates(
        self,
        get_templates_file_path_mock: MagicMock,
        open_mock: MagicMock,
        json_mock: MagicMock,
    ) -> None:
        get_all_templates()

        get_templates_file_path_mock.assert_called_once()
        open_mock.assert_called_once_with(
            get_templates_file_path_mock(), FILE_OPEN_MODE
        )
        json_mock.load.assert_called_once_with(open_mock().__enter__())
