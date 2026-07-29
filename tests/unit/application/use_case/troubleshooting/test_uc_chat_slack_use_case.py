from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.use_case.troubleshooting.chat_slack.chat_slack_command import (
    ChatSlackCommand,
)
from hexawyn.application.use_case.troubleshooting.chat_slack.chat_slack_response import (
    ChatSlackResponse,
)
from hexawyn.application.use_case.troubleshooting.chat_slack.chat_slack_use_case import (  # noqa: E501
    ChatSlackUseCase,
)
from hexawyn.domain.errors import QuotaExceededError


class TestChatSlackUseCase:
    def test_execute_returns_response(self) -> None:
        runtime = MagicMock()
        runtime.check_quota.return_value = {
            "allowed": True,
            "used": 5,
            "limit": 50,
        }
        runtime.run_investigation.return_value = {
            "answer": "OK",
            "suggestions": [],
        }

        use_case = ChatSlackUseCase(runtime=runtime)
        result = use_case.execute(
            ChatSlackCommand(
                query="why is payments-api crashing?",
                cluster_name="prod-eu",
                channel_id="C123",
            )
        )

        assert isinstance(result, ChatSlackResponse)

    def test_execute_quota_exceeded_raises(self) -> None:
        runtime = MagicMock()
        runtime.check_quota.return_value = {
            "allowed": False,
            "used": 50,
            "limit": 50,
        }

        use_case = ChatSlackUseCase(runtime=runtime)

        with pytest.raises(QuotaExceededError):
            use_case.execute(
                ChatSlackCommand(
                    query="test",
                    cluster_name="prod",
                    channel_id="C456",
                )
            )

    def test_execute_default_runtime_initialization(self) -> None:
        mock_runtime = MagicMock()
        mock_runtime.check_quota.return_value = {
            "allowed": True,
            "used": 5,
            "limit": 50,
        }
        mock_runtime.run_investigation.return_value = {
            "answer": "OK",
            "suggestions": [],
        }

        with patch(
            "hexawyn.application.service.runtime_adapter.get_runtime",
            return_value=mock_runtime,
        ):
            use_case = ChatSlackUseCase()
            result = use_case.execute(
                ChatSlackCommand(
                    query="test",
                    cluster_name="prod",
                    channel_id="C123",
                )
            )

        assert isinstance(result, ChatSlackResponse)
