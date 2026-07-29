from __future__ import annotations

from click.testing import CliRunner
from hexawyn.cli.commands.quota_command import (
    _get_tier_label,
    _render_bar,
    _render_line,
    quota,
)
from hexawyn.domain.models.quota import QuotaState


class TestRenderBar:
    def test_unlimited_shows_infinity(self) -> None:
        result = _render_bar(0, None, QuotaState.UNLIMITED)
        assert "\u221e" in result

    def test_locked_returns_empty(self) -> None:
        result = _render_bar(10, 100, QuotaState.LOCKED)
        assert result == ""

    def test_none_limit_returns_empty(self) -> None:
        result = _render_bar(10, None, QuotaState.NORMAL)
        assert result == ""

    def test_zero_limit_returns_empty(self) -> None:
        result = _render_bar(5, 0, QuotaState.NORMAL)
        assert result == ""

    def test_normal_bar_renders_fill(self) -> None:
        import click

        result = _render_bar(5, 20, QuotaState.NORMAL)
        unstyled = click.unstyle(result)
        assert len(unstyled) == 20  # noqa: PLR2004

    def test_warning_bar_renders_fill(self) -> None:
        import click

        result = _render_bar(17, 20, QuotaState.WARNING)
        unstyled = click.unstyle(result)
        assert len(unstyled) == 20  # noqa: PLR2004

    def test_critical_bar_renders_fill(self) -> None:
        import click

        result = _render_bar(19, 20, QuotaState.CRITICAL)
        unstyled = click.unstyle(result)
        assert len(unstyled) == 20  # noqa: PLR2004

    def test_exhausted_bar_renders_fill(self) -> None:
        import click

        result = _render_bar(20, 20, QuotaState.EXHAUSTED)
        unstyled = click.unstyle(result)
        assert len(unstyled) == 20  # noqa: PLR2004


class TestRenderLine:
    def test_unlimited_line(self) -> None:
        result = _render_line("Investigations", 0, None, QuotaState.UNLIMITED)
        assert "Investigations" in result
        assert "\u221e" in result

    def test_locked_line(self) -> None:
        result = _render_line("Alerts", 0, 50, QuotaState.LOCKED)
        assert "Alerts" in result
        assert "Unavailable" in result

    def test_normal_line_shows_fraction(self) -> None:
        result = _render_line("Investigations", 50, 200, QuotaState.NORMAL)
        assert "50/200" in result
        assert "150 remaining" in result

    def test_exhausted_line_shows_cross(self) -> None:
        result = _render_line("Investigations", 200, 200, QuotaState.EXHAUSTED)
        assert "200/200" in result


class TestGetTierLabel:
    def test_with_import_error_returns_starter(self) -> None:
        try:
            from unittest.mock import patch
        except ImportError:
            pass

        with patch(
            "hexawyn.infrastructure.config.license_manager.get_license_tier",
            side_effect=ImportError("No license module"),
        ):
            label = _get_tier_label()
        assert "Starter" in label

    def test_returns_label_with_price(self) -> None:
        label = _get_tier_label()
        assert len(label) > 0
        assert "$" in label


class TestQuotaCommandHelp:
    def test_quota_help_output(self) -> None:
        runner = CliRunner()
        result = runner.invoke(quota, ["--help"])
        assert result.exit_code == 0  # noqa: PLR2004
        assert "quota" in result.output.lower()
