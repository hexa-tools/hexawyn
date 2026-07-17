from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.cross_cluster_incident_port import (
    ClusterFailureSignature,
    CrossClusterIncidentPort,
)
from hexawyn.domain.errors import ClusterUnreachableError


def _sigs() -> list[ClusterFailureSignature]:
    return [
        ClusterFailureSignature(
            cluster_name="prod-eu",
            failure_type="ImagePullBackOff",
            pod_count=8,
            onset_utc="2026-06-16T09:00:00Z",
            affected_service="payment-service",
            shared_dependency="ghcr.io",
        ),
        ClusterFailureSignature(
            cluster_name="prod-us",
            failure_type="ImagePullBackOff",
            pod_count=6,
            onset_utc="2026-06-16T09:02:00Z",
            affected_service="payment-service",
            shared_dependency="ghcr.io",
        ),
    ]


def _port(failures: list[ClusterFailureSignature]) -> MagicMock:
    port = MagicMock(spec=CrossClusterIncidentPort)
    port.list_all_cluster_failures.return_value = failures
    return port


class TestDetectCrossClusterIncidentTool:
    def test_global_registry_issue(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_cross_cluster_incident_adapter", return_value=_port(_sigs())
        ):
            from hexawyn.mcp.tools.detect_cross_cluster_incident import (
                detect_cross_cluster_incident,
            )

            result = detect_cross_cluster_incident()

        assert result["scope"] == "regional"
        assert result["common_failure_type"] == "ImagePullBackOff"
        assert len(result["affected_clusters"]) == 2
        assert result["error"] is None

    def test_no_failures_none(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_cross_cluster_incident_adapter", return_value=_port([])
        ):
            from hexawyn.mcp.tools.detect_cross_cluster_incident import (
                detect_cross_cluster_incident,
            )

            result = detect_cross_cluster_incident()
        assert result["scope"] == "none"

    def test_handles_error(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_cross_cluster_incident_adapter",
            side_effect=ClusterUnreachableError("down"),
        ):
            from hexawyn.mcp.tools.detect_cross_cluster_incident import (
                detect_cross_cluster_incident,
            )

            result = detect_cross_cluster_incident()
        assert "down" in result["error"]

    def test_has_register(self) -> None:
        from hexawyn.mcp.tools.detect_cross_cluster_incident import register

        assert callable(register)
