from unittest import TestCase
from unittest.mock import MagicMock, patch

from create_app.settings import TEMPLATES_FILE_URI
from create_app.templates import AvailableTemplatesFetchError, get_templates
from create_app.tests.utils import get_module

MODULE = get_module(__file__)


class TemplatesTestCase(TestCase):
    @patch(f"{MODULE}.get")
    def test_get_templates_success(
        self,
        requests_get_mock: MagicMock,
    ) -> None:
        response_mock = MagicMock()
        requests_get_mock.return_value = response_mock

        templates = get_templates()

        requests_get_mock.assert_called_once_with(TEMPLATES_FILE_URI)

        self.assertIs(templates, response_mock.json())

    @patch(f"{MODULE}.get")
    def test_get_templates_failure(
        self,
        requests_get_mock: MagicMock,
    ) -> None:
        response_mock = MagicMock()
        response_mock.ok = False

        requests_get_mock.return_value = response_mock

        with self.assertRaises(AvailableTemplatesFetchError):
            get_templates()

        requests_get_mock.assert_called_once_with(TEMPLATES_FILE_URI)
