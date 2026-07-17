"""Tests for app.py module-level functions and session.py standalone methods."""

from unittest.mock import patch

from hexawyn.cli.app import _format_size


class TestFormatSize:
    def test_bytes_as_kb(self) -> None:
        result = _format_size(500)
        assert "KB" in result

    def test_kilobytes(self) -> None:
        result = _format_size(2048)
        assert "KB" in result

    def test_megabytes(self) -> None:
        result = _format_size(5_000_000)
        assert "MB" in result

    def test_gigabytes(self) -> None:
        result = _format_size(5_000_000_000)
        assert "GB" in result

    def test_zero(self) -> None:
        result = _format_size(0)
        assert "KB" in result


class TestLoadApiKeyToEnv:
    def test_loads_api_key_and_base_url(self) -> None:
        with patch(
            "hexawyn.cli.app.get_llm_config",
            return_value={"api_key": "sk-test", "base_url": "http://test"},
        ):
            with patch.dict("os.environ", {}, clear=True):
                from hexawyn.cli.app import _load_api_key_to_env

                result = _load_api_key_to_env()
                assert result is True


class TestSessionScreenHelpers:
    def test_is_context_command(self) -> None:
        from hexawyn.cli.screens.session import SessionScreen

        screen = SessionScreen()
        assert screen._is_context_command("/context") is True
        assert screen._is_context_command("/ctx") is True
        assert screen._is_context_command("/help") is False
        assert screen._is_context_command("") is False

    def test_requested_context_name(self) -> None:
        from hexawyn.cli.screens.session import SessionScreen

        screen = SessionScreen()
        assert screen._requested_context_name("/context prod-cluster") == "prod-cluster"
        assert screen._requested_context_name("/ctx staging") == "staging"
        assert screen._requested_context_name("/context") is None
        assert screen._requested_context_name("/ctx") is None

    def test_context_switch_lines_with_success(self) -> None:
        from pathlib import Path

        from hexawyn.cli.screens.session import SessionScreen
        from hexawyn.infrastructure.config.kubernetes_context import (
            ClusterContext,
            KubernetesContextSwitchResult,
        )

        screen = SessionScreen()
        ctx = ClusterContext(
            name="prod", namespace="default", cluster="c1", user="u1", is_current=True
        )
        result = KubernetesContextSwitchResult(
            contexts=[ctx],
            current_context=ctx,
            connected=True,
            switched=True,
            kubeconfig_paths=[Path("/fake/kubeconfig")],
        )
        lines = screen._context_switch_lines(result)
        assert len(lines) > 0

    def test_context_switch_lines_with_failure(self) -> None:
        from pathlib import Path

        from hexawyn.cli.screens.session import SessionScreen
        from hexawyn.infrastructure.config.kubernetes_context import KubernetesContextSwitchResult

        screen = SessionScreen()
        result = KubernetesContextSwitchResult(
            contexts=[],
            current_context=None,
            connected=False,
            switched=False,
            kubeconfig_paths=[Path("/fake/kubeconfig")],
            connection_error="timeout",
        )
        lines = screen._context_switch_lines(result)
        assert len(lines) > 0


class TestAppProviders:
    def test_providers_has_deepseek(self) -> None:
        from hexawyn.cli.app import _PROVIDERS

        assert "1" in _PROVIDERS
        assert _PROVIDERS["1"]["name"] == "DeepSeek"

    def test_providers_has_openai(self) -> None:
        from hexawyn.cli.app import _PROVIDERS

        assert "2" in _PROVIDERS

    def test_custom_provider_exists(self) -> None:
        from hexawyn.cli.app import _PROVIDERS

        assert "0" in _PROVIDERS
        assert _PROVIDERS["0"]["name"] == "Custom"


class TestHexawynApp:
    def test_app_init_defaults(self) -> None:
        from hexawyn.cli.app import HexawynApp

        app = HexawynApp()
        assert app.expert_mode is False
        assert app.force_setup is False

    def test_app_init_expert(self) -> None:
        from hexawyn.cli.app import HexawynApp

        app = HexawynApp(expert_mode=True)
        assert app.expert_mode is True


class TestSessionScreenInit:
    def test_init_stores_command(self) -> None:
        from hexawyn.cli.screens.session import SessionScreen

        screen = SessionScreen(initial_command="list pods")
        assert screen.initial_command == "list pods"

    def test_init_defaults(self) -> None:
        from hexawyn.cli.screens.session import SessionScreen

        screen = SessionScreen()
        assert screen.initial_command is None
