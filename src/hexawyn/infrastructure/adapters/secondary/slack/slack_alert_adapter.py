import os

import httpx

from hexawyn.application.ports.driven.alert_notification_port import (
    AlertMessage,
    AlertNotificationPort,
)
from hexawyn.domain.models.slack import SlackBlock, SlackMessage
from hexawyn.infrastructure.config.quota_manager import (
    check_slack_quota,
    increment_slack_quota,
)

_SEVERITY_EMOJI: dict[str, str] = {
    "critical": "🚨",
    "high": "⚠️",
    "warning": "⚠️",
    "info": "ℹ️",
}


class SlackAlertAdapter(AlertNotificationPort):
    """
    Sends alerts to Slack via incoming webhook.
    Free tier: 5 alerts/month (quota enforced via check_slack_quota).
    Pro tier: unlimited + enriched blocks format.

    Never raises on network errors — returns False instead.
    Raises SlackQuotaExceededError when monthly limit is reached.
    """

    def __init__(self, webhook_url: str | None = None) -> None:
        self._webhook_url = webhook_url or os.environ.get("HEXAWYN_SLACK_WEBHOOK_URL", "")

    def send_alert(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def send_test_ping(self) -> bool:
        """Send a connectivity test without consuming quota."""
        return self._post(
            SlackMessage(text="✅ hexawyn Slack integration is working!"), track_quota=False
        )

    def format_finding_alert(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def _to_slack_message(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def _post(self, message: SlackMessage, track_quota: bool) -> bool:
        if not self._webhook_url:
            return False
        try:
            response = httpx.post(
                self._webhook_url,
                json=message.to_payload(),
                timeout=10.0,
            )
            if response.status_code == 200:  # noqa: PLR2004
                if track_quota:
                    increment_slack_quota()
                return True
            return False
        except Exception:
            return False
