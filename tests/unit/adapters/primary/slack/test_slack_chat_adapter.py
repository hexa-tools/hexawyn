from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.adapters.primary.slack.slack_chat_adapter import SlackChatAdapter
from hexawyn.application.use_case.troubleshooting.chat_slack.chat_slack_response import (
    ChatSlackResponse,
)
from hexawyn.domain.errors import QuotaExceededError


class TestSlackChatAdapter:
    def test_handle_message_returns_formatted_answer(self) -> None:
        mock_use_case = MagicMock()
        mock_use_case.execute.return_value = ChatSlackResponse(
            message="OOM detected — increase memory limit",
            quota_display="5 / 50",
            suggestions=["Increase memory", "Check pod logs"],
            is_pro=False,
        )
        adapter = SlackChatAdapter(use_case=mock_use_case)

        result = adapter.handle_message(
            query="why is payments down?",
            cluster_name="prod",
            channel_id="C123",
        )

        assert "OOM detected" in result
        assert "5 / 50" in result
        assert "Increase memory" in result
        assert "Check pod logs" in result

    def test_handle_message_quota_exceeded_returns_error_message(self) -> None:
        mock_use_case = MagicMock()
        mock_use_case.execute.side_effect = QuotaExceededError(used=50, limit=50)
        adapter = SlackChatAdapter(use_case=mock_use_case)

        result = adapter.handle_message(
            query="query text",
            cluster_name="prod",
            channel_id="C123",
        )

        assert "QUOTA EXCEEDED" in result.upper()
        assert "50/50" in result
        assert "hexawyn.com/pro" in result

    def test_handle_message_generic_exception_returns_error_message(self) -> None:
        mock_use_case = MagicMock()
        mock_use_case.execute.side_effect = RuntimeError("connection refused")
        adapter = SlackChatAdapter(use_case=mock_use_case)

        result = adapter.handle_message(
            query="query text",
            cluster_name="prod",
            channel_id="C123",
        )

        assert "ERROR" in result.upper()
        assert "connection refused" in result
        assert "Please try again" in result

    def test_handle_message_passes_all_fields_to_use_case(self) -> None:
        mock_use_case = MagicMock()
        mock_use_case.execute.return_value = ChatSlackResponse(
            message="ok",
            quota_display="1 / 50",
            suggestions=[],
        )
        adapter = SlackChatAdapter(use_case=mock_use_case)

        adapter.handle_message(
            query="test query",
            cluster_name="staging",
            channel_id="C456",
            thread_ts="123.456",
        )

        called_command = mock_use_case.execute.call_args[0][0]
        assert called_command.query == "test query"
        assert called_command.cluster_name == "staging"
        assert called_command.channel_id == "C456"
        assert called_command.thread_ts == "123.456"

    def test_format_response_basic_no_suggestions(self) -> None:
        adapter = SlackChatAdapter(use_case=MagicMock())

        result = adapter.format_response(
            answer="All pods healthy.",
            quota_display="3 / 50",
            suggestions=[],
            is_pro=False,
        )

        assert "All pods healthy." in result
        assert "3 / 50" in result
        assert "Suggested questions" not in result

    def test_format_response_with_suggestions(self) -> None:
        adapter = SlackChatAdapter(use_case=MagicMock())

        result = adapter.format_response(
            answer="Cluster has 3 unhealthy pods.",
            quota_display="4 / 50",
            suggestions=["Fix memory limit", "Check restart policy"],
            is_pro=False,
        )

        assert "Fix memory limit" in result
        assert "Check restart policy" in result
        assert "Suggested questions" in result

    def test_format_response_truncates_suggestions_to_4(self) -> None:
        adapter = SlackChatAdapter(use_case=MagicMock())

        result = adapter.format_response(
            answer="ok",
            quota_display="1 / 50",
            suggestions=["a", "b", "c", "d", "e", "f"],
            is_pro=False,
        )

        assert "• a" in result
        assert "• d" in result
        assert "• e" not in result

    def test_format_response_with_paid_user_flag(self) -> None:
        adapter = SlackChatAdapter(use_case=MagicMock())

        result = adapter.format_response(
            answer="Detailed analysis...",
            quota_display="200 / 500",
            suggestions=["action1"],
            is_pro=True,
        )

        assert "Detailed analysis" in result
        assert "200 / 500" in result

    def test_format_response_structure(self) -> None:
        adapter = SlackChatAdapter(use_case=MagicMock())

        result = adapter.format_response(
            answer="The answer",
            quota_display="[5/50]",
            suggestions=["sug1", "sug2"],
            is_pro=False,
        )

        assert result.startswith("🔍")
        assert "investigation result" in result
        assert "The answer" in result
        assert "[5/50]" in result
        assert "Suggested questions" in result
