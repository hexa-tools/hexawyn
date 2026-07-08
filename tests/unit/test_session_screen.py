from unittest.mock import MagicMock, patch

from hexawyn.cli.screens.session import SessionScreen


class TestIsContextCommand:
    def test_slash_context_is_recognized(self) -> None:
        screen = SessionScreen()
        assert screen._is_context_command("/context") is True

    def test_slash_ctx_is_recognized(self) -> None:
        screen = SessionScreen()
        assert screen._is_context_command("/ctx") is True

    def test_slash_ctx_with_args_is_recognized(self) -> None:
        screen = SessionScreen()
        assert screen._is_context_command("/ctx prod-cluster") is True

    def test_regular_command_is_not_context(self) -> None:
        screen = SessionScreen()
        assert screen._is_context_command("list pods") is False

    def test_empty_string_is_not_context(self) -> None:
        screen = SessionScreen()
        assert screen._is_context_command("") is False

    def test_slash_setup_is_not_context(self) -> None:
        screen = SessionScreen()
        assert screen._is_context_command("/setup") is False


class TestRequestedContextName:
    def test_no_args_returns_none(self) -> None:
        screen = SessionScreen()
        result = screen._requested_context_name("/context")
        assert result is None

    def test_with_args_returns_name(self) -> None:
        screen = SessionScreen()
        result = screen._requested_context_name("/context prod-eu")
        assert result == "prod-eu"

    def test_whitespace_only_args_returns_none(self) -> None:
        screen = SessionScreen()
        result = screen._requested_context_name("/ctx   ")
        assert result is None

    def test_multiple_words_returns_full_remainder(self) -> None:
        screen = SessionScreen()
        result = screen._requested_context_name("/ctx kind-ecom-local extra")
        assert result == "kind-ecom-local extra"


class TestFindingWarningLines:
    def test_crashloop_detected(self) -> None:
        screen = SessionScreen()
        findings = [
            {"type": "CrashLoopBackOff", "severity": "high"},
            {"type": "Other", "severity": "low"},
        ]
        with patch("hexawyn.cli.screens.session.crashloop_finding_count", return_value=2):
            with patch("hexawyn.cli.screens.session.restarting_finding_count", return_value=0):
                lines = screen._finding_warning_lines(findings)
        assert any("2 CrashLoopBackOff detected" in line for line in lines)
        assert any("⚠" in line for line in lines)

    def test_restarting_frequently(self) -> None:
        screen = SessionScreen()
        findings = [{"type": "anything"}]
        with patch("hexawyn.cli.screens.session.crashloop_finding_count", return_value=0):
            with patch("hexawyn.cli.screens.session.restarting_finding_count", return_value=3):
                lines = screen._finding_warning_lines(findings)
        assert any("3 pods with high restart count" in line for line in lines)

    def test_no_warnings(self) -> None:
        screen = SessionScreen()
        findings: list[dict] = []
        with patch("hexawyn.cli.screens.session.crashloop_finding_count", return_value=0):
            with patch("hexawyn.cli.screens.session.restarting_finding_count", return_value=0):
                lines = screen._finding_warning_lines(findings)
        assert any("No active warnings" in line for line in lines)
        assert any("green" in line for line in lines)


class TestContextSwitchLines:
    def test_successful_switch(self) -> None:
        from hexawyn.infrastructure.config.kubernetes_context import (
            ClusterContext,
            KubernetesContextSwitchResult,
        )

        ctx = ClusterContext(
            name="prod-eu", cluster="prod-eu", namespace="default", user="admin", is_current=True
        )
        result = KubernetesContextSwitchResult(
            contexts=[ctx],
            current_context=ctx,
            connected=True,
            switched=True,
            kubeconfig_paths=[],
        )
        screen = SessionScreen()
        lines = screen._context_switch_lines(result)

        texts = [text for text, _ in lines]
        assert "✓ Context switched" in texts
        assert any("Current context: prod-eu" in t for t in texts)

    def test_connection_failed(self) -> None:
        from hexawyn.infrastructure.config.kubernetes_context import (
            ClusterContext,
            KubernetesContextSwitchResult,
        )

        ctx = ClusterContext(
            name="bad-cluster",
            cluster="bad-cluster",
            namespace="default",
            user="admin",
            is_current=True,
        )
        result = KubernetesContextSwitchResult(
            contexts=[ctx],
            current_context=ctx,
            connected=False,
            switched=True,
            kubeconfig_paths=[],
            connection_error="timeout",
        )
        screen = SessionScreen()
        lines = screen._context_switch_lines(result)

        texts = [text for text, _ in lines]
        assert any("Connection failed" in t for t in texts)

    def test_no_current_context(self) -> None:
        from hexawyn.infrastructure.config.kubernetes_context import (
            KubernetesContextSwitchResult,
        )

        result = KubernetesContextSwitchResult(
            contexts=[],
            current_context=None,
            connected=False,
            switched=False,
            kubeconfig_paths=[],
        )
        screen = SessionScreen()
        lines = screen._context_switch_lines(result)

        texts = [text for text, _ in lines]
        assert any("Context switch failed" in t for t in texts)


