from unittest.mock import MagicMock

from hexawyn.cli.screens.welcome import WelcomeScreen


class TestActionClearInput:
    def test_clears_value_when_non_empty(self) -> None:
        screen = WelcomeScreen()
        mock_input = MagicMock()
        mock_input.value = "some query"
        screen.query_one = MagicMock(return_value=mock_input)

        screen.action_clear_input()

        assert mock_input.value == ""


class TestOnMount:
    def test_focuses_command_input(self) -> None:
        screen = WelcomeScreen()
        mock_input = MagicMock()
        screen.query_one = MagicMock(return_value=mock_input)

        screen.on_mount()

        mock_input.focus.assert_called_once()
