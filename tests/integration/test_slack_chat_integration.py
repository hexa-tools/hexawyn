from unittest.mock import MagicMock

import pytest
from hexawyn.adapters.primary.slack.slack_chat_adapter import SlackChatAdapter
from hexawyn.adapters.primary.slack.slack_webhook import handle_slack_event
from hexawyn.domain.errors import QuotaExceededError


class TestSlackChatIntegration:
    @pytest.mark.integration
    def test_url_verification_flow(self) -> None:
        event = {
            "type": "url_verification",
            "challenge": "real_challenge_abc123",
        }
        result = handle_slack_event(event)
        assert result["challenge"] == "real_challenge_abc123"

    @pytest.mark.integration
    def test_quota_exceeded_returns_upgrade_message(self) -> None:
        use_case = MagicMock()
        use_case.execute.side_effect = QuotaExceededError(used=50, limit=50)
        adapter = SlackChatAdapter(use_case=use_case)
        result = adapter.handle_message(
            query="why is payments-api crashing?",
            cluster_name="prod-eu",
            channel_id="C123456",
        )
        assert "hexawyn.com/pro" in result
        assert "50/50" in result
        assert isinstance(result, str)

    @pytest.mark.integration
    def test_format_response_free_vs_pro(self) -> None:
        adapter = SlackChatAdapter()

        free_response = adapter.format_response(
            answer="OOM detected",
            quota_display="[23/50 · 27 remaining]",
            suggestions=["has this happened before?"],
            is_pro=False,
        )
        pro_response = adapter.format_response(
            answer="OOM detected",
            quota_display="[⭐ Pro — unlimited]",
            suggestions=["has this happened before?", "what is the SLO impact?"],
            is_pro=True,
        )

        assert "OOM detected" in free_response
        assert "OOM detected" in pro_response
        assert "has this happened before?" in pro_response
        assert "23/50" in free_response
        assert "unlimited" in pro_response.lower()
