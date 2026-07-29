from unittest.mock import MagicMock, patch


class TestSetupInfo:
    def test_shows_provider_info(self) -> None:
        from hexawyn.cli.presentation.setup_info import render_setup_info

        mock_log = MagicMock()
        with patch(
            "hexawyn.cli.presentation.setup_info.get_llm_config",
            return_value={
                "provider": "openai",
                "base_url": "https://api.openai.com",
                "api_key": "sk-test",
            },
        ):
            render_setup_info(mock_log)

        assert mock_log.write.call_count >= 3  # noqa: PLR2004

    def test_shows_missing_key_warning(self) -> None:
        from hexawyn.cli.presentation.setup_info import render_setup_info

        mock_log = MagicMock()
        with patch(
            "hexawyn.cli.presentation.setup_info.get_llm_config",
            return_value={
                "provider": "openai",
                "base_url": "https://api.openai.com",
                "api_key": "",
            },
        ):
            render_setup_info(mock_log)

        written = [str(c[0][0]) for c in mock_log.write.call_args_list]
        assert any("missing" in w.lower() for w in written)

    def test_shows_configured_key(self) -> None:
        from hexawyn.cli.presentation.setup_info import render_setup_info

        mock_log = MagicMock()
        with patch(
            "hexawyn.cli.presentation.setup_info.get_llm_config",
            return_value={
                "provider": "openai",
                "base_url": "https://api.openai.com",
                "api_key": "sk-key",
            },
        ):
            render_setup_info(mock_log)

        written = [str(c[0][0]) for c in mock_log.write.call_args_list]
        assert any("configured" in w.lower() for w in written)
