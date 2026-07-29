from __future__ import annotations

import pytest
from hexawyn.domain.models.simulation import (
    ImpactReport,
    RiskLevel,
    ScenarioInput,
    ServiceImpact,
)


class TestScenarioInput:
    def test_is_frozen(self) -> None:
        cmd = ScenarioInput(
            target_service="auth-service",
            namespace="production",
            current_replicas=3,
            proposed_replicas=1,
            current_cpu_utilization=62.0,
        )
        with pytest.raises(AttributeError):
            cmd.target_service = "other"  # type: ignore[misc]

    def test_all_fields_populated(self) -> None:
        cmd = ScenarioInput(
            target_service="auth-service",
            namespace="production",
            current_replicas=3,
            proposed_replicas=1,
            current_cpu_utilization=62.0,
        )
        assert cmd.target_service == "auth-service"
        assert cmd.namespace == "production"
        assert cmd.current_replicas == 3  # noqa: PLR2004
        assert cmd.proposed_replicas == 1
        assert cmd.current_cpu_utilization == 62.0  # noqa: PLR2004

    def test_repr_contains_key_fields(self) -> None:
        cmd = ScenarioInput(
            target_service="auth-service",
            namespace="staging",
            current_replicas=5,
            proposed_replicas=3,
            current_cpu_utilization=20.0,
        )
        rep = repr(cmd)
        assert "auth-service" in rep
        assert "staging" in rep


class TestRiskLevel:
    def test_has_four_levels(self) -> None:
        levels = list(RiskLevel)
        assert len(levels) == 4  # noqa: PLR2004

    def test_low_lt_medium(self) -> None:
        assert RiskLevel.LOW.value < RiskLevel.MEDIUM.value

    def test_high_lt_critical(self) -> None:
        assert RiskLevel.HIGH.value < RiskLevel.CRITICAL.value

    def test_levels_ordered_by_severity(self) -> None:
        assert RiskLevel.LOW < RiskLevel.MEDIUM < RiskLevel.HIGH < RiskLevel.CRITICAL


class TestServiceImpact:
    def test_creates_with_expected_fields(self) -> None:
        impact = ServiceImpact(
            name="checkout-service",
            calls_per_second=450,
            estimated_latency_delta_percent=35,
        )
        assert impact.name == "checkout-service"
        assert impact.calls_per_second == 450  # noqa: PLR2004
        assert impact.estimated_latency_delta_percent == 35  # noqa: PLR2004

    def test_default_latency_delta_is_zero(self) -> None:
        impact = ServiceImpact(name="payment-service", calls_per_second=200)
        assert impact.estimated_latency_delta_percent == 0


class TestImpactReport:
    def test_default_values(self) -> None:
        report = ImpactReport(
            target_service="auth-service",
            namespace="production",
            current_replicas=3,
            proposed_replicas=1,
            risk=RiskLevel.HIGH,
        )
        assert report.affected_services == []
        assert report.pdb_violation is False
        assert report.hpa_detected is False
        assert report.circular_dependency is False
        assert report.recommendation == ""

    def test_with_dependent_services(self) -> None:
        services = [
            ServiceImpact(
                name="checkout-service", calls_per_second=450, estimated_latency_delta_percent=35
            ),
            ServiceImpact(
                name="payment-service", calls_per_second=200, estimated_latency_delta_percent=15
            ),
        ]
        report = ImpactReport(
            target_service="auth-service",
            namespace="production",
            current_replicas=3,
            proposed_replicas=1,
            risk=RiskLevel.HIGH,
            affected_services=services,
            estimated_latency_increase_percent=35.0,
            error_risk="potential 503s under peak load",
            recommendation="Do not scale below 2 replicas during business hours",
        )
        assert len(report.affected_services) == 2  # noqa: PLR2004
        assert report.estimated_latency_increase_percent == 35.0  # noqa: PLR2004
        assert report.recommendation != ""

    def test_pdb_violation_flag(self) -> None:
        report = ImpactReport(
            target_service="auth-service",
            namespace="production",
            current_replicas=3,
            proposed_replicas=1,
            risk=RiskLevel.CRITICAL,
            pdb_violation=True,
            recommendation="Scaling to 1 violates PDB minAvailable=2",
        )
        assert report.pdb_violation is True

    def test_hpa_detected_flag(self) -> None:
        report = ImpactReport(
            target_service="auth-service",
            namespace="staging",
            current_replicas=2,
            proposed_replicas=1,
            risk=RiskLevel.MEDIUM,
            hpa_detected=True,
        )
        assert report.hpa_detected is True

    def test_scale_up_positive_impact(self) -> None:
        report = ImpactReport(
            target_service="auth-service",
            namespace="production",
            current_replicas=1,
            proposed_replicas=5,
            risk=RiskLevel.LOW,
            recommendation="Headroom increased — estimated capacity 5x current",
        )
        assert report.current_replicas < report.proposed_replicas
        assert report.risk == RiskLevel.LOW

    def test_circular_dependency_detected(self) -> None:
        report = ImpactReport(
            target_service="auth-service",
            namespace="production",
            current_replicas=3,
            proposed_replicas=1,
            risk=RiskLevel.HIGH,
            circular_dependency=True,
        )
        assert report.circular_dependency is True
