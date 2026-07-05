from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDetectNetworkSegmentationGapsTool:
    def test_returns_report(self) -> None:
        from hexawyn.mcp.tools.detect_network_segmentation_gaps import (
            detect_network_segmentation_gaps,
        )

        with patch("hexawyn.mcp.server.build_network_policy_audit_adapter") as build_adapter:
            port = MagicMock()
            port.list_namespaces_with_pod_counts.return_value = []
            port.list_network_policies.return_value = []
            port.has_calico_global_network_policies.return_value = False
            port.has_istio_strict_peer_authentication.return_value = False
            build_adapter.return_value = port

            result = detect_network_segmentation_gaps()

        assert result["error"] is None
        assert result["findings"] == []

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.detect_network_segmentation_gaps import (
            detect_network_segmentation_gaps,
        )

        with patch(
            "hexawyn.mcp.server.build_network_policy_audit_adapter",
            side_effect=RuntimeError("cluster unreachable"),
        ):
            result = detect_network_segmentation_gaps()

        assert "cluster unreachable" in result["error"]


class TestBuildNetworkPolicyAuditAdapterFactory:
    def test_build_network_policy_audit_adapter_returns_network_policy_audit_port(self) -> None:
        from hexawyn.application.ports.driven.network_policy_audit_port import (
            NetworkPolicyAuditPort,
        )
        from hexawyn.mcp.server import build_network_policy_audit_adapter

        result = build_network_policy_audit_adapter()

        assert isinstance(result, NetworkPolicyAuditPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.detect_network_segmentation_gaps")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
