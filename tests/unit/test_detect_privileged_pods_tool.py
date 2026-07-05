from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDetectPrivilegedPodsTool:
    def test_returns_report(self) -> None:
        from hexawyn.mcp.tools.detect_privileged_pods import detect_privileged_pods

        with patch("hexawyn.mcp.server.build_pod_security_adapter") as build_adapter:
            port = MagicMock()
            port.list_pod_security_specs.return_value = []
            port.get_namespace_psa_enforce_levels.return_value = {}
            build_adapter.return_value = port

            result = detect_privileged_pods()

        assert result["error"] is None
        assert result["findings"] == []

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.detect_privileged_pods import detect_privileged_pods

        with patch(
            "hexawyn.mcp.server.build_pod_security_adapter",
            side_effect=RuntimeError("cluster unreachable"),
        ):
            result = detect_privileged_pods()

        assert "cluster unreachable" in result["error"]


class TestBuildPodSecurityAdapterFactory:
    def test_build_pod_security_adapter_returns_pod_security_context_audit_port(self) -> None:
        from hexawyn.application.ports.driven.pod_security_context_audit_port import (
            PodSecurityContextAuditPort,
        )
        from hexawyn.mcp.server import build_pod_security_adapter

        result = build_pod_security_adapter()

        assert isinstance(result, PodSecurityContextAuditPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.detect_privileged_pods")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
