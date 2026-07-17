"""Tests for MCP consolidation tool."""

from unittest.mock import MagicMock, patch

from hexawyn.mcp.tools.run_consolidation import register, run_consolidation


class TestRunConsolidationTool:
    def test_returns_consolidated_result(self) -> None:
        mock_use_case = MagicMock()
        mock_response = MagicMock()
        mock_response.groups_found = 2
        mock_response.consolidated = [
            MagicMock(pattern="test pattern 1"),
            MagicMock(pattern="test pattern 2"),
        ]
        mock_use_case.execute.return_value = mock_response

        with patch(
            "hexawyn.mcp.server.build_consolidation_adapter",
            return_value=MagicMock(),
        ):
            with patch(
                "hexawyn.application.use_case.run_consolidation.run_consolidation_use_case.RunConsolidationUseCase",
                return_value=mock_use_case,
            ):
                result = run_consolidation(cluster_name="test")
                assert result["consolidated"] == 2
                assert len(result["patterns"]) == 2
                assert result["error"] is None

    def test_handles_exception(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_consolidation_adapter",
            side_effect=RuntimeError("db error"),
        ):
            result = run_consolidation(cluster_name="test")
            assert result["consolidated"] == 0
            assert result["patterns"] == []
            assert result["error"] is not None

    def test_register_calls_mcp_tool(self) -> None:
        mock_mcp = MagicMock()
        register(mock_mcp)
        mock_mcp.tool.assert_called()
