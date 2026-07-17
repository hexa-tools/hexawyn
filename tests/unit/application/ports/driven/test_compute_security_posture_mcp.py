"""RED → GREEN — MCP tool: compute_security_posture."""

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.security_posture_port import (
    SecurityPosturePort,
    WorkloadComplianceRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError

_ALL = ["tls", "rbac", "pod_security", "image_scanning", "secret_rotation"]


def _raw(workload: str, category: str, compliant: bool = True) -> WorkloadComplianceRaw:
    return WorkloadComplianceRaw(
        workload=workload,
        namespace="production",
        category=category,
        compliant=compliant,
        exempt=False,
        detail="" if compliant else f"{category} violation",
    )


def _port(records: list[WorkloadComplianceRaw], partial: bool = False) -> MagicMock:
    port = MagicMock(spec=SecurityPosturePort)
    port.list_workload_compliance.return_value = records
    port.get_defined_categories.return_value = _ALL
    port.is_partial.return_value = partial
    return port


class TestComputeSecurityPostureTool:
    def test_returns_score_and_breakdown(self) -> None:
        records = [_raw(f"tls{i}", "tls", compliant=i >= 5) for i in range(10)]
        records += [_raw(f"ok{i}", category) for i in range(10) for category in _ALL[1:]]

        with patch(
            "hexawyn.mcp.server.build_security_posture_adapter",
            return_value=_port(records),
        ):
            from hexawyn.mcp.tools.compute_security_posture import compute_security_posture

            result = compute_security_posture()

        assert 0 <= result["overall_score_pct"] <= 100
        tls = next(c for c in result["categories"] if c["category"] == "tls")
        assert tls["score_pct"] == 50.0
        assert result["error"] is None

    def test_remediation_order_present(self) -> None:
        records = [_raw("img-bad", "image_scanning", compliant=False)]
        records += [_raw("tls-bad", "tls", compliant=False)]

        with patch(
            "hexawyn.mcp.server.build_security_posture_adapter",
            return_value=_port(records),
        ):
            from hexawyn.mcp.tools.compute_security_posture import compute_security_posture

            result = compute_security_posture()

        assert result["remediation_order"][0]["category"] == "image_scanning"

    def test_passes_previous_score(self) -> None:
        records = [_raw(f"w{i}", category) for i in range(4) for category in _ALL]

        with patch(
            "hexawyn.mcp.server.build_security_posture_adapter",
            return_value=_port(records),
        ):
            from hexawyn.mcp.tools.compute_security_posture import compute_security_posture

            result = compute_security_posture(previous_score_pct=90.0)

        assert result["previous_score_pct"] == 90.0
        assert result["trend"] == "improving"

    def test_partial_flag_surfaced(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_security_posture_adapter",
            return_value=_port([_raw("w", "tls")], partial=True),
        ):
            from hexawyn.mcp.tools.compute_security_posture import compute_security_posture

            result = compute_security_posture()

        assert result["partial"] is True
        assert result["warning"] != ""

    def test_handles_error_gracefully(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_security_posture_adapter",
            side_effect=ClusterUnreachableError("down"),
        ):
            from hexawyn.mcp.tools.compute_security_posture import compute_security_posture

            result = compute_security_posture()

        assert result["overall_score_pct"] == 0.0
        assert "down" in result["error"]

    def test_has_register_function(self) -> None:
        from hexawyn.mcp.tools.compute_security_posture import register

        assert callable(register)
