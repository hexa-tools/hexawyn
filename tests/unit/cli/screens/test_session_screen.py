from unittest.mock import MagicMock, patch

from hexawyn.cli.screens.session import SessionScreen


class TestIsContextCommand:
    def test_slash_context_is_recognized(self) -> None:
        from hexawyn.cli.presentation.command_router import is_context_command

        assert is_context_command("/context") is True

    def test_slash_ctx_is_recognized(self) -> None:
        from hexawyn.cli.presentation.command_router import is_context_command

        assert is_context_command("/ctx") is True

    def test_slash_ctx_with_args_is_recognized(self) -> None:
        from hexawyn.cli.presentation.command_router import is_context_command

        assert is_context_command("/ctx prod-cluster") is True

    def test_regular_command_is_not_context(self) -> None:
        from hexawyn.cli.presentation.command_router import is_context_command

        assert is_context_command("list pods") is False

    def test_empty_string_is_not_context(self) -> None:
        from hexawyn.cli.presentation.command_router import is_context_command

        assert is_context_command("") is False

    def test_slash_setup_is_not_context(self) -> None:
        from hexawyn.cli.presentation.command_router import is_context_command

        assert is_context_command("/setup") is False


class TestIsStackCommand:
    def test_slash_stack_is_recognized(self) -> None:
        from hexawyn.cli.presentation.command_router import is_stack_command

        assert is_stack_command("/stack") is True

    def test_slash_stack_with_args_is_recognized(self) -> None:
        from hexawyn.cli.presentation.command_router import is_stack_command

        assert is_stack_command("/stack aws") is True

    def test_regular_command_is_not_stack(self) -> None:
        from hexawyn.cli.presentation.command_router import is_stack_command

        assert is_stack_command("/ctx") is False


class TestHandleStackCommand:
    def test_renders_run_stack_command_output(self) -> None:
        screen = SessionScreen()
        app = MagicMock()
        app.cluster_name = "prod-eks"
        log = MagicMock()

        with (
            patch.object(screen, "_tui_app", return_value=app),
            patch(
                "hexawyn.cli.presentation.stack_view.run_stack_command",
                return_value=[("Stack forced to 'aws'.", "green")],
            ) as run_stack,
        ):
            screen._handle_stack_command("/stack aws", log)

        run_stack.assert_called_once_with("/stack aws", "prod-eks")
        log.write.assert_called()

    def test_defaults_context_name_when_missing(self) -> None:
        screen = SessionScreen()
        app = MagicMock()
        app.cluster_name = None
        log = MagicMock()

        with (
            patch.object(screen, "_tui_app", return_value=app),
            patch(
                "hexawyn.cli.presentation.stack_view.run_stack_command",
                return_value=[],
            ) as run_stack,
        ):
            screen._handle_stack_command("/stack", log)

        run_stack.assert_called_once_with("/stack", "default")


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
        from hexawyn.cli.presentation.findings import format_finding_warnings

        findings = [
            {"type": "CrashLoopBackOff", "severity": "high"},
            {"type": "Other", "severity": "low"},
        ]
        with (
            patch("hexawyn.cli.presentation.findings.crashloop_finding_count", return_value=2),
            patch("hexawyn.cli.presentation.findings.restarting_finding_count", return_value=0),
        ):
            lines = format_finding_warnings(findings)
        assert any("2 CrashLoopBackOff detected" in line for line in lines)
        assert any("\u26a0" in line for line in lines)

    def test_restarting_frequently(self) -> None:
        from hexawyn.cli.presentation.findings import format_finding_warnings

        findings = [{"type": "anything"}]
        with (
            patch("hexawyn.cli.presentation.findings.crashloop_finding_count", return_value=0),
            patch("hexawyn.cli.presentation.findings.restarting_finding_count", return_value=3),
        ):
            lines = format_finding_warnings(findings)
        assert any("3 pods with high restart count" in line for line in lines)

    def test_no_warnings(self) -> None:
        from hexawyn.cli.presentation.findings import format_finding_warnings

        findings: list[dict[str, object]] = []
        with (
            patch("hexawyn.cli.presentation.findings.crashloop_finding_count", return_value=0),
            patch("hexawyn.cli.presentation.findings.restarting_finding_count", return_value=0),
        ):
            lines = format_finding_warnings(findings)
        assert any("No active warnings" in line for line in lines)
        assert any("green" in line for line in lines)


class TestContextSwitchLines:
    def test_successful_switch(self) -> None:
        from hexawyn.cli.presentation.context_display import format_context_switch_lines
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
        lines = format_context_switch_lines(result)

        texts = [text for text, _ in lines]
        assert "\u2713 Context switched" in texts
        assert any("Current context: prod-eu" in t for t in texts)

    def test_connection_failed(self) -> None:
        from hexawyn.cli.presentation.context_display import format_context_switch_lines
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
        lines = format_context_switch_lines(result)

        texts = [text for text, _ in lines]
        assert any("Connection failed" in t for t in texts)

    def test_no_current_context(self) -> None:
        from hexawyn.cli.presentation.context_display import format_context_switch_lines
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
        lines = format_context_switch_lines(result)

        texts = [text for text, _ in lines]
        assert any("Context switch failed" in t for t in texts)


