"""RED → GREEN — Layer 1: ProbeAudit domain models."""

from hexawyn.domain.models.probe_audit import MissingProbe, ProbeAuditResult


class TestMissingProbe:
    def test_is_frozen(self) -> None:
        probe = MissingProbe(
            deployment_name="test",
            namespace="production",
            missing=[],
            severity="warning",
            exposed_port=0,
            readiness_suggestion="",
            liveness_suggestion="",
            has_service=False,
            workload_type="Deployment",
            is_exposed_externally=False,
        )
        assert probe.deployment_name == "test"
        assert probe.namespace == "production"
        assert probe.severity == "warning"

    def test_all_fields_accessible(self) -> None:
        probe = MissingProbe(
            deployment_name="payment-service",
            namespace="production",
            missing=["livenessProbe", "readinessProbe"],
            severity="critical",
            exposed_port=8080,
            readiness_suggestion="httpGet: /health",
            liveness_suggestion="httpGet: /health",
            has_service=True,
            workload_type="Deployment",
            is_exposed_externally=True,
        )
        assert probe.deployment_name == "payment-service"
        assert probe.exposed_port == 8080  # noqa: PLR2004
        assert probe.workload_type == "Deployment"
        assert probe.is_exposed_externally is True


class TestProbeAuditResult:
    def test_default_values(self) -> None:
        result = ProbeAuditResult()
        assert result.total_without_probes == 0
        assert result.critical == 0
        assert result.warning == 0
        assert result.informational == 0
        assert result.missing_probes == []
        assert result.misconfigured_probes == []

    def test_can_append_missing_probe(self) -> None:
        result = ProbeAuditResult()
        probe = MissingProbe(
            deployment_name="svc",
            namespace="prod",
            missing=["livenessProbe"],
            severity="warning",
            exposed_port=8080,
            readiness_suggestion="",
            liveness_suggestion="",
            has_service=True,
            workload_type="Deployment",
            is_exposed_externally=False,
        )
        result.missing_probes.append(probe)
        assert len(result.missing_probes) == 1
        assert result.missing_probes[0].deployment_name == "svc"
