from __future__ import annotations

import pytest
from hexawyn.domain.models.simulation import ImpactReport, RiskLevel, ScenarioInput
from hexawyn.domain.services.simulation.what_if_scenario_simulator_service import (
    WhatIfScenarioSimulatorService,
)


def _make_scenario(
    current_replicas: int = 3,
    proposed_replicas: int = 1,
    current_cpu: float = 62.0,
) -> ScenarioInput:
    return ScenarioInput(
        target_service="auth-service",
        namespace="production",
        current_replicas=current_replicas,
        proposed_replicas=proposed_replicas,
        current_cpu_utilization=current_cpu,
    )


def _make_topology(
    dependent_services: list[dict[str, object]] | None = None,
) -> dict[str, object]:
    if dependent_services is None:
        dependent_services = [
            {"name": "checkout-service", "calls_per_second": 450},
            {"name": "payment-service", "calls_per_second": 200},
        ]
    return {"auth-service": dependent_services}


class TestComputeCapacityHeadroom:
    def test_headroom_saturates_on_scale_down(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        result = engine.compute_capacity_headroom(
            current_cpu_utilization=62.0,
            current_replicas=3,
            proposed_replicas=1,
        )
        assert result == pytest.approx(186.0)

    def test_headroom_increases_on_scale_up(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        result = engine.compute_capacity_headroom(
            current_cpu_utilization=20.0,
            current_replicas=1,
            proposed_replicas=5,
        )
        assert result == pytest.approx(4.0)

    def test_no_change_headroom_equals_current(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        result = engine.compute_capacity_headroom(
            current_cpu_utilization=50.0,
            current_replicas=3,
            proposed_replicas=3,
        )
        assert result == pytest.approx(50.0)

    def test_proposed_zero_returns_max_headroom(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        result = engine.compute_capacity_headroom(
            current_cpu_utilization=50.0,
            current_replicas=3,
            proposed_replicas=0,
        )
        assert result == 999.0  # noqa: PLR2004


class TestAssessRiskLevel:
    def test_3_to_1_at_62_pct_is_high(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        result = engine.assess_risk_level(
            headroom_percent=186.0,
            current_replicas=3,
            proposed_replicas=1,
        )
        assert result == RiskLevel.HIGH

    def test_5_to_3_at_20_pct_is_low(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        result = engine.assess_risk_level(
            headroom_percent=12.0,
            current_replicas=5,
            proposed_replicas=3,
        )
        assert result == RiskLevel.LOW

    def test_headroom_over_200_is_critical(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        result = engine.assess_risk_level(
            headroom_percent=250.0,
            current_replicas=2,
            proposed_replicas=1,
        )
        assert result == RiskLevel.CRITICAL

    def test_scale_up_always_low(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        result = engine.assess_risk_level(
            headroom_percent=5.0,
            current_replicas=1,
            proposed_replicas=3,
        )
        assert result == RiskLevel.LOW

    def test_headroom_100_is_medium(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        result = engine.assess_risk_level(
            headroom_percent=100.0,
            current_replicas=3,
            proposed_replicas=2,
        )
        assert result == RiskLevel.MEDIUM


class TestEstimateLatencyDelta:
    def test_high_headroom_gives_high_latency(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        result = engine.estimate_latency_delta_percent(headroom_percent=186.0)
        assert result > 30  # noqa: PLR2004

    def test_low_headroom_gives_low_latency(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        result = engine.estimate_latency_delta_percent(headroom_percent=12.0)
        assert result < 10  # noqa: PLR2004

    def test_no_headroom_no_latency(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        result = engine.estimate_latency_delta_percent(headroom_percent=0.0)
        assert result == 0.0


class TestCheckPDBViolation:
    def test_violates_pdb_min_available_2(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        pdb_info: dict[str, object] = {"min_available": 2, "max_unavailable": None}
        result = engine.check_pdb_violation(pdb_info=pdb_info, proposed_replicas=1)
        assert result is True

    def test_respects_pdb(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        pdb_info: dict[str, object] = {"min_available": 2, "max_unavailable": None}
        result = engine.check_pdb_violation(pdb_info=pdb_info, proposed_replicas=3)
        assert result is False

    def test_no_pdb_no_violation(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        result = engine.check_pdb_violation(pdb_info=None, proposed_replicas=1)
        assert result is False

    def test_pdb_with_string_min_available_not_violated(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        pdb_info: dict[str, object] = {"min_available": "50%"}
        result = engine.check_pdb_violation(pdb_info=pdb_info, proposed_replicas=1)
        assert result is False


class TestCheckHPAPresence:
    def test_hpa_can_compensate_scale_down(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        hpa_info: dict[str, object] = {"min_replicas": 1, "max_replicas": 5, "current_replicas": 3}
        result = engine.check_hpa_presence(hpa_info=hpa_info, proposed_replicas=1)
        assert result["detected"] is True
        assert result["can_compensate"] is True

    def test_no_hpa_returns_default(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        result = engine.check_hpa_presence(hpa_info=None, proposed_replicas=2)
        assert result["detected"] is False
        assert result["can_compensate"] is False

    def test_hpa_min_above_proposed(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        hpa_info: dict[str, object] = {"min_replicas": 3, "max_replicas": 10, "current_replicas": 5}
        result = engine.check_hpa_presence(hpa_info=hpa_info, proposed_replicas=1)
        assert result["detected"] is True
        assert result["can_compensate"] is True
        assert result["hpa_min"] == 3  # noqa: PLR2004


class TestDetectCircularDependency:
    def test_direct_circular_a_to_b_to_a(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        dependencies: dict[str, list[str]] = {
            "auth-service": ["checkout-service"],
            "checkout-service": ["auth-service"],
        }
        result = engine.detect_circular_dependency(
            target="auth-service",
            dependency_graph=dependencies,
        )
        assert result is True

    def test_no_circular_dependency(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        dependencies: dict[str, list[str]] = {
            "auth-service": ["checkout-service", "payment-service"],
        }
        result = engine.detect_circular_dependency(
            target="auth-service",
            dependency_graph=dependencies,
        )
        assert result is False

    def test_indirect_circular_a_to_b_to_c_to_a(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        dependencies: dict[str, list[str]] = {
            "auth-service": ["checkout-service"],
            "checkout-service": ["payment-service"],
            "payment-service": ["auth-service"],
        }
        result = engine.detect_circular_dependency(
            target="auth-service",
            dependency_graph=dependencies,
        )
        assert result is True

    def test_already_visited_node_skipped(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        dependencies: dict[str, list[str]] = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": ["D"],
            "D": [],
        }
        result = engine.detect_circular_dependency(
            target="A",
            dependency_graph=dependencies,
        )
        assert result is False

    def test_empty_dependency_graph(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        result = engine.detect_circular_dependency(
            target="A",
            dependency_graph={},
        )
        assert result is False


class TestComputeBaseline:
    def test_high_risk_scenario_with_dependents(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        scenario = _make_scenario()
        topology = _make_topology()
        pdb_info: dict[str, object] = {"min_available": 2}
        hpa_info: dict[str, object] | None = None

        report = engine.compute_scenario(
            scenario=scenario,
            topology=topology,
            pdb_info=pdb_info,
            hpa_info=hpa_info,
        )

        assert isinstance(report, ImpactReport)
        assert report.risk == RiskLevel.HIGH
        assert len(report.affected_services) == 2  # noqa: PLR2004
        assert report.pdb_violation is True
        assert report.hpa_detected is False

    def test_low_risk_scale_up(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        scenario = _make_scenario(current_replicas=1, proposed_replicas=5, current_cpu=20.0)
        topology = _make_topology(dependent_services=[])
        report = engine.compute_scenario(
            scenario=scenario,
            topology=topology,
            pdb_info=None,
            hpa_info=None,
        )

        assert report.risk == RiskLevel.LOW
        assert report.affected_services == []
        assert "headroom" in report.recommendation.lower()

    def test_no_dependents_isolated_change(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        scenario = _make_scenario()
        topology: dict[str, object] = {}
        report = engine.compute_scenario(
            scenario=scenario,
            topology=topology,
            pdb_info=None,
            hpa_info=None,
        )

        assert report.affected_services == []
        assert report.risk != RiskLevel.LOW

    def test_hpa_detected_and_reported(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        scenario = _make_scenario()
        topology = _make_topology()
        hpa_info: dict[str, object] = {"min_replicas": 1, "max_replicas": 5, "current_replicas": 3}

        report = engine.compute_scenario(
            scenario=scenario,
            topology=topology,
            pdb_info=None,
            hpa_info=hpa_info,
        )

        assert report.hpa_detected is True

    def test_circular_dependency_detected(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        scenario = _make_scenario()
        topology: dict[str, object] = {
            "auth-service": [
                {"name": "checkout-service", "calls_per_second": 100},
            ],
        }
        dependency_graph: dict[str, list[str]] = {
            "auth-service": ["checkout-service"],
            "checkout-service": ["auth-service"],
        }

        report = engine.compute_scenario(
            scenario=scenario,
            topology=topology,
            pdb_info=None,
            hpa_info=None,
            dependency_graph=dependency_graph,
        )

        assert report.circular_dependency is True

    def test_medium_risk_scenario(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        scenario = _make_scenario(current_replicas=3, proposed_replicas=1, current_cpu=40.0)
        topology: dict[str, object] = {}
        report = engine.compute_scenario(
            scenario=scenario,
            topology=topology,
            pdb_info=None,
            hpa_info=None,
        )

        assert report.risk == RiskLevel.MEDIUM
        assert "Moderate risk" in report.recommendation

    def test_critical_risk_with_pdb(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        scenario = _make_scenario(current_replicas=3, proposed_replicas=1, current_cpu=80.0)
        topology: dict[str, object] = {}
        pdb_info: dict[str, object] = {"min_available": 2}
        report = engine.compute_scenario(
            scenario=scenario,
            topology=topology,
            pdb_info=pdb_info,
            hpa_info=None,
        )

        assert report.risk == RiskLevel.CRITICAL
        assert report.pdb_violation is True
        assert "critical saturation risk" in report.recommendation

    def test_error_risk_for_medium_headroom(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        scenario = _make_scenario(current_replicas=2, proposed_replicas=1, current_cpu=45.0)
        topology: dict[str, object] = {}
        report = engine.compute_scenario(
            scenario=scenario,
            topology=topology,
            pdb_info=None,
            hpa_info=None,
        )

        assert report.risk == RiskLevel.MEDIUM
        assert "increased error rate" in report.error_risk

    def test_topology_with_string_rps_value(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        scenario = _make_scenario()
        topology: dict[str, object] = {
            "auth-service": [
                {"name": "checkout-service", "calls_per_second": "450.5"},
                {"name": "payment-service", "calls_per_second": None},
                {"name": "invalid-service", "calls_per_second": "not_a_number"},
            ],
        }
        report = engine.compute_scenario(
            scenario=scenario,
            topology=topology,
            pdb_info=None,
            hpa_info=None,
        )

        assert len(report.affected_services) == 3  # noqa: PLR2004
        assert report.affected_services[0].calls_per_second == 450.5  # noqa: PLR2004
        assert report.affected_services[1].calls_per_second == 0.0
        assert report.affected_services[2].calls_per_second == 0.0
        engine = WhatIfScenarioSimulatorService()
        scenario = _make_scenario()
        topology: dict[str, object] = {"auth-service": "invalid_not_a_list"}
        report = engine.compute_scenario(
            scenario=scenario,
            topology=topology,
            pdb_info=None,
            hpa_info=None,
        )

        assert report.affected_services == []

    def test_hpa_with_string_values_handled(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        scenario = _make_scenario()
        topology: dict[str, object] = {}
        hpa_info: dict[str, object] = {
            "min_replicas": "2",
            "max_replicas": "5",
            "current_replicas": 3,
        }
        report = engine.compute_scenario(
            scenario=scenario,
            topology=topology,
            pdb_info=None,
            hpa_info=hpa_info,
        )

        assert report.hpa_detected is True

    def test_low_risk_recommendation(self) -> None:
        engine = WhatIfScenarioSimulatorService()
        scenario = _make_scenario(
            current_replicas=3,
            proposed_replicas=3,
            current_cpu=30.0,
        )
        topology: dict[str, object] = {}
        report = engine.compute_scenario(
            scenario=scenario,
            topology=topology,
            pdb_info=None,
            hpa_info=None,
        )

        assert report.risk == RiskLevel.LOW
        assert "Low risk" in report.recommendation