class TestRenderLines:
    def test_renders_single_line(self) -> None:
        from hexawyn.cli.presentation.response_renderer import render_lines

        mock_log = MagicMock()
        lines = [("hello world", "bold")]

        render_lines(mock_log, lines)

        mock_log.write.assert_called_once()
        assert "[bold]hello world[/bold]" in str(mock_log.write.call_args[0][0])

    def test_renders_empty_text_as_blank(self) -> None:
        from hexawyn.cli.presentation.response_renderer import render_lines

        mock_log = MagicMock()
        lines = [("", "dim"), ("visible", "green")]

        render_lines(mock_log, lines)

        assert mock_log.write.call_count == 2
        assert str(mock_log.write.call_args_list[0][0][0]) == ""

    def test_renders_multiple_lines(self) -> None:
        from hexawyn.cli.presentation.response_renderer import render_lines

        mock_log = MagicMock()
        lines = [("line1", "bold"), ("line2", "dim"), ("line3", "red")]

        render_lines(mock_log, lines)

        assert mock_log.write.call_count == 3


class TestRenderSetupInfo:
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

        assert mock_log.write.call_count >= 3

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


class TestActionManageSubscription:
    def test_opens_with_token(self) -> None:
        screen = SessionScreen()
        with (
            patch(
                "hexawyn.infrastructure.config.config_manager.load_config",
                return_value={"hexawyn_token": "hxw_live_test"},
            ),
            patch("webbrowser.open") as mock_browser,
            patch.object(screen, "notify") as mock_notify,
        ):
            screen.action_manage_subscription()
        mock_browser.assert_called_once_with("https://hexawyn.com/account/manage?key=hxw_live_test")
        mock_notify.assert_called_once()

    def test_opens_without_token(self) -> None:
        screen = SessionScreen()
        with (
            patch(
                "hexawyn.infrastructure.config.config_manager.load_config",
                return_value={},
            ),
            patch("webbrowser.open") as mock_browser,
            patch.object(screen, "notify") as mock_notify,
        ):
            screen.action_manage_subscription()
        mock_browser.assert_called_once_with("https://hexawyn.com/account/manage")
        mock_notify.assert_called_once()


class TestLicenseAsideLines:
    def test_no_license_file(self) -> None:
        from hexawyn.cli.presentation.license_display import format_license_aside_lines

        with patch("hexawyn.cli.presentation.license_display.read_license_state") as mock_read:
            from hexawyn.domain.services.license_state import LicenseState

            mock_read.return_value = LicenseState(
                state="missing", plan="unknown", days_remaining=0, expiry_date=""
            )
            lines = format_license_aside_lines()
        assert any("not configured" in line for line in lines)

    def test_invalid_jwt_format(self) -> None:
        from hexawyn.cli.presentation.license_display import format_license_aside_lines

        with patch("hexawyn.cli.presentation.license_display.read_license_state") as mock_read:
            from hexawyn.domain.services.license_state import LicenseState

            mock_read.return_value = LicenseState(
                state="invalid", plan="unknown", days_remaining=0, expiry_date=""
            )
            lines = format_license_aside_lines()
        assert any("invalid" in line for line in lines)

    def test_valid_license(self) -> None:
        from hexawyn.cli.presentation.license_display import format_license_aside_lines

        with patch("hexawyn.cli.presentation.license_display.read_license_state") as mock_read:
            from hexawyn.domain.services.license_state import LicenseState

            mock_read.return_value = LicenseState(
                state="active", plan="starter", days_remaining=30, expiry_date="19 Aug 2026"
            )
            lines = format_license_aside_lines()
        assert any("License: Starter" in line for line in lines)
        assert any("Expires:" in line for line in lines)

    def test_expired_license(self) -> None:
        from hexawyn.cli.presentation.license_display import format_license_aside_lines

        with patch("hexawyn.cli.presentation.license_display.read_license_state") as mock_read:
            from hexawyn.domain.services.license_state import LicenseState

            mock_read.return_value = LicenseState(
                state="expired", plan="starter", days_remaining=-1, expiry_date="19 Jul 2026"
            )
            lines = format_license_aside_lines()
        assert any("expired" in line for line in lines)

    def test_error_returns_not_configured(self) -> None:
        from hexawyn.cli.presentation.license_display import format_license_aside_lines

        with patch("hexawyn.cli.presentation.license_display.read_license_state") as mock_read:
            from hexawyn.domain.services.license_state import LicenseState

            mock_read.return_value = LicenseState(
                state="missing", plan="unknown", days_remaining=0, expiry_date=""
            )
            lines = format_license_aside_lines()
        assert any("not configured" in line for line in lines)


