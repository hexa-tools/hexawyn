from unittest.mock import patch

from hexawyn.domain.errors import ClusterUnreachableError


class TestMCPServerStartup:
    def test_starts_in_degraded_mode_when_no_kubeconfig(self):
        with patch(
            "hexawyn.mcp.server.load_kubeconfig",
            side_effect=ClusterUnreachableError("no kubeconfig"),
        ):
            # Server should not crash — imports without error
            import hexawyn.mcp.server  # noqa: F401

    def test_health_includes_cluster_status(self):
        from hexawyn.mcp.server import health

        result = health.fn()
        assert "cluster" in result
        assert "status" in result
