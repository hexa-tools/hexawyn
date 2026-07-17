from unittest.mock import MagicMock, patch

from hexawyn.domain.errors import ClusterUnreachableError
from hexawyn.domain.models.fleet_health import ClusterRawMetrics


def _metrics(
    failing: int = 5, total: int = 200, cpu: float = 0.72, nodes: int = 12
) -> ClusterRawMetrics:
    return ClusterRawMetrics(
        context_name="prod-eu",
        nodes_total=nodes,
        nodes_not_ready=0,
        pods_total=total,
        pods_running=total - failing,
        pods_crashloop=0,
        cpu_utilization=cpu,
        memory_utilization=0.68,
        certs_expiring_critical=0,
        certs_expiring_warning=0,
        security_violations=0,
        pipelines_failing=0,
        prometheus_available=True,
    )


def _port(a: ClusterRawMetrics, b: ClusterRawMetrics) -> MagicMock:
    port = MagicMock()
    port.get_cluster_raw_metrics.side_effect = [a, b]
    return port


class TestCompareClusterHealthTool:
    def test_prod_eu_worse(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_fleet_health_adapter",
            return_value=_port(
                _metrics(failing=5, total=200, cpu=0.72),
                _metrics(failing=1, total=100, cpu=0.45),
            ),
        ):
            from hexawyn.mcp.tools.compare_cluster_health import compare_cluster_health

            result = compare_cluster_health(cluster_a="prod-eu", cluster_b="prod-us")

        assert result["comparison"]["worse_cluster"] == "prod-eu"
        assert result["comparison"]["delta_failing_pods"] == 4
        assert result["error"] is None

    def test_both_healthy(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_fleet_health_adapter",
            return_value=_port(
                _metrics(failing=0, total=100, cpu=0.3),
                _metrics(failing=0, total=100, cpu=0.3),
            ),
        ):
            from hexawyn.mcp.tools.compare_cluster_health import compare_cluster_health

            result = compare_cluster_health(cluster_a="prod-eu", cluster_b="prod-us")
        assert "both" in result["comparison"]["reason"].lower()

    def test_handles_error(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_fleet_health_adapter",
            side_effect=ClusterUnreachableError("multi-cluster down"),
        ):
            from hexawyn.mcp.tools.compare_cluster_health import compare_cluster_health

            result = compare_cluster_health(cluster_a="a", cluster_b="b")
        assert "down" in result["error"]

    def test_has_register(self) -> None:
        from hexawyn.mcp.tools.compare_cluster_health import register

        assert callable(register)
