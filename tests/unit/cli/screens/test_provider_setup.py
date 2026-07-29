from unittest.mock import MagicMock, patch

from hexawyn.cli.screens.provider_setup import ProviderSetupScreen


class TestProviderSetupInit:
    def test_providers_list_has_nine_entries(self) -> None:
        assert len(ProviderSetupScreen.PROVIDERS) == 9  # noqa: PLR2004

    def test_providers_include_deepseek(self) -> None:
        names = [name for _, name, _ in ProviderSetupScreen.PROVIDERS]
        assert "DeepSeek" in names

    def test_providers_include_openai(self) -> None:
        names = [name for _, name, _ in ProviderSetupScreen.PROVIDERS]
        assert "OpenAI" in names

    def test_providers_include_custom(self) -> None:
        names = [name for _, name, _ in ProviderSetupScreen.PROVIDERS]
        assert "Custom" in names


class TestActionSkip:
    def test_skip_calls_dismiss(self) -> None:
        screen = ProviderSetupScreen()
        screen.dismiss = MagicMock()  # type: ignore[method-assign]
        screen.action_skip()
        screen.dismiss.assert_called_once()


class TestOnButtonPressed:
    def test_skip_button_dismisses(self) -> None:
        screen = ProviderSetupScreen()
        screen.dismiss = MagicMock()  # type: ignore[method-assign]
        event = MagicMock()
        event.button.id = "setup-skip"
        screen.on_button_pressed(event)
        screen.dismiss.assert_called_once()

    def test_select_provider_sets_selected_provider(self) -> None:
        screen = ProviderSetupScreen()
        screen._selected_provider = ""
        screen._highlight_provider = MagicMock()  # type: ignore[method-assign]
        screen.query_one = MagicMock()  # type: ignore[method-assign]

        event = MagicMock()
        event.button.id = "provider-1"
        screen.on_button_pressed(event)

        assert screen._selected_provider == "DeepSeek"

    def test_select_custom_provider_sets_custom(self) -> None:
        screen = ProviderSetupScreen()
        screen._selected_provider = ""
        screen._highlight_provider = MagicMock()  # type: ignore[method-assign]
        screen.query_one = MagicMock()  # type: ignore[method-assign]

        event = MagicMock()
        event.button.id = "provider-0"
        screen.on_button_pressed(event)

        assert screen._selected_provider == "Custom"

    def test_select_custom_updates_placeholder(self) -> None:
        screen = ProviderSetupScreen()
        screen._selected_provider = ""
        screen._highlight_provider = MagicMock()  # type: ignore[method-assign]
        mock_input = MagicMock()
        screen.query_one = MagicMock(return_value=mock_input)

        event = MagicMock()
        event.button.id = "provider-0"
        screen.on_button_pressed(event)

        assert "base URL" in mock_input.placeholder

    def test_select_provider_updates_placeholder_with_name(self) -> None:
        screen = ProviderSetupScreen()
        screen._selected_provider = ""
        screen._highlight_provider = MagicMock()  # type: ignore[method-assign]
        mock_input = MagicMock()
        screen.query_one = MagicMock(return_value=mock_input)

        event = MagicMock()
        event.button.id = "provider-3"
        screen.on_button_pressed(event)

        assert "Groq" in mock_input.placeholder


class TestSaveAndContinue:
    def _make_screen_with_mocks(self) -> tuple[ProviderSetupScreen, MagicMock, MagicMock]:
        screen = ProviderSetupScreen()
        screen.dismiss = MagicMock()  # type: ignore[method-assign]
        mock_input = MagicMock()
        mock_input.value = "sk-test-key"
        mock_status = MagicMock()
        screen.query_one = MagicMock(
            side_effect=lambda selector, _widget_type=None: {
                "#setup-key": mock_input,
                "#setup-status": mock_status,
            }[selector]
        )
        return screen, mock_input, mock_status

    def test_save_requires_provider_selection(self) -> None:
        screen, mock_input, mock_status = self._make_screen_with_mocks()
        screen._selected_provider = ""

        screen._save_and_continue()

        mock_status.update.assert_called_once()
        assert "select a provider" in str(mock_status.update.call_args[0][0]).lower()

    def test_save_requires_api_key(self) -> None:
        screen, mock_input, mock_status = self._make_screen_with_mocks()
        screen._selected_provider = "OpenAI"
        mock_input.value = ""

        screen._save_and_continue()

        mock_status.update.assert_called_once()
        assert "API key" in str(mock_status.update.call_args[0][0])

    def test_custom_provider_first_paste_is_url(self) -> None:
        screen = ProviderSetupScreen()
        screen.dismiss = MagicMock()  # type: ignore[method-assign]
        screen._selected_provider = "Custom"
        screen._selected_url = ""
        mock_input = MagicMock()
        mock_input.value = "https://my-llm.example.com/v1"
        mock_status = MagicMock()
        screen.query_one = MagicMock(
            side_effect=lambda selector, _widget_type=None: {
                "#setup-key": mock_input,
                "#setup-status": mock_status,
            }[selector]
        )

        screen._save_and_continue()

        assert screen._selected_url == "https://my-llm.example.com/v1"

    def test_custom_provider_invalid_url_shows_error(self) -> None:
        screen = ProviderSetupScreen()
        screen.dismiss = MagicMock()  # type: ignore[method-assign]
        screen._selected_provider = "Custom"
        screen._selected_url = ""
        mock_input = MagicMock()
        mock_input.value = "not-a-url"
        mock_status = MagicMock()
        screen.query_one = MagicMock(
            side_effect=lambda selector, _widget_type=None: {
                "#setup-key": mock_input,
                "#setup-status": mock_status,
            }[selector]
        )

        screen._save_and_continue()

        mock_status.update.assert_called_once()
        assert "URL" in str(mock_status.update.call_args[0][0])

    def test_save_calls_save_llm_config_and_dismisses(self) -> None:
        screen, mock_input, mock_status = self._make_screen_with_mocks()
        screen._selected_provider = "OpenAI"
        screen._selected_url = "https://api.openai.com/v1"

        with patch("hexawyn.infrastructure.config.config_manager.save_llm_config") as mock_save:
            with patch.dict("os.environ", {}, clear=True):
                screen._save_and_continue()

        mock_save.assert_called_once_with("OpenAI", "https://api.openai.com/v1", "sk-test-key")
        screen.dismiss.assert_called_once()
