import importlib
from unittest import TestCase
from unittest.mock import MagicMock, patch

from create_app import cli
from create_app.tests.utils import get_module

MODULE = get_module(__file__)


class CliTestCase(TestCase):
    def setUp(self) -> None:
        def return_decorated_function(decorated_function):
            return decorated_function

        main_mock = MagicMock()
        main_group_mock = MagicMock(return_value=main_mock)
        main_mock.command.return_value = return_decorated_function

        self.click_group_mock = patch(
            "click.group",
            return_value=main_group_mock,
        ).start()

        self.click_option_mock = patch(
            "click.option",
            return_value=return_decorated_function,
        ).start()

        self.click_argument_mock = patch(
            "click.argument",
            return_value=return_decorated_function,
        ).start()

        importlib.reload(cli)

    def tearDown(self) -> None:
        self.click_group_mock.stop()
        self.click_option_mock.stop()
        self.click_argument_mock.stop()

    @patch(f"{MODULE}.create_app")
    def test_create(self, create_app_mock: MagicMock):
        template_name_mock = MagicMock()
        index_mock = MagicMock()
        use_defaults_mock = MagicMock()

        from create_app.cli import create

        create(template_name_mock, index_mock, use_defaults_mock)

        create_app_mock.assert_called_once_with(
            template_name_mock,
            index_mock,
            use_defaults_mock,
        )

    @patch(f"{MODULE}.list_templates")
    def test_list(self, list_templates_mock: MagicMock):
        index_mock = MagicMock()

        from create_app.cli import list

        list(index_mock)

        list_templates_mock.assert_called_once_with(index_mock)
