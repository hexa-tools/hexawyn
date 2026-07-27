"""Tests for MCP server adapter factories."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.cluster_certificate_health_port import (
    ClusterCertificateHealthPort,
)


class TestMCPClusterCertificateHealthAdapterFactory:
    def test_build_cluster_certificate_health_adapter_returns_port(self) -> None:
        from hexawyn.mcp.server import build_cluster_certificate_health_adapter

        with patch(
            "hexawyn.mcp.server.load_kubeconfig",
            return_value=MagicMock(),
        ):
            result = build_cluster_certificate_health_adapter()

        assert isinstance(result, ClusterCertificateHealthPort)
