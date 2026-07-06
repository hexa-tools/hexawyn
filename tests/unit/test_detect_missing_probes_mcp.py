"""RED → GREEN — MCP tool: detect_missing_probes."""

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.probe_audit_port import (
    ProbeAuditPort,
    ProbeContainerRawData,
    ProbeDeploymentRawData,
)
from hexawyn.domain.errors import ClusterUnreachableError


class TestDetectMissingProbesTool:
    def test_delegates_to_use_case_and_returns_dict(self) -> None:
        mock_port = MagicMock(spec=ProbeAuditPort)
        mock_port.get_probe_audit_data.return_value = [
            ProbeDeploymentRawData(
                deployment_name="payment-service",
                namespace="production",
                workload_type="Deployment",
                containers=[
                    ProbeContainerRawData(
                        container_name="main",
                        is_init_container=False,
                        exposed_ports=[8080],
                        has_liveness_probe=False,
                        has_readiness_probe=False,
                        liveness_probe_type="",
                        readiness_probe_type="",
                        liveness_http_path="",
                        readiness_http_path="",
                        liveness_port=0,
                        readiness_port=0,
                    ),
                ],
                has_service=True,
                is_exposed_externally=True,
            ),
        ]

        with patch("hexawyn.mcp.server.build_probe_audit_adapter", return_value=mock_port):
            from hexawyn.mcp.tools.detect_missing_probes import detect_missing_probes

            result = detect_missing_probes()

        assert result["total_without_probes"] == 1
        assert result["critical"] == 1
        assert result["error"] is None
        assert len(result["missing_probes"]) == 1
        assert result["missing_probes"][0]["deployment_name"] == "payment-service"
        assert result["missing_probes"][0]["severity"] == "critical"

    def test_passes_namespace_to_command(self) -> None:
        mock_port = MagicMock(spec=ProbeAuditPort)
        mock_port.get_probe_audit_data.return_value = []

        with patch("hexawyn.mcp.server.build_probe_audit_adapter", return_value=mock_port):
            from hexawyn.mcp.tools.detect_missing_probes import detect_missing_probes

            detect_missing_probes(namespace="production")

        mock_port.get_probe_audit_data.assert_called_once_with("production")

    def test_handles_exception_gracefully(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_probe_audit_adapter",
            side_effect=ClusterUnreachableError("cluster down"),
        ):
            from hexawyn.mcp.tools.detect_missing_probes import detect_missing_probes

            result = detect_missing_probes()

        assert result["total_without_probes"] == 0
        assert result["critical"] == 0
        assert result["error"] == "cluster down"

    def test_includes_misconfigured_in_result(self) -> None:
        mock_port = MagicMock(spec=ProbeAuditPort)
        mock_port.get_probe_audit_data.return_value = [
            ProbeDeploymentRawData(
                deployment_name="broken-probe",
                namespace="production",
                workload_type="Deployment",
                containers=[
                    ProbeContainerRawData(
                        container_name="app",
                        is_init_container=False,
                        exposed_ports=[8080],
                        has_liveness_probe=True,
                        has_readiness_probe=True,
                        liveness_probe_type="httpGet",
                        readiness_probe_type="httpGet",
                        liveness_http_path="/healthz",
                        readiness_http_path="/wrong-path",
                        liveness_port=8080,
                        readiness_port=9090,
                    ),
                ],
                has_service=True,
                is_exposed_externally=False,
            ),
        ]

        with patch("hexawyn.mcp.server.build_probe_audit_adapter", return_value=mock_port):
            from hexawyn.mcp.tools.detect_missing_probes import detect_missing_probes

            result = detect_missing_probes()

        assert len(result["misconfigured_probes"]) == 1
        assert result["misconfigured_probes"][0]["deployment_name"] == "broken-probe"

    def test_has_register_function(self) -> None:
        from hexawyn.mcp.tools.detect_missing_probes import register

        assert callable(register)
