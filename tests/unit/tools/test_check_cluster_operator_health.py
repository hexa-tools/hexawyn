from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCheckClusterOperatorHealthMCPTool:
    def test_returns_dict_with_error_none_on_success(self) -> None:
        from hexawyn.mcp.tools.check_cluster_operator_health import (
            check_cluster_operator_health,
        )

        mock_port = MagicMock()
        mock_port.list_cluster_operators.return_value = []

        with patch(
            "hexawyn.mcp.server.build_cluster_operator_status_adapter",
            return_value=mock_port,
        ):
            result = check_cluster_operator_health()

        assert isinstance(result, dict)
        assert result["error"] is None
        assert result["total"] == 0
        assert result["operators"] == []

    def test_returns_operators_from_port(self) -> None:
        from hexawyn.mcp.tools.check_cluster_operator_health import (
            check_cluster_operator_health,
        )

        mock_port = MagicMock()
        mock_port.list_cluster_operators.return_value = [
            {
                "name": "etcd",
                "available": True,
                "progressing": False,
                "degraded": False,
                "available_unknown": False,
                "message": "",
                "degraded_since": None,
            },
        ]

        with patch(
            "hexawyn.mcp.server.build_cluster_operator_status_adapter",
            return_value=mock_port,
        ):
            result = check_cluster_operator_health()

        assert result["error"] is None
        assert result["total"] == 1
        assert result["all_healthy"] is True
        assert result["operators"][0]["name"] == "etcd"  # type: ignore[index]

    def test_returns_error_on_exception(self) -> None:
        from hexawyn.mcp.tools.check_cluster_operator_health import (
            check_cluster_operator_health,
        )

        with patch(
            "hexawyn.mcp.server.build_cluster_operator_status_adapter",
            side_effect=RuntimeError("openshift unreachable"),
        ):
            result = check_cluster_operator_health()

        assert isinstance(result, dict)
        assert "openshift unreachable" in str(result["error"])
        assert result["total"] == 0
