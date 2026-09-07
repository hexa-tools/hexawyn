from __future__ import annotations

import pytest
from hexawyn.domain.models.simulation import (
    ImpactReport,
    RiskLevel,
    ScenarioInput,
    ServiceImpact,
)
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


def _engine() -> WhatIfScenarioSimulatorService:
    return WhatIfScenarioSimulatorService()


class TestHeadroomExact:
    def test_rounding_to_two_decimals(self) -> None:
        assert _engine().compute_capacity_headroom(16.0, 1, 3) == 5.33  # noqa: PLR2004

    def test_three_decimal_division_rounds(self) -> None:
        assert _engine().compute_capacity_headroom(33.333, 3, 1) == 100.0  # noqa: PLR2004

    def test_negative_proposed_returns_max_headroom(self) -> None:
        assert _engine().compute_capacity_headroom(50.0, 3, -1) == 999.0  # noqa: PLR2004


class TestRiskThresholdsExact:
    def test_headroom_200_is_critical(self) -> None:
        assert _engine().assess_risk_level(200.0, 3, 1) == RiskLevel.CRITICAL

    def test_headroom_150_is_high(self) -> None:
        assert _engine().assess_risk_level(150.0, 3, 1) == RiskLevel.HIGH

    def test_headroom_80_is_medium(self) -> None:
        assert _engine().assess_risk_level(80.0, 3, 1) == RiskLevel.MEDIUM

    def test_headroom_below_80_is_low(self) -> None:
        assert _engine().assess_risk_level(79.0, 3, 1) == RiskLevel.LOW

    def test_scale_up_ignores_high_headroom(self) -> None:
        assert _engine().assess_risk_level(500.0, 1, 3) == RiskLevel.LOW


class TestLatencyExact:
    def test_quarter_of_headroom(self) -> None:
        assert _engine().estimate_latency_delta_percent(100.0) == 25.0  # noqa: PLR2004

    def test_small_headroom_rounded_to_one_decimal(self) -> None:
        assert _engine().estimate_latency_delta_percent(4.0) == 1.0

    def test_fractional_headroom_rounding(self) -> None:
        assert _engine().estimate_latency_delta_percent(1.7) == 0.4  # noqa: PLR2004

    def test_latency_capped_at_200(self) -> None:
        assert _engine().estimate_latency_delta_percent(1000.0) == 200.0  # noqa: PLR2004

    def test_negative_headroom_returns_zero(self) -> None:
        assert _engine().estimate_latency_delta_percent(-5.0) == 0.0


class TestPDBViolationExact:
    def test_proposed_equal_to_min_available_is_not_violation(self) -> None:
        assert _engine().check_pdb_violation({"min_available": 2}, 2) is False

    def test_pdb_without_min_available_is_not_violation(self) -> None:
        assert _engine().check_pdb_violation({"max_unavailable": 1}, 1) is False

    def test_min_available_zero_never_violates(self) -> None:
        assert _engine().check_pdb_violation({"min_available": 0}, 0) is False


class TestHPAExact:
    def test_no_hpa_returns_default_dict(self) -> None:
        assert _engine().check_hpa_presence(None, 2) == {"detected": False, "can_compensate": False}

    def test_hpa_full_return_dict(self) -> None:
        hpa_info: dict[str, object] = {"min_replicas": 1, "max_replicas": 5, "current_replicas": 3}

        assert _engine().check_hpa_presence(hpa_info, 1) == {
            "detected": True,
            "can_compensate": True,
            "hpa_min": 1,
            "hpa_max": 5,
        }

    def test_hpa_cannot_compensate_below_bounds(self) -> None:
        hpa_info: dict[str, object] = {"min_replicas": 2, "max_replicas": 3, "current_replicas": 5}

        assert _engine().check_hpa_presence(hpa_info, 5) == {
            "detected": True,
            "can_compensate": False,
            "hpa_min": 2,
            "hpa_max": 3,
        }

    def test_hpa_float_bounds_truncated_to_int(self) -> None:
        hpa_info: dict[str, object] = {
            "min_replicas": 2.0,
            "max_replicas": 5.9,
            "current_replicas": 3,
        }

        assert _engine().check_hpa_presence(hpa_info, 1) == {
            "detected": True,
            "can_compensate": True,
            "hpa_min": 2,
            "hpa_max": 5,
        }

    def test_hpa_string_bounds_ignored(self) -> None:
        hpa_info: dict[str, object] = {
            "min_replicas": "2",
            "max_replicas": "5",
            "current_replicas": 3,
        }

        assert _engine().check_hpa_presence(hpa_info, 1) == {
            "detected": True,
            "can_compensate": False,
            "hpa_min": 0,
            "hpa_max": 0,
        }


class TestCircularDependencyExact:
    def test_self_loop_detected(self) -> None:
        assert _engine().detect_circular_dependency("A", {"A": ["A"]}) is True

    def test_cycle_beyond_max_depth_not_detected(self) -> None:
        graph: dict[str, list[str]] = {}
        for index in range(22):
            graph[f"n{index}"] = [f"n{index + 1}"]
        graph["n21"] = ["A"]

        assert _engine().detect_circular_dependency("A", graph) is False

    def test_long_chain_terminates(self) -> None:
        graph: dict[str, list[str]] = {}
        for index in range(30):
            graph[f"n{index}"] = [f"n{index + 1}"]

        assert _engine().detect_circular_dependency("n0", graph) is False


