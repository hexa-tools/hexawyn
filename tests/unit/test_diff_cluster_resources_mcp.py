from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.cluster_diff_port import (
    ClusterDiffPort,
    ClusterInventoryData,
    ResourceInventoryRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError


def _inv(
    name: str = "staging", resources: list[ResourceInventoryRaw] | None = None
) -> ClusterInventoryData:
    return ClusterInventoryData(cluster_name=name, resources=resources or [])


def _port(staging: ClusterInventoryData, prod: ClusterInventoryData) -> MagicMock:
    port = MagicMock(spec=ClusterDiffPort)
    port.get_resource_inventory.side_effect = [staging, prod]
    return port


class TestDiffClusterResourcesTool:
    def test_missing_resource_found(self) -> None:
        staging = _inv(
            "staging",
            [
                ResourceInventoryRaw(
                    kind="Deployment",
                    name="notification-service",
                    namespace="production",
                    image_tag="v1",
                    replicas=1,
                    is_secret=False,
                )
            ],
        )
        with patch(
            "hexawyn.mcp.server.build_cluster_diff_adapter",
            return_value=_port(staging, _inv("prod")),
        ):
            from hexawyn.mcp.tools.diff_cluster_resources import diff_cluster_resources

            result = diff_cluster_resources(source_context="staging", target_context="prod")

        assert result["sync_status"] == "out_of_sync"
        assert result["total_differences"] == 1
        assert result["error"] is None

    def test_in_sync(self) -> None:
        inv = _inv()
        with patch(
            "hexawyn.mcp.server.build_cluster_diff_adapter",
            return_value=_port(inv, inv),
        ):
            from hexawyn.mcp.tools.diff_cluster_resources import diff_cluster_resources

            result = diff_cluster_resources(source_context="staging", target_context="prod")

        assert result["sync_status"] == "in_sync"

    def test_handles_error(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_cluster_diff_adapter",
            side_effect=ClusterUnreachableError("down"),
        ):
            from hexawyn.mcp.tools.diff_cluster_resources import diff_cluster_resources

            result = diff_cluster_resources(source_context="staging", target_context="prod")
        assert "down" in result["error"]

    def test_has_register(self) -> None:
        from hexawyn.mcp.tools.diff_cluster_resources import register

        assert callable(register)