class TestRefreshFooter:
    def test_active_license_shows_manage(self) -> None:
        from hexawyn.domain.services.license_state import LicenseState

        screen = SessionScreen()
        mock_static = MagicMock()
        with (
            patch(
                "hexawyn.infrastructure.license.license_reader.read_license_state",
                return_value=LicenseState(
                    state="active", plan="starter", days_remaining=30, expiry_date="19 Aug 2026"
                ),
            ),
            patch.object(screen, "query_one", return_value=mock_static),
        ):
            screen._refresh_footer()
        call_text = str(mock_static.update.call_args[0][0])
        assert "manage" in call_text
        assert "upgrade" not in call_text

    def test_expired_license_shows_upgrade(self) -> None:
        from hexawyn.domain.services.license_state import LicenseState

        screen = SessionScreen()
        mock_static = MagicMock()
        with (
            patch(
                "hexawyn.infrastructure.license.license_reader.read_license_state",
                return_value=LicenseState(
                    state="expired", plan="starter", days_remaining=-1, expiry_date="19 Jul 2026"
                ),
            ),
            patch.object(screen, "query_one", return_value=mock_static),
        ):
            screen._refresh_footer()
        call_text = str(mock_static.update.call_args[0][0])
        assert "upgrade" in call_text

    def test_warning_license_shows_upgrade_in_dim(self) -> None:
        from hexawyn.domain.services.license_state import LicenseState

        screen = SessionScreen()
        mock_static = MagicMock()
        with (
            patch(
                "hexawyn.infrastructure.license.license_reader.read_license_state",
                return_value=LicenseState(
                    state="warning", plan="starter", days_remaining=3, expiry_date="23 Jul 2026"
                ),
            ),
            patch.object(screen, "query_one", return_value=mock_static),
        ):
            screen._refresh_footer()
        call_text = str(mock_static.update.call_args[0][0])
        assert "upgrade" in call_text
        assert "[dim]upgrade" in call_text or "#f97316" in call_text


class TestSuggestionLines:
    def test_ai_suggestion(self) -> None:
        from hexawyn.cli.presentation.suggestions import format_suggestion_lines

        app = MagicMock()
        app.ai_suggestion = "Try checking your pod limits"
        app.startup_result = None

        lines = format_suggestion_lines(app, [])
        assert any("Try checking your pod limits" in line for line in lines)

    def test_startup_suggestions(self) -> None:
        from hexawyn.cli.presentation.suggestions import format_suggestion_lines

        app = MagicMock()
        app.ai_suggestion = None
        app.startup_result = {
            "suggestions": [
                {
                    "label": "Fix CrashLoop",
                    "explanation": "Pod is crashing",
                    "severity": "critical",
                },
                {"label": "Scale up", "explanation": "Need more resources", "severity": "warning"},
                {"label": "Just info", "explanation": "", "severity": "info"},
            ]
        }

        lines = format_suggestion_lines(app, [])
        assert any("Fix CrashLoop" in line for line in lines)
        assert any("Pod is crashing" in line for line in lines)
        assert any("\U0001f534" in line for line in lines)
        assert any("\U0001f7e1" in line for line in lines)
        assert any("Scale up" in line for line in lines)
        assert any("Just info" in line for line in lines)

    def test_startup_suggestion_with_label_only(self) -> None:
        from hexawyn.cli.presentation.suggestions import format_suggestion_lines

        app = MagicMock()
        app.ai_suggestion = None
        app.startup_result = {
            "suggestions": [
                {"label": "Restart needed", "explanation": "", "severity": "info"},
            ]
        }

        lines = format_suggestion_lines(app, [])
        assert any("Restart needed" in line for line in lines)

    def test_narrative_summary(self) -> None:
        from hexawyn.cli.presentation.suggestions import format_suggestion_lines

        app = MagicMock()
        app.ai_suggestion = None
        app.startup_result = {
            "narrative_summary": "Cluster looks healthy overall",
        }

        lines = format_suggestion_lines(app, [])
        assert any("Cluster looks healthy overall" in line for line in lines)

    def test_skips_error_narrative(self) -> None:
        from hexawyn.cli.presentation.suggestions import format_suggestion_lines

        app = MagicMock()
        app.ai_suggestion = None
        app.startup_result = {
            "narrative_summary": "Runtime not available. Please check your configuration.",
        }

        lines = format_suggestion_lines(app, [])
        assert not any("Runtime not available" in line for line in lines)

    def test_fallback_suggestions(self) -> None:
        from hexawyn.cli.presentation.suggestions import format_suggestion_lines

        app = MagicMock()
        app.ai_suggestion = None
        app.startup_result = None

        lines = format_suggestion_lines(app, ["sug1", "sug2", "sug3", "sug4", "sug5"])
        assert any("sug1" in line for line in lines)
        assert any("sug4" in line for line in lines)
        assert not any("sug5" in line for line in lines)
