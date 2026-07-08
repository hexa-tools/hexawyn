from unittest.mock import patch

import pytest
from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter
from hexawyn.adapters.secondary.slack.slack_alert_adapter import SlackAlertAdapter


class TestSlackAlertIntegration:
    @pytest.mark.integration
    def test_full_alert_flow_demo_aws_eks(self) -> None:
        demo = DemoAdapter(scenario="aws_eks")
        adapter = SlackAlertAdapter(webhook_url="https://hooks.slack.com/test")

        findings = demo.get_findings()
        critical = [f for f in findings if f["severity"] == "critical"]
        assert len(critical) >= 1

        msg = adapter.format_finding_alert(
            finding=critical[0],
            cluster_name="prod-eu",
            score=demo.get_health_score(),
            is_pro=False,
        )
        assert "76" in msg["text"]
        assert msg["is_pro"] is False

        with patch("httpx.post") as mock_post:
            mock_post.return_value.status_code = 200
            with patch("hexawyn.adapters.secondary.slack.slack_alert_adapter.check_slack_quota"):
                with patch(
                    "hexawyn.adapters.secondary.slack.slack_alert_adapter.increment_slack_quota"
                ):
                    result = adapter.send_alert(msg)
        assert result is True

    @pytest.mark.integration
    @pytest.mark.parametrize(
        "scenario", ["aws_eks", "azure_aks", "gcp_gke", "openshift", "datadog"]
    )
    def test_all_scenarios_produce_sendable_alerts(self, scenario: str) -> None:
        demo = DemoAdapter(scenario=scenario)
        adapter = SlackAlertAdapter(webhook_url="https://hooks.slack.com/test")

        findings = demo.get_findings()
        assert len(findings) >= 1

        msg = adapter.format_finding_alert(
            finding=findings[0],
            cluster_name="test-cluster",
            score=demo.get_health_score(),
            is_pro=False,
        )
        assert len(msg["text"]) > 0
        assert msg["cluster_name"] == "test-cluster"
