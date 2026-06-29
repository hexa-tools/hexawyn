from unittest.mock import patch

import pytest
from hexawyn.adapters.secondary.slack.slack_alert_adapter import SlackAlertAdapter
from hexawyn.application.ports.driven.alert_notification_port import AlertMessage
from hexawyn.domain.errors import SlackQuotaExceededError


def _make_alert(text: str = "test alert", is_pro: bool = False) -> AlertMessage:
    return AlertMessage(
        text=text,
        title="hexawyn Alert",
        severity="info",
        remediation=None,
        cluster_name="test-cluster",
        score=100,
        is_pro=is_pro,
    )


class TestSlackAlertAdapter:
    def setup_method(self) -> None:
        self.adapter = SlackAlertAdapter(webhook_url="https://hooks.slack.com/test")

    def test_send_alert_returns_true_on_success(self) -> None:
        with patch("httpx.post") as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.text = "ok"
            with patch("hexawyn.adapters.secondary.slack.slack_alert_adapter.check_slack_quota"):
                with patch(
                    "hexawyn.adapters.secondary.slack.slack_alert_adapter.increment_slack_quota"
                ):
                    result = self.adapter.send_alert(_make_alert())
        assert result is True

    def test_send_alert_returns_false_on_http_error(self) -> None:
        with patch("httpx.post") as mock_post:
            mock_post.return_value.status_code = 500
            mock_post.return_value.text = "error"
            with patch("hexawyn.adapters.secondary.slack.slack_alert_adapter.check_slack_quota"):
                result = self.adapter.send_alert(_make_alert())
        assert result is False

    def test_send_alert_raises_quota_exceeded(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.slack.slack_alert_adapter.check_slack_quota",
            side_effect=SlackQuotaExceededError(used=5, limit=5),
        ):
            with pytest.raises(SlackQuotaExceededError):
                self.adapter.send_alert(_make_alert())

    def test_send_alert_returns_false_when_no_webhook(self) -> None:
        with patch.dict("os.environ", {"HEXAWYN_SLACK_WEBHOOK_URL": ""}, clear=False):
            adapter = SlackAlertAdapter(webhook_url=None)
            with patch(
                "hexawyn.adapters.secondary.slack.slack_alert_adapter.os.environ.get",
                return_value="",
            ):
                with patch(
                    "hexawyn.adapters.secondary.slack.slack_alert_adapter.check_slack_quota"
                ):
                    result = adapter.send_alert(_make_alert())
        assert result is False

    def test_format_finding_free_tier(self) -> None:
        msg = self.adapter.format_finding_alert(
            finding={
                "severity": "critical",
                "message": "payments-api CrashLoopBackOff",
                "remediation": "increase memory limit",
            },
            cluster_name="prod-eu",
            score=76,
            is_pro=False,
        )
        assert "76" in msg["text"]
        assert "🚨" in msg["text"] or "critical" in msg["text"].lower()
        assert msg["is_pro"] is False

    def test_format_finding_pro_tier(self) -> None:
        msg = self.adapter.format_finding_alert(
            finding={
                "severity": "critical",
                "message": "payments-api CrashLoopBackOff",
                "remediation": "increase memory limit",
            },
            cluster_name="prod-eu",
            score=76,
            is_pro=True,
        )
        assert msg["is_pro"] is True

    def test_never_raises_on_network_error(self) -> None:
        with patch("httpx.post", side_effect=Exception("network error")):
            with patch("hexawyn.adapters.secondary.slack.slack_alert_adapter.check_slack_quota"):
                result = self.adapter.send_alert(_make_alert())
        assert result is False

    def test_format_finding_includes_cluster_name(self) -> None:
        msg = self.adapter.format_finding_alert(
            finding={"severity": "warning", "message": "pod pending", "remediation": "check nodes"},
            cluster_name="staging-eu",
            score=90,
            is_pro=False,
        )
        assert "staging-eu" in msg["text"]

    def test_format_finding_pro_includes_remediation(self) -> None:
        msg = self.adapter.format_finding_alert(
            finding={
                "severity": "critical",
                "message": "OOM kill",
                "remediation": "increase memory to 512Mi",
            },
            cluster_name="prod-eu",
            score=76,
            is_pro=True,
        )
        assert msg["remediation"] is not None
        assert "512Mi" in msg["remediation"]

    def test_uses_env_webhook_url_when_none_passed(self) -> None:
        with patch("hexawyn.adapters.secondary.slack.slack_alert_adapter.os") as mock_os:
            mock_os.environ.get.return_value = "https://hooks.slack.com/env"
            adapter = SlackAlertAdapter()
            assert adapter._webhook_url == "https://hooks.slack.com/env"

    def test_send_alert_pro_uses_rich_blocks(self) -> None:
        captured: list[dict[str, object]] = []

        def fake_post(url: str, json: dict[str, object], timeout: float) -> object:
            captured.append(json)

            class Resp:
                status_code = 200

            return Resp()

        with patch("httpx.post", side_effect=fake_post):
            with patch("hexawyn.adapters.secondary.slack.slack_alert_adapter.check_slack_quota"):
                with patch(
                    "hexawyn.adapters.secondary.slack.slack_alert_adapter.increment_slack_quota"
                ):
                    self.adapter.send_alert(_make_alert(is_pro=True))

        assert len(captured) == 1
        assert "blocks" in captured[0]
