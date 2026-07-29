"""Tests for CLI presentation layer — pure functions with no TUI dependency."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.cli.presentation.command_router import (
    extract_requested_context,
    is_context_command,
    is_refresh_command,
    is_setup_command,
    is_stack_command,
    is_token_command,
)
from hexawyn.cli.presentation.context_display import format_context_switch_lines
from hexawyn.cli.presentation.license_display import (
    format_license_aside_lines,
    format_license_footer_hint,
)
from hexawyn.cli.presentation.suggestions import format_suggestion_lines
from hexawyn.infrastructure.config.kubernetes_context import (
    ClusterContext,
    KubernetesContextSwitchResult,
)


class TestCommandRouter:
    """Cover is_*_command and extract_requested_context (6 functions)."""

    def test_is_context_command_with_slash_context(self) -> None:
        assert is_context_command("/context") is True
        assert is_context_command("/context prod-eu") is True
        assert is_context_command("  /context xyz  ") is True

    def test_is_context_command_with_slash_ctx(self) -> None:
        assert is_context_command("/ctx") is True
        assert is_context_command("/ctx staging") is True

    def test_is_context_command_false(self) -> None:
        assert is_context_command("/token") is False
        assert is_context_command("why is it crashing") is False
        assert is_context_command("") is False

    def test_is_token_command(self) -> None:
        assert is_token_command("/token") is True
        assert is_token_command("/token sk-xxx") is True
        assert is_token_command("/context") is False
        assert is_token_command("") is False

    def test_is_stack_command(self) -> None:
        assert is_stack_command("/stack") is True
        assert is_stack_command("/stack aws") is True
        assert is_stack_command("/context") is False
        assert is_stack_command("") is False

    def test_is_refresh_command(self) -> None:
        assert is_refresh_command("/refresh") is True
        assert is_refresh_command("  /refresh  ") is True
        assert is_refresh_command("/refresh extra") is False
        assert is_refresh_command("") is False

    def test_is_setup_command(self) -> None:
        assert is_setup_command("/setup") is True
        assert is_setup_command("  /setup  ") is True
        assert is_setup_command("/setup now") is False
        assert is_setup_command("") is False

    def test_extract_requested_context(self) -> None:
        assert extract_requested_context("/context prod-eu") == "prod-eu"
        assert extract_requested_context("/ctx staging-us") == "staging-us"
        assert extract_requested_context("/context") is None
        assert extract_requested_context("") is None
        assert extract_requested_context("/context    ") is None

    def test_extract_requested_context_trailing_spaces(self) -> None:
        assert extract_requested_context("/context  my-cluster  ") == "my-cluster"


class TestContextDisplay:
    """Cover format_context_switch_lines."""

    def test_null_current_context(self) -> None:
        result = KubernetesContextSwitchResult(
            contexts=[],
            current_context=None,
            connected=False,
            switched=False,
            kubeconfig_paths=[],
        )
        lines = format_context_switch_lines(result)
        assert len(lines) == 1  # noqa: PLR2004
        assert "failed" in lines[0][0]

    def test_connected_switch(self) -> None:
        ctx = ClusterContext(
            name="prod-eu", cluster="c1", namespace="default", user="admin", is_current=True
        )
        result = KubernetesContextSwitchResult(
            contexts=[],
            current_context=ctx,
            connected=True,
            switched=True,
            kubeconfig_paths=[],
        )
        lines = format_context_switch_lines(result)
        assert len(lines) == 5  # noqa: PLR2004
        assert "Connection successful" in [l[0] for l in lines]  # noqa: E741
        assert any("green" == l[1] for l in lines)  # noqa: E741

    def test_not_connected_with_error(self) -> None:
        ctx = ClusterContext(
            name="prod-eu", cluster="c1", namespace="default", user="admin", is_current=True
        )
        result = KubernetesContextSwitchResult(
            contexts=[],
            current_context=ctx,
            connected=False,
            switched=False,
            kubeconfig_paths=[],
            connection_error="timeout",
        )
        lines = format_context_switch_lines(result)
        assert "timeout" in [l[0] for l in lines]  # noqa: E741


class TestLicenseDisplay:
    """Cover license_display functions."""

    def test_format_license_footer_hint_expired(self) -> None:
        assert "upgrade" in format_license_footer_hint("expired")

    def test_format_license_footer_hint_warning(self) -> None:
        assert "upgrade" in format_license_footer_hint("warning")

    def test_format_license_footer_hint_other(self) -> None:
        assert "manage" in format_license_footer_hint("active")
        assert "manage" in format_license_footer_hint("missing")

    def test_format_license_aside_lines_missing(self) -> None:
        with patch(
            "hexawyn.cli.presentation.license_display.read_license_state",
            return_value=MagicMock(
                state="missing", plan="unknown", days_remaining=0, expiry_date=""
            ),
        ):
            lines = format_license_aside_lines()
            assert "not configured" in lines[1]

    def test_format_license_aside_lines_invalid(self) -> None:
        with patch(
            "hexawyn.cli.presentation.license_display.read_license_state",
            return_value=MagicMock(
                state="invalid", plan="unknown", days_remaining=0, expiry_date=""
            ),
        ):
            lines = format_license_aside_lines()
            assert "invalid" in lines[1]

    def test_format_license_aside_lines_expired(self) -> None:
        with patch(
            "hexawyn.cli.presentation.license_display.read_license_state",
            return_value=MagicMock(
                state="expired", plan="starter", days_remaining=0, expiry_date="2024-01-01"
            ),
        ):
            lines = format_license_aside_lines()
            assert any("expired" in line for line in lines)

    def test_format_license_aside_lines_active(self) -> None:
        with patch(
            "hexawyn.cli.presentation.license_display.read_license_state",
            return_value=MagicMock(
                state="active", plan="starter", days_remaining=30, expiry_date="2026-12-01"
            ),
        ):
            lines = format_license_aside_lines()
            assert "License: Starter" in lines[1]
            assert "30d" in lines[2]

    def test_format_license_aside_lines_active_no_days_remaining(self) -> None:
        with patch(
            "hexawyn.cli.presentation.license_display.read_license_state",
            return_value=MagicMock(
                state="active", plan="enterprise", days_remaining=0, expiry_date="permanent"
            ),
        ):
            lines = format_license_aside_lines()
            assert "Enterprise" in lines[1]


class TestSuggestions:
    """Cover format_suggestion_lines."""

    def test_basic_suggestions(self) -> None:
        app = MagicMock()
        app.ai_suggestion = None
        app.startup_result = None

        lines = format_suggestion_lines(app, [])
        assert "Suggestions" in lines[2]

    def test_with_ai_suggestion(self) -> None:
        app = MagicMock()
        app.ai_suggestion = "Try checking pod logs"
        app.startup_result = None

        lines = format_suggestion_lines(app, [])
        assert "Try checking pod logs" in " ".join(lines)

    def test_with_startup_result(self) -> None:
        app = MagicMock()
        app.ai_suggestion = None
        app.startup_result = {
            "suggestions": [
                {"label": "High CPU", "explanation": "80% usage", "severity": "critical"},
                {"label": "Low memory", "explanation": "10% free", "severity": "warning"},
                {"label": "Info check", "severity": "info"},
            ],
            "narrative_summary": "Cluster is healthy",
        }

        with patch(
            "hexawyn.cli.presentation.suggestions.is_error_narrative",
            return_value=False,
        ):
            lines = format_suggestion_lines(app, [])
            assert "High CPU" in " ".join(lines)
            assert "healthy" in " ".join(lines)

    def test_fallback_suggestions_when_few_lines(self) -> None:
        app = MagicMock()
        app.ai_suggestion = None
        app.startup_result = None

        lines = format_suggestion_lines(app, ["sug1", "sug2", "sug3"])
        assert "sug1" in " ".join(lines)
        assert "sug3" in " ".join(lines)

    def test_error_narrative_skipped(self) -> None:
        app = MagicMock()
        app.ai_suggestion = None
        app.startup_result = {
            "suggestions": [],
            "narrative_summary": "Cluster has critical issues",
        }

        with patch(
            "hexawyn.cli.presentation.suggestions.is_error_narrative",
            return_value=True,
        ):
            lines = format_suggestion_lines(app, [])
            assert "critical issues" not in " ".join(lines)
