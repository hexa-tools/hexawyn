"""Unit tests for the CLI quota renderer helpers."""

from __future__ import annotations

from hexawyn.cli.presentation.quota_renderer import format_quota_exceeded


class TestFormatQuotaExceeded:
    def test_default_investigations(self) -> None:
        out = format_quota_exceeded(23, 50)
        assert "Quota exceeded" in out
        assert "23/50" in out
        assert "Upgrade your plan" in out
        assert "hexa license activate" in out

    def test_resource_label_mapped(self) -> None:
        out = format_quota_exceeded(4, 5, resource="slack_alerts")
        assert "Slack alerts" in out
        assert "4/5" in out

    def test_unknown_resource_uses_name(self) -> None:
        out = format_quota_exceeded(1, 10, resource="custom_meter")
        assert "custom_meter" in out

    def test_upgrade_url_present(self) -> None:
        out = format_quota_exceeded(23, 50)
        assert "https://hexawyn.com/pricing" in out
