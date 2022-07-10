from unittest import TestCase
from unittest.mock import MagicMock, patch

from create_app.tests.utils import get_module

MODULE = get_module(__file__)


class CliTestCase(TestCase):
    def setUp(self) -> None:
        def return_decorated_function(decorated_function):
            return decorated_function

        self.click_command_mock = patch(
            "click.command",
            return_value=return_decorated_function,
        ).start()
        self.click_option_mock = patch(
            "click.option",
            return_value=return_decorated_function,
        ).start()
        self.click_argument_mock = patch(
            "click.argument",
            return_value=return_decorated_function,
        ).start()

    def tearDown(self) -> None:
        self.click_argument_mock.stop()
        self.click_option_mock.stop()
        self.click_command_mock.stop()

    @patch(f"{MODULE}.create_app")
    def test_main(self, create_app_mock: MagicMock):
        template_name_mock = MagicMock()
        use_defaults_mock = MagicMock()

        from create_app.cli import main

        self.click_command_mock.assert_called_once()
        self.click_option_mock.assert_called_once()
        self.click_argument_mock.assert_called_once()

        main(template_name_mock, use_defaults_mock)

        create_app_mock.assert_called_once_with(
            template_name_mock,
            use_defaults_mock,
        )
