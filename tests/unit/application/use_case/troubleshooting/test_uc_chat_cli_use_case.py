from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.troubleshooting.chat_cli.chat_cli_command import (
    ChatCliCommand,
)
from hexawyn.application.use_case.troubleshooting.chat_cli.chat_cli_response import (
    ChatCliResponse,
)
from hexawyn.application.use_case.troubleshooting.chat_cli.chat_cli_use_case import (  # noqa: E501
    ChatCliUseCase,
)


class TestChatCliUseCase:
    def test_execute_returns_response(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = []
        runtime = MagicMock()
        runtime.run_investigation.return_value = {
            "status": "ok",
            "answer": "test response",
            "suggestions": [],
            "usage": {},
            "embedding": [],
            "cause": "",
            "solution": "",
            "error": None,
        }
        runtime.check_quota.return_value = {
            "allowed": True,
            "used": 1,
            "limit": 50,
        }

        use_case = ChatCliUseCase(
            k8s_port=k8s,
            runtime=runtime,
        )
        result = use_case.execute(ChatCliCommand(query="test query"))

        assert isinstance(result, ChatCliResponse)

    def test_list_pods_returns_response(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = []
        runtime = MagicMock()

        use_case = ChatCliUseCase(
            k8s_port=k8s,
            runtime=runtime,
        )
        result = use_case.list_pods()

        assert isinstance(result, ChatCliResponse)
        assert result.kind == "pods"

    def test_execute_with_empty_query(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = []
        runtime = MagicMock()
        runtime.run_investigation.return_value = {
            "status": "error",
            "answer": "No query provided",
            "suggestions": [],
            "usage": {},
            "embedding": [],
            "cause": "",
            "solution": "",
            "error": "empty query",
        }
        runtime.check_quota.return_value = {
            "allowed": True,
            "used": 1,
            "limit": 50,
        }

        use_case = ChatCliUseCase(
            k8s_port=k8s,
            runtime=runtime,
        )
        result = use_case.execute(ChatCliCommand(query=""))

        assert isinstance(result, ChatCliResponse)
