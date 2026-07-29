from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.cli.app import HexawynApp, _load_api_key_to_env


class TestLoadApiKeyToEnv:
    def test_configured_with_api_key(self) -> None:
        with (
            patch("hexawyn.cli.app.get_llm_config") as mock_cfg,
            patch("hexawyn.cli.app.os.environ", {}),
        ):
            mock_cfg.return_value = {"api_key": "test-key", "base_url": "http://localhost"}
            assert _load_api_key_to_env() is True

    def test_configured_with_api_key_no_base_url(self) -> None:
        with (
            patch("hexawyn.cli.app.get_llm_config") as mock_cfg,
            patch("hexawyn.cli.app.os.environ", {}),
        ):
            mock_cfg.return_value = {"api_key": "test-key"}
            assert _load_api_key_to_env() is True

    def test_not_configured_no_api_key(self) -> None:
        with patch("hexawyn.cli.app.get_llm_config") as mock_cfg:
            mock_cfg.return_value = {}
            assert _load_api_key_to_env() is False

    def test_not_configured_empty_config(self) -> None:
        with patch("hexawyn.cli.app.get_llm_config") as mock_cfg:
            mock_cfg.return_value = {"api_key": ""}
            assert _load_api_key_to_env() is False


class TestHexawynApp:
    def test_init_defaults(self) -> None:
        app = HexawynApp()
        assert app.expert_mode is False
        assert app.force_setup is False

    def test_init_expert_mode(self) -> None:
        app = HexawynApp(expert_mode=True)
        assert app.expert_mode is True

    def test_init_force_setup(self) -> None:
        app = HexawynApp(force_setup=True)
        assert app.force_setup is True

    def test_auto_refresh_license_success(self) -> None:
        app = HexawynApp()
        with patch(
            "hexawyn.infrastructure.license.license_reader.refresh_license", return_value=True
        ):
            app._auto_refresh_license()

    def test_auto_refresh_license_failure(self) -> None:
        app = HexawynApp()
        with patch(
            "hexawyn.infrastructure.license.license_reader.refresh_license", return_value=False
        ):
            app._auto_refresh_license()

    def test_run_demo_mode(self) -> None:
        app = HexawynApp()
        with (
            patch("hexawyn.cli.app.os.environ", {"HEXAWYN_DEMO_MODE": "true"}),
            patch("hexawyn.cli.app._load_api_key_to_env"),
            patch("hexawyn.cli.tui.HexawynTUI") as mock_tui,
        ):
            app.run()
            mock_tui.return_value.run.assert_called_once()

    def test_run_with_force_setup_not_demo(self) -> None:
        app = HexawynApp(force_setup=True)
        with (
            patch("hexawyn.cli.app.os.environ", {"HEXAWYN_DEMO_MODE": "false"}),
            patch("hexawyn.cli.app._load_api_key_to_env"),
            patch("hexawyn.cli.tui.HexawynTUI") as mock_tui,
            patch("hexawyn.adapters.secondary.adapter_factory.build_adapters"),
            patch("hexawyn.application.service.runtime_adapter.get_runtime") as mock_runtime,
            patch(
                "hexawyn.infrastructure.config.kubernetes_context.FileKubernetesDiscoveryService"
            ) as mock_svc,
            patch("hexawyn.infrastructure.memory.duckdb_client.get_db_size_bytes", return_value=0),
        ):
            mock_runtime.return_value = MagicMock()
            mock_svc.return_value.current.return_value = None
            app.run()
            tui_instance = mock_tui.return_value
            tui_instance.run.assert_called_once()
            call_kwargs = mock_tui.call_args[1]
            assert call_kwargs["needs_setup"] is True

    def test_run_tui_normal(self) -> None:
        app = HexawynApp()
        with (
            patch("hexawyn.cli.app.os.environ", {"HEXAWYN_DEMO_MODE": "false"}),
            patch("hexawyn.cli.tui.HexawynTUI") as mock_tui,
            patch("hexawyn.adapters.secondary.adapter_factory.build_adapters"),
            patch("hexawyn.application.service.runtime_adapter.get_runtime") as mock_runtime,
            patch(
                "hexawyn.infrastructure.config.kubernetes_context.FileKubernetesDiscoveryService"
            ) as mock_svc,
            patch("hexawyn.infrastructure.memory.duckdb_client.get_db_size_bytes", return_value=0),
        ):
            mock_runtime.return_value = MagicMock()
            mock_svc.return_value.current.return_value = None
            app._run_tui()
            mock_tui.return_value.run.assert_called_once()

    def test_run_tui_db_size_warning(self) -> None:
        app = HexawynApp(expert_mode=False)
        with (
            patch("hexawyn.cli.app.os.environ", {"HEXAWYN_DEMO_MODE": "false"}),
            patch("hexawyn.cli.tui.HexawynTUI") as mock_tui,
            patch("hexawyn.adapters.secondary.adapter_factory.build_adapters"),
            patch("hexawyn.application.service.runtime_adapter.get_runtime") as mock_runtime,
            patch(
                "hexawyn.infrastructure.config.kubernetes_context.FileKubernetesDiscoveryService"
            ) as mock_svc,
            patch(
                "hexawyn.infrastructure.memory.duckdb_client.get_db_size_bytes",
                return_value=2_000_000_000,
            ),
            patch("hexawyn.cli.app._DB_SIZE_WARNING_THRESHOLD", 1_000_000_000),
        ):
            mock_runtime.return_value = MagicMock()
            mock_svc.return_value.current.return_value = None
            app._run_tui()
            call_kwargs = mock_tui.call_args[1]
            assert call_kwargs["expert_mode"] is False

    def test_run_tui_expert_mode_skips_db_check(self) -> None:
        app = HexawynApp(expert_mode=True)
        with (
            patch("hexawyn.cli.app.os.environ", {"HEXAWYN_DEMO_MODE": "false"}),
            patch("hexawyn.cli.tui.HexawynTUI") as mock_tui,
            patch("hexawyn.adapters.secondary.adapter_factory.build_adapters"),
            patch("hexawyn.application.service.runtime_adapter.get_runtime") as mock_runtime,
            patch(
                "hexawyn.infrastructure.config.kubernetes_context.FileKubernetesDiscoveryService"
            ) as mock_svc,
        ):
            mock_runtime.return_value = MagicMock()
            mock_svc.return_value.current.return_value = None
            app._run_tui()
            call_kwargs = mock_tui.call_args[1]
            assert call_kwargs["extra_chip"] is None
