from unittest import TestCase
from unittest.mock import MagicMock, patch

from create_app.templates import (
    TemplateNotFound,
    TemplatesIndex,
    TemplatesIndexFetchError,
)
from create_app.tests.utils import get_module

MODULE = get_module(__file__)


class TemplatesIndexTestCase(TestCase):
    @patch(f"{MODULE}.get")
    def test_get_templates_success(
        self,
        requests_get_mock: MagicMock,
    ) -> None:
        index_uri_mock = MagicMock()

        response_mock = MagicMock()
        response_mock.ok = True
        requests_get_mock.return_value = response_mock

        templates = TemplatesIndex(index_uri_mock).get_templates()

        requests_get_mock.assert_called_once_with(
            index_uri_mock, timeout=TemplatesIndex.TIMEOUT
        )

        self.assertIs(templates, response_mock.json())

    @patch(f"{MODULE}.get")
    def test_get_templates_when_request_fails(
        self,
        requests_get_mock: MagicMock,
    ) -> None:
        index_uri_mock = MagicMock()

        requests_get_mock.side_effect = Exception("Failed")

        with self.assertRaises(TemplatesIndexFetchError):
            TemplatesIndex(index_uri_mock).get_templates()

        requests_get_mock.assert_called_once_with(
            index_uri_mock, timeout=TemplatesIndex.TIMEOUT
        )

    @patch(f"{MODULE}.get")
    def test_get_templates_when_request_returns_bad_status(
        self,
        requests_get_mock: MagicMock,
    ) -> None:
        index_uri_mock = MagicMock()

        response_mock = MagicMock()
        response_mock.ok = False

        requests_get_mock.return_value = response_mock

        with self.assertRaises(TemplatesIndexFetchError):
            TemplatesIndex(index_uri_mock).get_templates()

        requests_get_mock.assert_called_once_with(
            index_uri_mock, timeout=TemplatesIndex.TIMEOUT
        )

    @patch(f"{MODULE}.TemplatesIndex.get_templates")
    def test_get_template_success(self, get_templates_mock: MagicMock) -> None:
        index_url_mock = MagicMock()

        template_name_mock = MagicMock()
        template_repo_mock = MagicMock()

        get_templates_mock.return_value = {
            template_name_mock: template_repo_mock,
        }

        templates_index = TemplatesIndex(index_url_mock)

        template = templates_index.get_template(template_name_mock)

        self.assertIs(template.name, template_name_mock)
        self.assertIs(template.repo, template_repo_mock)

    @patch(f"{MODULE}.TemplatesIndex.get_templates")
    def test_get_template_when_template_does_not_exist_in_index(
        self, get_templates_mock: MagicMock
    ) -> None:
        index_url_mock = MagicMock()

        template_name_mock = MagicMock()

        templates_index = TemplatesIndex(index_url_mock)
        get_templates_mock.return_value = {}

        with self.assertRaises(TemplateNotFound):
            templates_index.get_template(template_name_mock)
