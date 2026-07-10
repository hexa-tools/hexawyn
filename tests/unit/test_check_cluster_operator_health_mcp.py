"""RED → GREEN — MCP tool: check_cluster_operator_health."""

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.cluster_operator_status_port import (
    ClusterOperatorRawData,
    ClusterOperatorStatusPort,
)
from hexawyn.domain.errors import ClusterOperatorCRDNotFoundError


def _raw(name: str, degraded: bool = False, since: str | None = None) -> ClusterOperatorRawData:
    return ClusterOperatorRawData(
        name=name,
        available=True,
        progressing=False,
        degraded=degraded,
        available_unknown=False,
        message="etcd member ip-10-0-1-5 is not responding" if degraded else "",
        degraded_since=since,
    )


class TestCheckClusterOperatorHealthTool:
    def test_delegates_and_returns_summary(self) -> None:
        mock_port = MagicMock(spec=ClusterOperatorStatusPort)
        mock_port.list_cluster_operators.return_value = [
            _raw("authentication"),
            _raw("etcd", degraded=True, since="2026-06-16T01:00:00Z"),
        ]

        with patch(
            "hexawyn.mcp.server.build_cluster_operator_status_adapter",
            return_value=mock_port,
        ):
            from hexawyn.mcp.tools.check_cluster_operator_health import (
                check_cluster_operator_health,
            )

            result = check_cluster_operator_health()

        assert result["total"] == 2
        assert result["degraded"] == 1
        assert result["all_healthy"] is False
        assert result["error"] is None
        etcd = next(op for op in result["operators"] if op["name"] == "etcd")
        assert etcd["health"] == "degraded"
        assert "not responding" in etcd["message"]

    def test_handles_crd_absent_gracefully(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_cluster_operator_status_adapter",
            side_effect=ClusterOperatorCRDNotFoundError(),
        ):
            from hexawyn.mcp.tools.check_cluster_operator_health import (
                check_cluster_operator_health,
            )

            result = check_cluster_operator_health()

        assert result["all_healthy"] is False
        assert result["total"] == 0
        assert "OpenShift" in result["error"]

    def test_has_register_function(self) -> None:
        from hexawyn.mcp.tools.check_cluster_operator_health import register

        assert callable(register)
