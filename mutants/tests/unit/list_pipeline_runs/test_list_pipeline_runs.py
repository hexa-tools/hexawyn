from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestListPipelineRunsTool:
    def test_returns_dict_on_error(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_tekton_adapter",
            side_effect=Exception("no cluster"),
        ):  # noqa: E501
            from hexawyn.mcp.tools.list_pipeline_runs import list_pipeline_runs

            result = list_pipeline_runs(service_name="test")
            assert isinstance(result, dict)
            assert result.get("runs") == []

    def test_returns_dict_on_success(self) -> None:
        with patch("hexawyn.mcp.server.build_tekton_adapter") as mock_build:  # noqa: E501
            mock_adapter = MagicMock()
            mock_adapter.list_pipeline_runs.return_value = []
            mock_build.return_value = mock_adapter

            from hexawyn.mcp.tools.list_pipeline_runs import list_pipeline_runs

            result = list_pipeline_runs(service_name="test")
            assert isinstance(result, dict)