class TestExtractDependentServicesExact:
    def test_filters_non_dict_entries(self) -> None:
        topology: dict[str, object] = {
            "auth-service": [{"name": "svc"}, 42, {"name": "svc2"}, "junk"]
        }

        result = _engine()._extract_dependent_services("auth-service", topology)

        assert result == [{"name": "svc"}, {"name": "svc2"}]

    def test_missing_target_returns_empty(self) -> None:
        assert _engine()._extract_dependent_services("auth-service", {}) == []

    def test_non_list_value_returns_empty(self) -> None:
        assert _engine()._extract_dependent_services("auth-service", {"auth-service": {}}) == []


class TestRecommendationExact:
    def test_scale_up_recommendation(self) -> None:
        recommendation = _engine()._build_recommendation(
            RiskLevel.LOW,
            pdb_violation=False,
            hpa_detected=False,
            headroom=5.0,
            current_replicas=1,
            proposed_replicas=3,
        )
        assert recommendation == (
            "Headroom increase detected — scaling from 1 to 3 replicas adds capacity."
        )

    def test_critical_recommendation(self) -> None:
        recommendation = _engine()._build_recommendation(
            RiskLevel.CRITICAL,
            pdb_violation=False,
            hpa_detected=False,
            headroom=250.0,
            current_replicas=3,
            proposed_replicas=1,
        )
        assert recommendation == ("Do not scale below 3 replicas — critical saturation risk.")

    def test_high_recommendation_with_floor(self) -> None:
        recommendation = _engine()._build_recommendation(
            RiskLevel.HIGH,
            pdb_violation=False,
            hpa_detected=False,
            headroom=186.0,
            current_replicas=5,
            proposed_replicas=1,
        )
        assert recommendation == ("Do not scale below 4 replicas during business hours.")

    def test_high_recommendation_floor_at_two(self) -> None:
        recommendation = _engine()._build_recommendation(
            RiskLevel.HIGH,
            pdb_violation=False,
            hpa_detected=False,
            headroom=186.0,
            current_replicas=2,
            proposed_replicas=1,
        )
        assert recommendation == ("Do not scale below 2 replicas during business hours.")

    def test_medium_recommendation(self) -> None:
        recommendation = _engine()._build_recommendation(
            RiskLevel.MEDIUM,
            pdb_violation=False,
            hpa_detected=False,
            headroom=90.0,
            current_replicas=3,
            proposed_replicas=1,
        )
        assert recommendation == "Moderate risk — monitor closely after scaling."

    def test_low_recommendation_when_no_parts(self) -> None:
        recommendation = _engine()._build_recommendation(
            RiskLevel.LOW,
            pdb_violation=False,
            hpa_detected=False,
            headroom=10.0,
            current_replicas=3,
            proposed_replicas=1,
        )
        assert recommendation == "Low risk — change appears safe."

    def test_pdb_and_critical_recommendations_combined(self) -> None:
        recommendation = _engine()._build_recommendation(
            RiskLevel.CRITICAL,
            pdb_violation=True,
            hpa_detected=False,
            headroom=250.0,
            current_replicas=3,
            proposed_replicas=1,
        )
        assert recommendation == (
            "Scaling violates PodDisruptionBudget — change blocked. "
            "Do not scale below 3 replicas — critical saturation risk."
        )

    def test_high_with_hpa_recommendation(self) -> None:
        recommendation = _engine()._build_recommendation(
            RiskLevel.HIGH,
            pdb_violation=False,
            hpa_detected=True,
            headroom=186.0,
            current_replicas=5,
            proposed_replicas=1,
        )
        assert recommendation == (
            "Do not scale below 4 replicas during business hours. "
            "HPA detected — may compensate for scale-down within configured bounds."
        )


class TestScenarioFieldExact:
    def test_high_risk_fields_exact(self) -> None:
        scenario = _make_scenario()
        report = _engine().compute_scenario(scenario, {}, None, None)

        assert report.risk == RiskLevel.HIGH
        assert report.estimated_latency_increase_percent == 46.5  # noqa: PLR2004
        assert report.error_risk == "potential 503s under peak load"
        assert report.pdb_violation is False
        assert report.hpa_detected is False
        assert report.circular_dependency is False
        assert report.recommendation == "Do not scale below 2 replicas during business hours."

    def test_medium_error_risk_text(self) -> None:
        scenario = _make_scenario(current_replicas=2, proposed_replicas=1, current_cpu=45.0)
        report = _engine().compute_scenario(scenario, {}, None, None)

        assert report.risk == RiskLevel.MEDIUM
        assert report.error_risk == "increased error rate under sustained load"

    def test_low_risk_scale_up_error_risk_empty(self) -> None:
        scenario = _make_scenario(current_replicas=1, proposed_replicas=5, current_cpu=20.0)
        topology = _make_topology()
        report = _engine().compute_scenario(scenario, topology, None, None)

        assert report.risk == RiskLevel.LOW
        assert report.error_risk == ""
        assert report.affected_services == [
            ServiceImpact(
                name="checkout-service",
                calls_per_second=450.0,
                estimated_latency_delta_percent=1.0,
            ),
            ServiceImpact(
                name="payment-service",
                calls_per_second=200.0,
                estimated_latency_delta_percent=1.0,
            ),
        ]
        assert report.recommendation == (
            "Headroom increase detected — scaling from 1 to 5 replicas adds capacity."
        )