class TestRenderLines:
    def test_renders_single_line(self) -> None:
        screen = SessionScreen()
        mock_log = MagicMock()
        lines = [("hello world", "bold")]

        screen._render_lines(mock_log, lines)

        mock_log.write.assert_called_once()
        assert "[bold]hello world[/bold]" in str(mock_log.write.call_args[0][0])

    def test_renders_empty_text_as_blank(self) -> None:
        screen = SessionScreen()
        mock_log = MagicMock()
        lines = [("", "dim"), ("visible", "green")]

        screen._render_lines(mock_log, lines)

        assert mock_log.write.call_count == 2
        assert str(mock_log.write.call_args_list[0][0][0]) == ""

    def test_renders_multiple_lines(self) -> None:
        screen = SessionScreen()
        mock_log = MagicMock()
        lines = [("line1", "bold"), ("line2", "dim"), ("line3", "red")]

        screen._render_lines(mock_log, lines)

        assert mock_log.write.call_count == 3


class TestRenderSetupInfo:
    def test_shows_provider_info(self) -> None:
        screen = SessionScreen()
        mock_log = MagicMock()

        with patch(
            "hexawyn.infrastructure.config.config_manager.get_llm_config",
            return_value={
                "provider": "openai",
                "base_url": "https://api.openai.com",
                "api_key": "sk-test",
            },
        ):
            screen._render_setup_info(mock_log)

        assert mock_log.write.call_count >= 3

    def test_shows_missing_key_warning(self) -> None:
        screen = SessionScreen()
        mock_log = MagicMock()

        with patch(
            "hexawyn.infrastructure.config.config_manager.get_llm_config",
            return_value={
                "provider": "openai",
                "base_url": "https://api.openai.com",
                "api_key": "",
            },
        ):
            screen._render_setup_info(mock_log)

        written = [str(c[0][0]) for c in mock_log.write.call_args_list]
        assert any("missing" in w.lower() for w in written)

    def test_shows_configured_key(self) -> None:
        screen = SessionScreen()
        mock_log = MagicMock()

        with patch(
            "hexawyn.infrastructure.config.config_manager.get_llm_config",
            return_value={
                "provider": "openai",
                "base_url": "https://api.openai.com",
                "api_key": "sk-key",
            },
        ):
            screen._render_setup_info(mock_log)

        written = [str(c[0][0]) for c in mock_log.write.call_args_list]
        assert any("configured" in w.lower() for w in written)


class TestAvailableContexts:
    def test_uses_context_service_when_available(self) -> None:
        from hexawyn.infrastructure.config.kubernetes_context import ClusterContext

        screen = SessionScreen()
        mock_app = MagicMock()
        mock_app.context_service = MagicMock()
        mock_app.context_service.discover.return_value = [
            ClusterContext(
                name="prod", cluster="prod", namespace="default", user="u", is_current=True
            )
        ]
        mock_app.startup_status = None
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]

        result = screen._available_contexts()

        assert len(result) == 1
        assert result[0].name == "prod"

    def test_falls_back_to_startup_status(self) -> None:
        from hexawyn.infrastructure.config.kubernetes_context import (
            ClusterContext,
            KubernetesStartupStatus,
        )

        screen = SessionScreen()
        mock_app = MagicMock()
        mock_app.context_service = None
        mock_app.startup_status = KubernetesStartupStatus(
            contexts=[
                ClusterContext(
                    name="kind", cluster="kind", namespace="default", user="u", is_current=True
                )
            ],
            current_context=None,
            connected=True,
            kubeconfig_paths=[],
        )
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]

        result = screen._available_contexts()

        assert len(result) == 1
        assert result[0].name == "kind"

    def test_returns_empty_list_when_nothing_available(self) -> None:
        screen = SessionScreen()
        mock_app = MagicMock()
        mock_app.context_service = None
        mock_app.startup_status = None
        screen._tui_app = MagicMock(return_value=mock_app)  # type: ignore[method-assign]

        result = screen._available_contexts()

        assert result == []
