from unittest.mock import patch

from hexawyn.adapters.primary.slack.slack_chat_adapter import SlackChatAdapter
from hexawyn.domain.errors import QuotaExceededError


class TestSlackChatAdapter:
    def setup_method(self) -> None:
        self.adapter = SlackChatAdapter()

    def test_handle_message_returns_string(self) -> None:
        with patch(
            "hexawyn.adapters.primary.slack.slack_chat_adapter.run_investigation",
            return_value="OOM detected — increase memory limit",
        ):
            with patch(
                "hexawyn.adapters.primary.slack.slack_chat_adapter.get_quota_display",
                return_value="[23/50 · 27 remaining]",
            ):
                with patch(
                    "hexawyn.adapters.primary.slack.slack_chat_adapter.is_pro",
                    return_value=False,
                ):
                    result = self.adapter.handle_message(
                        query="why is payments-api crashing?",
                        cluster_name="prod-eu",
                        channel_id="C123456",
                    )
        assert isinstance(result, str)
        assert len(result) > 0

    def test_handle_message_includes_quota_display(self) -> None:
        with patch(
            "hexawyn.adapters.primary.slack.slack_chat_adapter.run_investigation",
            return_value="OOM detected",
        ):
            with patch(
                "hexawyn.adapters.primary.slack.slack_chat_adapter.get_quota_display",
                return_value="[23/50 · 27 remaining]",
            ):
                with patch(
                    "hexawyn.adapters.primary.slack.slack_chat_adapter.is_pro",
                    return_value=False,
                ):
                    result = self.adapter.handle_message(
                        query="test",
                        cluster_name="prod-eu",
                        channel_id="C123456",
                    )
        assert "23/50" in result or "27 remaining" in result

    def test_handle_message_quota_exceeded_returns_upgrade_message(self) -> None:
        with patch(
            "hexawyn.adapters.primary.slack.slack_chat_adapter.run_investigation",
            side_effect=QuotaExceededError(used=50, limit=50),
        ):
            result = self.adapter.handle_message(
                query="test",
                cluster_name="prod-eu",
                channel_id="C123456",
            )
        assert "hexawyn.com/pro" in result
        assert "50/50" in result

    def test_format_response_free_tier_basic_text(self) -> None:
        result = self.adapter.format_response(
            answer="OOM detected",
            quota_display="[23/50 · 27 remaining]",
            suggestions=["has this happened before?"],
            is_pro=False,
        )
        assert "OOM detected" in result
        assert "23/50" in result

    def test_format_response_pro_tier_enriched(self) -> None:
        result = self.adapter.format_response(
            answer="OOM detected",
            quota_display="[⭐ Pro — unlimited]",
            suggestions=[
                "has this happened before?",
                "what is the SLO impact?",
            ],
            is_pro=True,
        )
        assert "OOM detected" in result
        assert "has this happened before?" in result

    def test_never_raises_on_langgraph_error(self) -> None:
        with patch(
            "hexawyn.adapters.primary.slack.slack_chat_adapter.run_investigation",
            side_effect=Exception("unexpected error"),
        ):
            result = self.adapter.handle_message(
                query="test",
                cluster_name="prod-eu",
                channel_id="C123456",
            )
        assert isinstance(result, str)
        assert "error" in result.lower()

    def test_handle_message_with_thread_ts(self) -> None:
        with patch(
            "hexawyn.adapters.primary.slack.slack_chat_adapter.run_investigation",
            return_value="All pods running",
        ):
            with patch(
                "hexawyn.adapters.primary.slack.slack_chat_adapter.get_quota_display",
                return_value="[1/50 · 49 remaining]",
            ):
                with patch(
                    "hexawyn.adapters.primary.slack.slack_chat_adapter.is_pro",
                    return_value=False,
                ):
                    result = self.adapter.handle_message(
                        query="list pods",
                        cluster_name="prod-eu",
                        channel_id="C123456",
                        thread_ts="1234567890.123456",
                    )
        assert isinstance(result, str)

    def test_format_response_includes_suggestions_when_pro(self) -> None:
        result = self.adapter.format_response(
            answer="Memory limit exceeded",
            quota_display="[⭐ Pro — unlimited]",
            suggestions=["scale up memory", "check HPA config"],
            is_pro=True,
        )
        assert "scale up memory" in result
        assert "check HPA config" in result

    def test_format_response_limits_suggestions_to_four(self) -> None:
        result = self.adapter.format_response(
            answer="ok",
            quota_display="[1/50]",
            suggestions=["s1", "s2", "s3", "s4", "s5"],
            is_pro=True,
        )
        assert "s5" not in result
        assert "s4" in result
