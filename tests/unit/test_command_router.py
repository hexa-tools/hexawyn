from unittest.mock import MagicMock, patch

from hexawyn.application.use_case.chat_cli.chat_cli_response import ChatCliResponse
from hexawyn.cli.command_router import route_command


class TestRouteCommand:
    def test_empty_input_returns_unknown(self) -> None:
        result = route_command("", MagicMock())
        assert result.kind == "unknown"

    def test_whitespace_only_returns_unknown(self) -> None:
        result = route_command("   ", MagicMock())
        assert result.kind == "unknown"

    def test_returns_chat_cli_response(self) -> None:
        mock_adapter = MagicMock()
        mock_adapter.get_cluster_context.return_value = {
            "name": "prod-eu",
            "cluster": "k8s",
            "provider": "aws",
            "namespace": "default",
        }
        mock_runtime = MagicMock()
        mock_runtime.run_investigation.return_value = {
            "answer": "OOM detected",
            "cause": "",
            "solution": "",
            "status": "complete",
            "suggestions": [],
            "error": None,
        }
        with patch("hexawyn.cli.command_router.get_runtime", return_value=mock_runtime):
            result = route_command("why is payments crashing?", mock_adapter)
        assert isinstance(result, ChatCliResponse)
        assert result.kind == "debug"

    def test_delegates_to_chat_cli_service(self) -> None:
        mock_adapter = MagicMock()
        mock_adapter.get_cluster_context.return_value = {
            "name": "prod",
            "cluster": "k8s",
            "provider": "aws",
            "namespace": "default",
        }
        mock_runtime = MagicMock()
        mock_runtime.run_investigation.return_value = {
            "answer": "ok",
            "cause": "",
            "solution": "",
            "status": "complete",
            "suggestions": ["scale up"],
            "error": None,
        }
        with patch("hexawyn.cli.command_router.get_runtime", return_value=mock_runtime):
            result = route_command("investigate pods", mock_adapter)
        assert "scale up" in result.suggestions