class TestErrorRiskBoundaries:
    def _error_risk_for_cpu(self, current_cpu: float) -> str:
        scenario = _make_scenario(
            current_replicas=3,
            proposed_replicas=3,
            current_cpu=current_cpu,
        )
        return _engine().compute_scenario(scenario, {}, None, None).error_risk

    def test_headroom_80_has_no_error_risk(self) -> None:
        assert self._error_risk_for_cpu(80.0) == ""

    def test_headroom_81_increased_error_rate(self) -> None:
        assert self._error_risk_for_cpu(81.0) == "increased error rate under sustained load"

    def test_headroom_100_increased_error_rate(self) -> None:
        assert self._error_risk_for_cpu(100.0) == "increased error rate under sustained load"

    def test_headroom_101_potential_503s(self) -> None:
        assert self._error_risk_for_cpu(101.0) == "potential 503s under peak load"


class TestScenarioIdentityFields:
    def test_identity_fields_match_scenario(self) -> None:
        scenario = _make_scenario()
        report = _engine().compute_scenario(scenario, {}, None, None)

        assert report.target_service == scenario.target_service
        assert report.namespace == scenario.namespace
        assert report.current_replicas == scenario.current_replicas
        assert report.proposed_replicas == scenario.proposed_replicas


class TestEqualReplicasRisk:
    def test_equal_replicas_still_uses_headroom_thresholds(self) -> None:
        assert _engine().assess_risk_level(250.0, 3, 3) == RiskLevel.CRITICAL


class TestLatencyOneHeadroom:
    def test_headroom_one_returns_quarter_rounded(self) -> None:
        assert _engine().estimate_latency_delta_percent(1.0) == 0.2  # noqa: PLR2004


class TestHPADefaults:
    def test_hpa_without_bounds_uses_zero_defaults(self) -> None:
        hpa_info: dict[str, object] = {"current_replicas": 3}

        assert _engine().check_hpa_presence(hpa_info, 5) == {
            "detected": True,
            "can_compensate": False,
            "hpa_min": 0,
            "hpa_max": 0,
        }

    def test_can_compensate_false_when_proposed_equals_bounds(self) -> None:
        hpa_info: dict[str, object] = {"min_replicas": 5, "max_replicas": 5, "current_replicas": 5}

        assert _engine().check_hpa_presence(hpa_info, 5) == {
            "detected": True,
            "can_compensate": False,
            "hpa_min": 5,
            "hpa_max": 5,
        }

    def test_can_compensate_false_when_proposed_equals_max(self) -> None:
        hpa_info: dict[str, object] = {"min_replicas": 2, "max_replicas": 5, "current_replicas": 5}

        assert _engine().check_hpa_presence(hpa_info, 5) == {
            "detected": True,
            "can_compensate": False,
            "hpa_min": 2,
            "hpa_max": 5,
        }


class TestCircularDepthExact:
    def test_cycle_just_beyond_default_depth_not_detected(self) -> None:
        graph: dict[str, list[str]] = {"A": ["n0"]}
        for index in range(19):
            graph[f"n{index}"] = [f"n{index + 1}"]
        graph["n19"] = ["A"]

        assert _engine().detect_circular_dependency("A", graph) is False

    def test_revisited_node_does_not_abort_later_detection(self) -> None:
        graph: dict[str, list[str]] = {
            "A": ["D", "C"],
            "C": ["B"],
            "B": ["C"],
            "D": ["A"],
        }

        assert _engine().detect_circular_dependency("A", graph) is True

    def test_non_target_cycle_terminates_as_false(self) -> None:
        graph: dict[str, list[str]] = {
            "X": ["A"],
            "A": ["B"],
            "B": ["A"],
        }

        assert _engine().detect_circular_dependency("X", graph) is False


class TestScenarioPdbHpaRecommendation:
    def test_pdb_and_hpa_reflected_in_recommendation(self) -> None:
        scenario = _make_scenario()
        topology: dict[str, object] = {}
        pdb_info: dict[str, object] = {"min_available": 2}
        hpa_info: dict[str, object] = {"min_replicas": 1, "max_replicas": 5, "current_replicas": 3}

        report = _engine().compute_scenario(scenario, topology, pdb_info, hpa_info)

        assert report.pdb_violation is True
        assert report.hpa_detected is True
        assert report.recommendation == (
            "Scaling violates PodDisruptionBudget — change blocked. "
            "Do not scale below 2 replicas during business hours. "
            "HPA detected — may compensate for scale-down within configured bounds."
        )
