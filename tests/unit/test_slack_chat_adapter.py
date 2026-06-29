from unittest.mock import MagicMock

from hexawyn.adapters.primary.slack.slack_chat_adapter import SlackChatAdapter
from hexawyn.application.use_case.chat_slack.chat_slack_response import ChatSlackResponse
from hexawyn.domain.errors import QuotaExceededError


def _make_response(
    message: str = "OOM detected",
    quota_display: str = "[23/50 · 27 remaining]",
    suggestions: list[str] | None = None,
    is_pro: bool = False,
) -> ChatSlackResponse:
    return ChatSlackResponse(
        message=message,
        quota_display=quota_display,
        suggestions=suggestions or [],
        is_pro=is_pro,
    )


class TestSlackChatAdapter:
    def setup_method(self) -> None:
        self.use_case = MagicMock()
        self.adapter = SlackChatAdapter(use_case=self.use_case)

    def test_handle_message_returns_string(self) -> None:
        self.use_case.execute.return_value = _make_response()
        result = self.adapter.handle_message(
            query="why is payments-api crashing?",
            cluster_name="prod-eu",
            channel_id="C123456",
        )
        assert isinstance(result, str)
        assert len(result) > 0

    def test_handle_message_includes_quota_display(self) -> None:
        self.use_case.execute.return_value = _make_response(quota_display="[23/50 · 27 remaining]")
        result = self.adapter.handle_message(
            query="test",
            cluster_name="prod-eu",
            channel_id="C123456",
        )
        assert "23/50" in result or "27 remaining" in result

    def test_handle_message_quota_exceeded_returns_upgrade_message(self) -> None:
        self.use_case.execute.side_effect = QuotaExceededError(used=50, limit=50)
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

    def test_format_response_pro_tier_includes_suggestions(self) -> None:
        result = self.adapter.format_response(
            answer="OOM detected",
            quota_display="[⭐ Pro — unlimited]",
            suggestions=["has this happened before?", "what is the SLO impact?"],
            is_pro=True,
        )
        assert "OOM detected" in result
        assert "has this happened before?" in result

    def test_never_raises_on_unexpected_error(self) -> None:
        self.use_case.execute.side_effect = Exception("unexpected error")
        result = self.adapter.handle_message(
            query="test",
            cluster_name="prod-eu",
            channel_id="C123456",
        )
        assert isinstance(result, str)
        assert "error" in result.lower()

    def test_handle_message_with_thread_ts(self) -> None:
        self.use_case.execute.return_value = _make_response(message="All pods running")
        result = self.adapter.handle_message(
            query="list pods",
            cluster_name="prod-eu",
            channel_id="C123456",
            thread_ts="1234567890.123456",
        )
        assert isinstance(result, str)

    def test_format_response_includes_suggestions_when_given(self) -> None:
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

    def test_use_case_receives_correct_command(self) -> None:
        self.use_case.execute.return_value = _make_response()
        self.adapter.handle_message(
            query="why is api crashing?",
            cluster_name="prod-eu",
            channel_id="C999",
            thread_ts="1234.5678",
        )
        cmd = self.use_case.execute.call_args[0][0]
        assert cmd.query == "why is api crashing?"
        assert cmd.cluster_name == "prod-eu"
        assert cmd.channel_id == "C999"
        assert cmd.thread_ts == "1234.5678"

    def test_default_use_case_is_chat_slack_service(self) -> None:
        from hexawyn.application.service.chat_slack_service import ChatSlackService

        adapter = SlackChatAdapter()
        assert isinstance(adapter._use_case, ChatSlackService)
