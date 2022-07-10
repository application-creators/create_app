from unittest import TestCase
from unittest.mock import MagicMock, patch


class MainTestCase(TestCase):
    @patch("create_app.cli.main", MagicMock())
    def test_main(self) -> None:
        from create_app.__main__ import main

        main.assert_called_once_with()
