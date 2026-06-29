from unittest.mock import patch

import pytest
from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter
from hexawyn.adapters.secondary.slack.slack_alert_adapter import SlackAlertAdapter


class TestSlackDemoMode:
    @pytest.mark.parametrize(
        "scenario,expected_score",
        [
            ("aws_eks", 76),
            ("azure_aks", 98),
            ("gcp_gke", 84),
            ("openshift", 71),
            ("datadog", 79),
        ],
    )
    def test_demo_scenario_slack_message_sendable(self, scenario: str, expected_score: int) -> None:
        demo = DemoAdapter(scenario=scenario)
        slack_msg = demo.get_slack_message()
        assert len(slack_msg) > 0
        assert str(expected_score) in slack_msg

    def test_send_demo_slack_alert(self) -> None:
        demo = DemoAdapter(scenario="aws_eks")
        adapter = SlackAlertAdapter(webhook_url="https://hooks.slack.com/test")

        with patch("httpx.post") as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.text = "ok"
            with patch("hexawyn.adapters.secondary.slack.slack_alert_adapter.check_slack_quota"):
                with patch(
                    "hexawyn.adapters.secondary.slack.slack_alert_adapter.increment_slack_quota"
                ):
                    findings = demo.get_findings()
                    critical = [f for f in findings if f["severity"] == "critical"]
                    msg = adapter.format_finding_alert(
                        finding=critical[0],
                        cluster_name="prod-eu",
                        score=demo.get_health_score(),
                        is_pro=False,
                    )
                    result = adapter.send_alert(msg)
        assert result is True
