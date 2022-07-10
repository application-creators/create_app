from unittest import TestCase
from unittest.mock import MagicMock, patch

from create_app.templates import AvailableTemplatesFetchError, get_templates
from create_app.tests.utils import get_module

MODULE = get_module(__file__)


class TemplatesTestCase(TestCase):
    @patch(f"{MODULE}.get")
    def test_get_templates_success(
        self,
        requests_get_mock: MagicMock,
    ) -> None:
        index_uri_mock = MagicMock()

        response_mock = MagicMock()
        requests_get_mock.return_value = response_mock

        templates = get_templates(index_uri_mock)

        requests_get_mock.assert_called_once_with(index_uri_mock)

        self.assertIs(templates, response_mock.json())

    @patch(f"{MODULE}.get")
    def test_get_templates_failure(
        self,
        requests_get_mock: MagicMock,
    ) -> None:
        index_uri_mock = MagicMock()

        response_mock = MagicMock()
        response_mock.ok = False

        requests_get_mock.return_value = response_mock

        with self.assertRaises(AvailableTemplatesFetchError):
            get_templates(index_uri_mock)

        requests_get_mock.assert_called_once_with(index_uri_mock)
