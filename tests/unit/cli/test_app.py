"""Tests for hexawyn CLI app startup and license auto-refresh."""

import os
from unittest.mock import MagicMock, patch

import hexawyn.cli.app as app_module
from hexawyn.cli.app import HexawynApp, _load_api_key_to_env
from hexawyn.cli.presentation.formatting import format_size as _format_size


class TestFormatSize:
    def test_kb(self) -> None:
        assert "B" in _format_size(512)

    def test_mb(self) -> None:
        assert "MB" in _format_size(2_000_000)

    def test_gb(self) -> None:
        assert "GB" in _format_size(2_000_000_000)


class TestLoadApiKeyToEnv:
    def test_returns_false_when_no_key(self) -> None:
        with patch(
            "hexawyn.cli.app.get_llm_config",
            return_value={},
        ):
            result = _load_api_key_to_env()
        assert result is False

    def test_returns_true_and_sets_env(self) -> None:
        with patch(
            "hexawyn.cli.app.get_llm_config",
            return_value={"api_key": "sk-test", "base_url": "https://api.test.com"},
        ):
            result = _load_api_key_to_env()
        assert result is True
        assert os.environ.get("LLM_API_KEY") == "sk-test"
        assert os.environ.get("LLM_BASE_URL") == "https://api.test.com"

    def test_sets_key_without_base_url(self) -> None:
        with patch(
            "hexawyn.cli.app.get_llm_config",
            return_value={"api_key": "sk-key"},
        ):
            result = _load_api_key_to_env()
        assert result is True
        assert os.environ.get("LLM_API_KEY") == "sk-key"


class TestAutoRefreshLicense:
    def test_skips_when_no_token(self) -> None:
        app = HexawynApp()
        with (
            patch(
                "hexawyn.infrastructure.config.config_manager.load_config",
                return_value={},
            ),
            patch("httpx.Client") as mock_client_cls,
        ):
            app._auto_refresh_license()
        mock_client_cls.assert_not_called()

    def test_refreshes_license_on_success(self) -> None:
        app = HexawynApp()
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"token": "new_jwt_token"}

        with (
            patch(
                "hexawyn.infrastructure.config.config_manager.load_config",
                return_value={"hexawyn_token": "hxw_live_test"},
            ),
            patch("httpx.Client") as mock_client_cls,
            patch(
                "hexawyn.infrastructure.config.machine_id.get_machine_id",
                return_value="machine-1",
            ),
            patch("pathlib.Path.mkdir"),
            patch("pathlib.Path.write_text") as mock_write,
        ):
            mock_client = MagicMock()
            mock_client.__enter__.return_value = mock_client
            mock_client.post.return_value = mock_resp
            mock_client_cls.return_value = mock_client

            app._auto_refresh_license()

        mock_write.assert_called_once_with("new_jwt_token")

    def test_silently_handles_error(self) -> None:
        app = HexawynApp()
        with (
            patch(
                "hexawyn.infrastructure.config.config_manager.load_config",
                return_value={"hexawyn_token": "hxw_live_test"},
            ),
            patch("httpx.Client", side_effect=Exception("network error")),
        ):
            app._auto_refresh_license()

    def test_silently_handles_http_error_status(self) -> None:
        app = HexawynApp()
        mock_resp = MagicMock()
        mock_resp.status_code = 401

        with (
            patch(
                "hexawyn.infrastructure.config.config_manager.load_config",
                return_value={"hexawyn_token": "hxw_live_test"},
            ),
            patch("httpx.Client") as mock_client_cls,
            patch(
                "hexawyn.infrastructure.config.machine_id.get_machine_id",
                return_value="machine-1",
            ),
            patch("pathlib.Path.write_text") as mock_write,
        ):
            mock_client = MagicMock()
            mock_client.__enter__.return_value = mock_client
            mock_client.post.return_value = mock_resp
            mock_client_cls.return_value = mock_client

            app._auto_refresh_license()

        mock_write.assert_not_called()

    def test_skips_write_when_no_token_in_response(self) -> None:
        app = HexawynApp()
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {}

        with (
            patch(
                "hexawyn.infrastructure.config.config_manager.load_config",
                return_value={"hexawyn_token": "hxw_live_test"},
            ),
            patch("httpx.Client") as mock_client_cls,
            patch(
                "hexawyn.infrastructure.config.machine_id.get_machine_id",
                return_value="machine-1",
            ),
            patch("pathlib.Path.write_text") as mock_write,
        ):
            mock_client = MagicMock()
            mock_client.__enter__.return_value = mock_client
            mock_client.post.return_value = mock_resp
            mock_client_cls.return_value = mock_client

            app._auto_refresh_license()

        mock_write.assert_not_called()


class TestRun:
    def test_run_demo_mode_skips_license_refresh(self) -> None:
        app = HexawynApp()
        app._auto_refresh_license = MagicMock()
        app._run_tui = MagicMock()

        with (
            patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "true"}),
            patch("hexawyn.cli.app._load_api_key_to_env"),
        ):
            app.run()

        app._auto_refresh_license.assert_not_called()
        app._run_tui.assert_called_once()

    def test_run_calls_auto_refresh_in_normal_mode(self) -> None:
        app = HexawynApp()
        app._auto_refresh_license = MagicMock()
        app._run_tui = MagicMock()

        with (
            patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "false"}),
            patch("hexawyn.cli.app._load_api_key_to_env"),
        ):
            app.run()

        app._auto_refresh_license.assert_called_once()

    def test_run_force_setup(self) -> None:
        app = HexawynApp(force_setup=True)
        app._auto_refresh_license = MagicMock()
        app._run_tui = MagicMock()

        with (
            patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "false"}),
            patch("hexawyn.cli.app._load_api_key_to_env"),
        ):
            app.run()

        app._run_tui.assert_called_once_with(needs_setup=True)

    def test_run_force_setup_skipped_in_demo(self) -> None:
        app = HexawynApp(force_setup=True)
        app._auto_refresh_license = MagicMock()
        app._run_tui = MagicMock()

        with (
            patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "true"}),
            patch("hexawyn.cli.app._load_api_key_to_env"),
        ):
            app.run()

        app._run_tui.assert_called_once_with()


class TestRunTui:
    def test_run_tui_demo_mode(self) -> None:
        app = HexawynApp()
        with (
            patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "true"}),
            patch("hexawyn.cli.app.build_adapters") as mock_build,
            patch("hexawyn.cli.app.get_runtime") as mock_runtime,
            patch("hexawyn.cli.tui.HexawynTUI") as mock_tui_cls,
        ):
            mock_adapter = MagicMock()
            mock_build.return_value = mock_adapter
            mock_runtime_obj = MagicMock()
            mock_runtime.return_value = mock_runtime_obj
            mock_tui = MagicMock()
            mock_tui_cls.return_value = mock_tui

            app._run_tui()

            mock_tui_cls.assert_called_once()
            mock_tui.run.assert_called_once()

    def test_run_tui_normal_mode(self) -> None:
        app = HexawynApp()
        with (
            patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "false"}),
            patch("hexawyn.cli.app.FileKubernetesDiscoveryService") as mock_discovery,
            patch("hexawyn.cli.app.build_adapters") as mock_build,
            patch("hexawyn.cli.app.get_runtime") as mock_runtime,
            patch("hexawyn.cli.tui.HexawynTUI") as mock_tui_cls,
        ):
            mock_discovery_instance = MagicMock()
            mock_discovery_instance.current.return_value = None
            mock_discovery.return_value = mock_discovery_instance

            mock_adapter = MagicMock()
            mock_build.return_value = mock_adapter
            mock_runtime_obj = MagicMock()
            mock_runtime.return_value = mock_runtime_obj
            mock_tui = MagicMock()
            mock_tui_cls.return_value = mock_tui

            app._run_tui()

            mock_tui_cls.assert_called_once()
            mock_tui.run.assert_called_once()

    def test_run_tui_with_current_context(self) -> None:
        from hexawyn.infrastructure.config.kubernetes_context import ClusterContext

        app = HexawynApp()
        ctx = ClusterContext(
            name="prod-eu", cluster="prod-eu", namespace="default", user="u", is_current=True
        )
        with (
            patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "false"}),
            patch("hexawyn.cli.app.FileKubernetesDiscoveryService") as mock_discovery,
            patch("hexawyn.cli.app.build_adapters") as mock_build,
            patch("hexawyn.cli.app.get_runtime") as mock_runtime,
            patch("hexawyn.cli.tui.HexawynTUI") as mock_tui_cls,
        ):
            mock_discovery_instance = MagicMock()
            mock_discovery_instance.current.return_value = ctx
            mock_discovery.return_value = mock_discovery_instance

            mock_adapter = MagicMock()
            mock_build.return_value = mock_adapter
            mock_runtime_obj = MagicMock()
            mock_runtime.return_value = mock_runtime_obj
            mock_tui = MagicMock()
            mock_tui_cls.return_value = mock_tui

            app._run_tui()

            mock_build.assert_called_once_with("prod-eu")
            mock_tui.run.assert_called_once()

    def test_run_tui_with_db_warning(self) -> None:
        app = HexawynApp()
        with (
            patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "false"}),
            patch("hexawyn.cli.app.FileKubernetesDiscoveryService") as mock_discovery,
            patch("hexawyn.cli.app.build_adapters") as mock_build,
            patch("hexawyn.cli.app.get_runtime") as mock_runtime,
            patch("hexawyn.cli.tui.HexawynTUI") as mock_tui_cls,
            patch.object(app_module, "get_db_size_bytes", return_value=2_000_000_000),
        ):
            mock_discovery_instance = MagicMock()
            mock_discovery_instance.current.return_value = None
            mock_discovery.return_value = mock_discovery_instance

            mock_adapter = MagicMock()
            mock_build.return_value = mock_adapter
            mock_runtime_obj = MagicMock()
            mock_runtime.return_value = mock_runtime_obj
            mock_tui = MagicMock()
            mock_tui_cls.return_value = mock_tui

            app._run_tui()

            call_kwargs = mock_tui_cls.call_args[1]
            assert call_kwargs["extra_chip"] is not None
            assert "DB:" in call_kwargs["extra_chip"]
            mock_tui.run.assert_called_once()


class TestProviders:
    def test_all_providers_have_required_fields(self) -> None:
        from hexawyn.cli.app import _PROVIDERS

        for key, provider in _PROVIDERS.items():
            assert "name" in provider
            assert "base_url" in provider
            assert "env_key" in provider
