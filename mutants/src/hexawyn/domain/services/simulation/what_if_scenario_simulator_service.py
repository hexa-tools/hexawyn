from __future__ import annotations

from hexawyn.domain.models.simulation import ImpactReport, RiskLevel, ScenarioInput, ServiceImpact


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut: MutantDict = {}  # type: ignore
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut: MutantDict = {}  # type: ignore
mutants_xǁWhatIfScenarioSimulatorServiceǁassess_risk_level__mutmut: MutantDict = {}  # type: ignore
mutants_xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut: MutantDict = {}  # type: ignore
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut: MutantDict = {}  # type: ignore
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut: MutantDict = {}  # type: ignore
mutants_xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut: MutantDict = {}  # type: ignore
mutants_xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut: MutantDict = {}  # type: ignore
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut: MutantDict = {}  # type: ignore


class WhatIfScenarioSimulatorService:
    _HEADROOM_MEDIUM_THRESHOLD: float = 80.0
    _HEADROOM_HIGH_THRESHOLD: float = 150.0
    _HEADROOM_CRITICAL_THRESHOLD: float = 200.0

    # ── public orchestration ──────────────────────────────────────
    @_mutmut_mutated(mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut)
    def compute_scenario(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_orig(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_1(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = None
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_2(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=None,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_3(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=None,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_4(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_5(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_6(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = None
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_7(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=None,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_8(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=None,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_9(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=None,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_10(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_11(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_12(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_13(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = None
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_14(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=None,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_15(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=None,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_16(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=None,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_17(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_18(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_19(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_20(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = None
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_21(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=None)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_22(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = None
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_23(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=None,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_24(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=None,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_25(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_26(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_27(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = None
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_28(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=None,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_29(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=None,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_30(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_31(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_32(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = None
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_33(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = True
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_34(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_35(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = None

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_36(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=None,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_37(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=None,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_38(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_39(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_40(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = None

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_41(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=None,
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_42(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=None,
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_43(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=None,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_44(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_45(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_46(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_47(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(None),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_48(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["XXnameXX"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_49(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["NAME"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_50(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(None),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_51(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get(None)),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_52(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("XXcalls_per_secondXX")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_53(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("CALLS_PER_SECOND")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_54(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = None
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_55(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = "XXXX"
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_56(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom >= 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_57(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 101:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_58(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = None
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_59(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "XXpotential 503s under peak loadXX"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_60(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "POTENTIAL 503S UNDER PEAK LOAD"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_61(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom >= 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_62(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 81:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_63(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = None

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_64(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "XXincreased error rate under sustained loadXX"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_65(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "INCREASED ERROR RATE UNDER SUSTAINED LOAD"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_66(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = None
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_67(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(None) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_68(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["XXdetectedXX"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_69(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["DETECTED"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_70(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["XXdetectedXX"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_71(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["DETECTED"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_72(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else True
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_73(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = None

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_74(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=None,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_75(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=None,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_76(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=None,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_77(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=None,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_78(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=None,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_79(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=None,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_80(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_81(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_82(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_83(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_84(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_85(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_86(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=None,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_87(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=None,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_88(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=None,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_89(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=None,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_90(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=None,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_91(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=None,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_92(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=None,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_93(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=None,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_94(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=None,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_95(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=None,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_96(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=None,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_97(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=None,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_98(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_99(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_100(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_101(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_102(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_103(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_104(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_105(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_106(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_107(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            circular_dependency=circular,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_108(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            recommendation=recommendation,
        )

    # ── public orchestration ──────────────────────────────────────
    def xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_109(  # noqa: PLR0913
        self,
        scenario: ScenarioInput,
        topology: dict[str, object],
        pdb_info: dict[str, object] | None,
        hpa_info: dict[str, object] | None,
        dependency_graph: dict[str, list[str]] | None = None,
    ) -> ImpactReport:
        dependent_services = self._extract_dependent_services(
            target=scenario.target_service,
            topology=topology,
        )
        headroom = self.compute_capacity_headroom(
            current_cpu_utilization=scenario.current_cpu_utilization,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        risk = self.assess_risk_level(
            headroom_percent=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )
        latency = self.estimate_latency_delta_percent(headroom_percent=headroom)
        pdb_violation = self.check_pdb_violation(
            pdb_info=pdb_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        hpa_result = self.check_hpa_presence(
            hpa_info=hpa_info,
            proposed_replicas=scenario.proposed_replicas,
        )
        circular = False
        if dependency_graph is not None:
            circular = self.detect_circular_dependency(
                target=scenario.target_service,
                dependency_graph=dependency_graph,
            )

        affected = [
            ServiceImpact(
                name=str(svc["name"]),
                calls_per_second=_safe_float(svc.get("calls_per_second")),
                estimated_latency_delta_percent=latency,
            )
            for svc in dependent_services
        ]

        error_risk = ""
        if headroom > 100:  # noqa: PLR2004
            error_risk = "potential 503s under peak load"
        elif headroom > 80:  # noqa: PLR2004
            error_risk = "increased error rate under sustained load"

        hpa_flag: bool = bool(hpa_result["detected"]) if hpa_result["detected"] else False
        recommendation = self._build_recommendation(
            risk=risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            headroom=headroom,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
        )

        return ImpactReport(
            target_service=scenario.target_service,
            namespace=scenario.namespace,
            current_replicas=scenario.current_replicas,
            proposed_replicas=scenario.proposed_replicas,
            risk=risk,
            affected_services=affected,
            estimated_latency_increase_percent=latency,
            error_risk=error_risk,
            pdb_violation=pdb_violation,
            hpa_detected=hpa_flag,
            circular_dependency=circular,
            )

    # ── pure functions ────────────────────────────────────────────
    @staticmethod
    @_mutmut_mutated(mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut)
    def compute_capacity_headroom(
        current_cpu_utilization: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> float:
        if proposed_replicas <= 0:
            return 999.0
        return round(current_cpu_utilization * current_replicas / proposed_replicas, 2)

    # ── pure functions ────────────────────────────────────────────
    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_orig(
        current_cpu_utilization: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> float:
        if proposed_replicas <= 0:
            return 999.0
        return round(current_cpu_utilization * current_replicas / proposed_replicas, 2)

    # ── pure functions ────────────────────────────────────────────
    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_1(
        current_cpu_utilization: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> float:
        if proposed_replicas < 0:
            return 999.0
        return round(current_cpu_utilization * current_replicas / proposed_replicas, 2)

    # ── pure functions ────────────────────────────────────────────
    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_2(
        current_cpu_utilization: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> float:
        if proposed_replicas <= 1:
            return 999.0
        return round(current_cpu_utilization * current_replicas / proposed_replicas, 2)

    # ── pure functions ────────────────────────────────────────────
    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_3(
        current_cpu_utilization: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> float:
        if proposed_replicas <= 0:
            return 1000.0
        return round(current_cpu_utilization * current_replicas / proposed_replicas, 2)

    # ── pure functions ────────────────────────────────────────────
    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_4(
        current_cpu_utilization: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> float:
        if proposed_replicas <= 0:
            return 999.0
        return round(None, 2)

    # ── pure functions ────────────────────────────────────────────
    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_5(
        current_cpu_utilization: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> float:
        if proposed_replicas <= 0:
            return 999.0
        return round(current_cpu_utilization * current_replicas / proposed_replicas, None)

    # ── pure functions ────────────────────────────────────────────
    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_6(
        current_cpu_utilization: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> float:
        if proposed_replicas <= 0:
            return 999.0
        return round(2)

    # ── pure functions ────────────────────────────────────────────
    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_7(
        current_cpu_utilization: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> float:
        if proposed_replicas <= 0:
            return 999.0
        return round(current_cpu_utilization * current_replicas / proposed_replicas, )

    # ── pure functions ────────────────────────────────────────────
    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_8(
        current_cpu_utilization: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> float:
        if proposed_replicas <= 0:
            return 999.0
        return round(current_cpu_utilization * current_replicas * proposed_replicas, 2)

    # ── pure functions ────────────────────────────────────────────
    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_9(
        current_cpu_utilization: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> float:
        if proposed_replicas <= 0:
            return 999.0
        return round(current_cpu_utilization / current_replicas / proposed_replicas, 2)

    # ── pure functions ────────────────────────────────────────────
    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_10(
        current_cpu_utilization: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> float:
        if proposed_replicas <= 0:
            return 999.0
        return round(current_cpu_utilization * current_replicas / proposed_replicas, 3)

    @classmethod
    @_mutmut_mutated(mutants_xǁWhatIfScenarioSimulatorServiceǁassess_risk_level__mutmut, is_classmethod = True)
    def assess_risk_level(
        cls,
        headroom_percent: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> RiskLevel:
        if proposed_replicas > current_replicas:
            return RiskLevel.LOW
        if headroom_percent >= cls._HEADROOM_CRITICAL_THRESHOLD:
            return RiskLevel.CRITICAL
        if headroom_percent >= cls._HEADROOM_HIGH_THRESHOLD:
            return RiskLevel.HIGH
        if headroom_percent >= cls._HEADROOM_MEDIUM_THRESHOLD:
            return RiskLevel.MEDIUM
        return RiskLevel.LOW

    @classmethod
    def xǁWhatIfScenarioSimulatorServiceǁassess_risk_level__mutmut_orig(
        cls,
        headroom_percent: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> RiskLevel:
        if proposed_replicas > current_replicas:
            return RiskLevel.LOW
        if headroom_percent >= cls._HEADROOM_CRITICAL_THRESHOLD:
            return RiskLevel.CRITICAL
        if headroom_percent >= cls._HEADROOM_HIGH_THRESHOLD:
            return RiskLevel.HIGH
        if headroom_percent >= cls._HEADROOM_MEDIUM_THRESHOLD:
            return RiskLevel.MEDIUM
        return RiskLevel.LOW

    @classmethod
    def xǁWhatIfScenarioSimulatorServiceǁassess_risk_level__mutmut_1(
        cls,
        headroom_percent: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> RiskLevel:
        if proposed_replicas >= current_replicas:
            return RiskLevel.LOW
        if headroom_percent >= cls._HEADROOM_CRITICAL_THRESHOLD:
            return RiskLevel.CRITICAL
        if headroom_percent >= cls._HEADROOM_HIGH_THRESHOLD:
            return RiskLevel.HIGH
        if headroom_percent >= cls._HEADROOM_MEDIUM_THRESHOLD:
            return RiskLevel.MEDIUM
        return RiskLevel.LOW

    @classmethod
    def xǁWhatIfScenarioSimulatorServiceǁassess_risk_level__mutmut_2(
        cls,
        headroom_percent: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> RiskLevel:
        if proposed_replicas > current_replicas:
            return RiskLevel.LOW
        if headroom_percent > cls._HEADROOM_CRITICAL_THRESHOLD:
            return RiskLevel.CRITICAL
        if headroom_percent >= cls._HEADROOM_HIGH_THRESHOLD:
            return RiskLevel.HIGH
        if headroom_percent >= cls._HEADROOM_MEDIUM_THRESHOLD:
            return RiskLevel.MEDIUM
        return RiskLevel.LOW

    @classmethod
    def xǁWhatIfScenarioSimulatorServiceǁassess_risk_level__mutmut_3(
        cls,
        headroom_percent: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> RiskLevel:
        if proposed_replicas > current_replicas:
            return RiskLevel.LOW
        if headroom_percent >= cls._HEADROOM_CRITICAL_THRESHOLD:
            return RiskLevel.CRITICAL
        if headroom_percent > cls._HEADROOM_HIGH_THRESHOLD:
            return RiskLevel.HIGH
        if headroom_percent >= cls._HEADROOM_MEDIUM_THRESHOLD:
            return RiskLevel.MEDIUM
        return RiskLevel.LOW

    @classmethod
    def xǁWhatIfScenarioSimulatorServiceǁassess_risk_level__mutmut_4(
        cls,
        headroom_percent: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> RiskLevel:
        if proposed_replicas > current_replicas:
            return RiskLevel.LOW
        if headroom_percent >= cls._HEADROOM_CRITICAL_THRESHOLD:
            return RiskLevel.CRITICAL
        if headroom_percent >= cls._HEADROOM_HIGH_THRESHOLD:
            return RiskLevel.HIGH
        if headroom_percent > cls._HEADROOM_MEDIUM_THRESHOLD:
            return RiskLevel.MEDIUM
        return RiskLevel.LOW

    @staticmethod
    @_mutmut_mutated(mutants_xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut)
    def estimate_latency_delta_percent(headroom_percent: float) -> float:
        if headroom_percent <= 0:
            return 0.0
        return round(min(headroom_percent * 0.25, 200.0), 1)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_orig(headroom_percent: float) -> float:
        if headroom_percent <= 0:
            return 0.0
        return round(min(headroom_percent * 0.25, 200.0), 1)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_1(headroom_percent: float) -> float:
        if headroom_percent < 0:
            return 0.0
        return round(min(headroom_percent * 0.25, 200.0), 1)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_2(headroom_percent: float) -> float:
        if headroom_percent <= 1:
            return 0.0
        return round(min(headroom_percent * 0.25, 200.0), 1)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_3(headroom_percent: float) -> float:
        if headroom_percent <= 0:
            return 1.0
        return round(min(headroom_percent * 0.25, 200.0), 1)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_4(headroom_percent: float) -> float:
        if headroom_percent <= 0:
            return 0.0
        return round(None, 1)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_5(headroom_percent: float) -> float:
        if headroom_percent <= 0:
            return 0.0
        return round(min(headroom_percent * 0.25, 200.0), None)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_6(headroom_percent: float) -> float:
        if headroom_percent <= 0:
            return 0.0
        return round(1)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_7(headroom_percent: float) -> float:
        if headroom_percent <= 0:
            return 0.0
        return round(min(headroom_percent * 0.25, 200.0), )

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_8(headroom_percent: float) -> float:
        if headroom_percent <= 0:
            return 0.0
        return round(min(None, 200.0), 1)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_9(headroom_percent: float) -> float:
        if headroom_percent <= 0:
            return 0.0
        return round(min(headroom_percent * 0.25, None), 1)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_10(headroom_percent: float) -> float:
        if headroom_percent <= 0:
            return 0.0
        return round(min(200.0), 1)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_11(headroom_percent: float) -> float:
        if headroom_percent <= 0:
            return 0.0
        return round(min(headroom_percent * 0.25, ), 1)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_12(headroom_percent: float) -> float:
        if headroom_percent <= 0:
            return 0.0
        return round(min(headroom_percent / 0.25, 200.0), 1)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_13(headroom_percent: float) -> float:
        if headroom_percent <= 0:
            return 0.0
        return round(min(headroom_percent * 1.25, 200.0), 1)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_14(headroom_percent: float) -> float:
        if headroom_percent <= 0:
            return 0.0
        return round(min(headroom_percent * 0.25, 201.0), 1)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_15(headroom_percent: float) -> float:
        if headroom_percent <= 0:
            return 0.0
        return round(min(headroom_percent * 0.25, 200.0), 2)

    @staticmethod
    @_mutmut_mutated(mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut)
    def check_pdb_violation(
        pdb_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> bool:
        if pdb_info is None:
            return False
        min_available = pdb_info.get("min_available")
        if isinstance(min_available, int) and proposed_replicas < min_available:
            return True
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_orig(
        pdb_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> bool:
        if pdb_info is None:
            return False
        min_available = pdb_info.get("min_available")
        if isinstance(min_available, int) and proposed_replicas < min_available:
            return True
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_1(
        pdb_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> bool:
        if pdb_info is not None:
            return False
        min_available = pdb_info.get("min_available")
        if isinstance(min_available, int) and proposed_replicas < min_available:
            return True
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_2(
        pdb_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> bool:
        if pdb_info is None:
            return True
        min_available = pdb_info.get("min_available")
        if isinstance(min_available, int) and proposed_replicas < min_available:
            return True
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_3(
        pdb_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> bool:
        if pdb_info is None:
            return False
        min_available = None
        if isinstance(min_available, int) and proposed_replicas < min_available:
            return True
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_4(
        pdb_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> bool:
        if pdb_info is None:
            return False
        min_available = pdb_info.get(None)
        if isinstance(min_available, int) and proposed_replicas < min_available:
            return True
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_5(
        pdb_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> bool:
        if pdb_info is None:
            return False
        min_available = pdb_info.get("XXmin_availableXX")
        if isinstance(min_available, int) and proposed_replicas < min_available:
            return True
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_6(
        pdb_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> bool:
        if pdb_info is None:
            return False
        min_available = pdb_info.get("MIN_AVAILABLE")
        if isinstance(min_available, int) and proposed_replicas < min_available:
            return True
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_7(
        pdb_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> bool:
        if pdb_info is None:
            return False
        min_available = pdb_info.get("min_available")
        if isinstance(min_available, int) or proposed_replicas < min_available:
            return True
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_8(
        pdb_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> bool:
        if pdb_info is None:
            return False
        min_available = pdb_info.get("min_available")
        if isinstance(min_available, int) and proposed_replicas <= min_available:
            return True
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_9(
        pdb_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> bool:
        if pdb_info is None:
            return False
        min_available = pdb_info.get("min_available")
        if isinstance(min_available, int) and proposed_replicas < min_available:
            return False
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_10(
        pdb_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> bool:
        if pdb_info is None:
            return False
        min_available = pdb_info.get("min_available")
        if isinstance(min_available, int) and proposed_replicas < min_available:
            return True
        return True

    @staticmethod
    @_mutmut_mutated(mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut)
    def check_hpa_presence(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_orig(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_1(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is not None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_2(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"XXdetectedXX": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_3(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"DETECTED": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_4(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": True, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_5(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "XXcan_compensateXX": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_6(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "CAN_COMPENSATE": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_7(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": True}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_8(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = None
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_9(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get(None, 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_10(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", None)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_11(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get(0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_12(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", )
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_13(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("XXmin_replicasXX", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_14(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("MIN_REPLICAS", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_15(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 1)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_16(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = None
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_17(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get(None, 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_18(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", None)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_19(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get(0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_20(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", )
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_21(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("XXmax_replicasXX", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_22(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("MAX_REPLICAS", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_23(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 1)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_24(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = None
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_25(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(None) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_26(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 1
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_27(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = None
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_28(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(None) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_29(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 1
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_30(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = None
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_31(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas and min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_32(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas >= proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_33(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas >= proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_34(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "XXdetectedXX": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_35(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "DETECTED": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_36(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": False,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_37(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "XXcan_compensateXX": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_38(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "CAN_COMPENSATE": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_39(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "XXhpa_minXX": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_40(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "HPA_MIN": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_41(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 1,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_42(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "XXhpa_maxXX": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_43(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "HPA_MAX": max_replicas if isinstance(max_replicas, int) else 0,
        }

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_44(
        hpa_info: dict[str, object] | None,
        proposed_replicas: int,
    ) -> dict[str, object]:
        if hpa_info is None:
            return {"detected": False, "can_compensate": False}
        min_val = hpa_info.get("min_replicas", 0)
        max_val = hpa_info.get("max_replicas", 0)
        min_replicas: int = int(min_val) if isinstance(min_val, int | float) else 0
        max_replicas: int = int(max_val) if isinstance(max_val, int | float) else 0
        can_compensate = max_replicas > proposed_replicas or min_replicas > proposed_replicas
        return {
            "detected": True,
            "can_compensate": can_compensate,
            "hpa_min": min_replicas if isinstance(min_replicas, int) else 0,
            "hpa_max": max_replicas if isinstance(max_replicas, int) else 1,
        }

    @staticmethod
    @_mutmut_mutated(mutants_xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut)
    def detect_circular_dependency(
        target: str,
        dependency_graph: dict[str, list[str]],
        max_depth: int = 20,
    ) -> bool:
        visited: set[str] = set()
        stack: list[str] = [target]
        while stack and len(visited) < max_depth:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            for neighbor in dependency_graph.get(current, []):
                if neighbor == target:
                    return True
                stack.append(neighbor)
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_orig(
        target: str,
        dependency_graph: dict[str, list[str]],
        max_depth: int = 20,
    ) -> bool:
        visited: set[str] = set()
        stack: list[str] = [target]
        while stack and len(visited) < max_depth:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            for neighbor in dependency_graph.get(current, []):
                if neighbor == target:
                    return True
                stack.append(neighbor)
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_1(
        target: str,
        dependency_graph: dict[str, list[str]],
        max_depth: int = 21,
    ) -> bool:
        visited: set[str] = set()
        stack: list[str] = [target]
        while stack and len(visited) < max_depth:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            for neighbor in dependency_graph.get(current, []):
                if neighbor == target:
                    return True
                stack.append(neighbor)
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_2(
        target: str,
        dependency_graph: dict[str, list[str]],
        max_depth: int = 20,
    ) -> bool:
        visited: set[str] = None
        stack: list[str] = [target]
        while stack and len(visited) < max_depth:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            for neighbor in dependency_graph.get(current, []):
                if neighbor == target:
                    return True
                stack.append(neighbor)
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_3(
        target: str,
        dependency_graph: dict[str, list[str]],
        max_depth: int = 20,
    ) -> bool:
        visited: set[str] = set()
        stack: list[str] = None
        while stack and len(visited) < max_depth:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            for neighbor in dependency_graph.get(current, []):
                if neighbor == target:
                    return True
                stack.append(neighbor)
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_4(
        target: str,
        dependency_graph: dict[str, list[str]],
        max_depth: int = 20,
    ) -> bool:
        visited: set[str] = set()
        stack: list[str] = [target]
        while stack or len(visited) < max_depth:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            for neighbor in dependency_graph.get(current, []):
                if neighbor == target:
                    return True
                stack.append(neighbor)
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_5(
        target: str,
        dependency_graph: dict[str, list[str]],
        max_depth: int = 20,
    ) -> bool:
        visited: set[str] = set()
        stack: list[str] = [target]
        while stack and len(visited) <= max_depth:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            for neighbor in dependency_graph.get(current, []):
                if neighbor == target:
                    return True
                stack.append(neighbor)
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_6(
        target: str,
        dependency_graph: dict[str, list[str]],
        max_depth: int = 20,
    ) -> bool:
        visited: set[str] = set()
        stack: list[str] = [target]
        while stack and len(visited) < max_depth:
            current = None
            if current in visited:
                continue
            visited.add(current)
            for neighbor in dependency_graph.get(current, []):
                if neighbor == target:
                    return True
                stack.append(neighbor)
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_7(
        target: str,
        dependency_graph: dict[str, list[str]],
        max_depth: int = 20,
    ) -> bool:
        visited: set[str] = set()
        stack: list[str] = [target]
        while stack and len(visited) < max_depth:
            current = stack.pop()
            if current not in visited:
                continue
            visited.add(current)
            for neighbor in dependency_graph.get(current, []):
                if neighbor == target:
                    return True
                stack.append(neighbor)
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_8(
        target: str,
        dependency_graph: dict[str, list[str]],
        max_depth: int = 20,
    ) -> bool:
        visited: set[str] = set()
        stack: list[str] = [target]
        while stack and len(visited) < max_depth:
            current = stack.pop()
            if current in visited:
                break
            visited.add(current)
            for neighbor in dependency_graph.get(current, []):
                if neighbor == target:
                    return True
                stack.append(neighbor)
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_9(
        target: str,
        dependency_graph: dict[str, list[str]],
        max_depth: int = 20,
    ) -> bool:
        visited: set[str] = set()
        stack: list[str] = [target]
        while stack and len(visited) < max_depth:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(None)
            for neighbor in dependency_graph.get(current, []):
                if neighbor == target:
                    return True
                stack.append(neighbor)
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_10(
        target: str,
        dependency_graph: dict[str, list[str]],
        max_depth: int = 20,
    ) -> bool:
        visited: set[str] = set()
        stack: list[str] = [target]
        while stack and len(visited) < max_depth:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            for neighbor in dependency_graph.get(None, []):
                if neighbor == target:
                    return True
                stack.append(neighbor)
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_11(
        target: str,
        dependency_graph: dict[str, list[str]],
        max_depth: int = 20,
    ) -> bool:
        visited: set[str] = set()
        stack: list[str] = [target]
        while stack and len(visited) < max_depth:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            for neighbor in dependency_graph.get(current, None):
                if neighbor == target:
                    return True
                stack.append(neighbor)
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_12(
        target: str,
        dependency_graph: dict[str, list[str]],
        max_depth: int = 20,
    ) -> bool:
        visited: set[str] = set()
        stack: list[str] = [target]
        while stack and len(visited) < max_depth:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            for neighbor in dependency_graph.get([]):
                if neighbor == target:
                    return True
                stack.append(neighbor)
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_13(
        target: str,
        dependency_graph: dict[str, list[str]],
        max_depth: int = 20,
    ) -> bool:
        visited: set[str] = set()
        stack: list[str] = [target]
        while stack and len(visited) < max_depth:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            for neighbor in dependency_graph.get(current, ):
                if neighbor == target:
                    return True
                stack.append(neighbor)
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_14(
        target: str,
        dependency_graph: dict[str, list[str]],
        max_depth: int = 20,
    ) -> bool:
        visited: set[str] = set()
        stack: list[str] = [target]
        while stack and len(visited) < max_depth:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            for neighbor in dependency_graph.get(current, []):
                if neighbor != target:
                    return True
                stack.append(neighbor)
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_15(
        target: str,
        dependency_graph: dict[str, list[str]],
        max_depth: int = 20,
    ) -> bool:
        visited: set[str] = set()
        stack: list[str] = [target]
        while stack and len(visited) < max_depth:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            for neighbor in dependency_graph.get(current, []):
                if neighbor == target:
                    return False
                stack.append(neighbor)
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_16(
        target: str,
        dependency_graph: dict[str, list[str]],
        max_depth: int = 20,
    ) -> bool:
        visited: set[str] = set()
        stack: list[str] = [target]
        while stack and len(visited) < max_depth:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            for neighbor in dependency_graph.get(current, []):
                if neighbor == target:
                    return True
                stack.append(None)
        return False

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_17(
        target: str,
        dependency_graph: dict[str, list[str]],
        max_depth: int = 20,
    ) -> bool:
        visited: set[str] = set()
        stack: list[str] = [target]
        while stack and len(visited) < max_depth:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            for neighbor in dependency_graph.get(current, []):
                if neighbor == target:
                    return True
                stack.append(neighbor)
        return True

    # ── private helpers ───────────────────────────────────────────
    @staticmethod
    @_mutmut_mutated(mutants_xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut)
    def _extract_dependent_services(
        target: str,
        topology: dict[str, object],
    ) -> list[dict[str, object]]:
        raw = topology.get(target, [])
        if isinstance(raw, list):
            return [svc for svc in raw if isinstance(svc, dict)]
        return []

    # ── private helpers ───────────────────────────────────────────
    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut_orig(
        target: str,
        topology: dict[str, object],
    ) -> list[dict[str, object]]:
        raw = topology.get(target, [])
        if isinstance(raw, list):
            return [svc for svc in raw if isinstance(svc, dict)]
        return []

    # ── private helpers ───────────────────────────────────────────
    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut_1(
        target: str,
        topology: dict[str, object],
    ) -> list[dict[str, object]]:
        raw = None
        if isinstance(raw, list):
            return [svc for svc in raw if isinstance(svc, dict)]
        return []

    # ── private helpers ───────────────────────────────────────────
    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut_2(
        target: str,
        topology: dict[str, object],
    ) -> list[dict[str, object]]:
        raw = topology.get(None, [])
        if isinstance(raw, list):
            return [svc for svc in raw if isinstance(svc, dict)]
        return []

    # ── private helpers ───────────────────────────────────────────
    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut_3(
        target: str,
        topology: dict[str, object],
    ) -> list[dict[str, object]]:
        raw = topology.get(target, None)
        if isinstance(raw, list):
            return [svc for svc in raw if isinstance(svc, dict)]
        return []

    # ── private helpers ───────────────────────────────────────────
    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut_4(
        target: str,
        topology: dict[str, object],
    ) -> list[dict[str, object]]:
        raw = topology.get([])
        if isinstance(raw, list):
            return [svc for svc in raw if isinstance(svc, dict)]
        return []

    # ── private helpers ───────────────────────────────────────────
    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut_5(
        target: str,
        topology: dict[str, object],
    ) -> list[dict[str, object]]:
        raw = topology.get(target, )
        if isinstance(raw, list):
            return [svc for svc in raw if isinstance(svc, dict)]
        return []

    @staticmethod
    @_mutmut_mutated(mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut)
    def _build_recommendation(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_orig(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_1(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = None

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_2(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas >= current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_3(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                None  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_4(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(None)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_5(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return "XX XX".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_6(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append(None)

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_7(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("XXScaling violates PodDisruptionBudget — change blocked.XX")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_8(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("scaling violates poddisruptionbudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_9(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("SCALING VIOLATES PODDISRUPTIONBUDGET — CHANGE BLOCKED.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_10(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk != RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_11(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                None
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_12(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk != RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_13(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = None
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_14(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(None, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_15(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, None)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_16(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_17(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, )
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_18(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas + 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_19(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 2, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_20(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 3)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_21(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(None)
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_22(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk != RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_23(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append(None)

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_24(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("XXModerate risk — monitor closely after scaling.XX")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_25(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_26(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("MODERATE RISK — MONITOR CLOSELY AFTER SCALING.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_27(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append(None)

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_28(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("XXHPA detected — may compensate for scale-down within configured bounds.XX")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_29(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("hpa detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_30(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA DETECTED — MAY COMPENSATE FOR SCALE-DOWN WITHIN CONFIGURED BOUNDS.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_31(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_32(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append(None)

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_33(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("XXLow risk — change appears safe.XX")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_34(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("low risk — change appears safe.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_35(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("LOW RISK — CHANGE APPEARS SAFE.")

        return " ".join(parts)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_36(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return " ".join(None)

    @staticmethod
    def xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_37(  # noqa: PLR0913
        risk: RiskLevel,
        pdb_violation: bool,
        hpa_detected: bool,
        headroom: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> str:
        parts: list[str] = []

        if proposed_replicas > current_replicas:
            parts.append(
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."  # noqa: E501
            )
            return " ".join(parts)

        if pdb_violation:
            parts.append("Scaling violates PodDisruptionBudget — change blocked.")

        if risk == RiskLevel.CRITICAL:
            parts.append(
                f"Do not scale below {current_replicas} replicas — critical saturation risk."
            )
        elif risk == RiskLevel.HIGH:
            safe = max(current_replicas - 1, 2)
            parts.append(f"Do not scale below {safe} replicas during business hours.")
        elif risk == RiskLevel.MEDIUM:
            parts.append("Moderate risk — monitor closely after scaling.")

        if hpa_detected:
            parts.append("HPA detected — may compensate for scale-down within configured bounds.")

        if not parts:
            parts.append("Low risk — change appears safe.")

        return "XX XX".join(parts)

mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['_mutmut_orig'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_1'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_2'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_3'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_4'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_4 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_5'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_5 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_6'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_6 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_7'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_7 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_8'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_8 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_9'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_9 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_10'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_10 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_11'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_11 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_12'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_12 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_13'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_13 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_14'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_14 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_15'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_15 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_16'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_16 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_17'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_17 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_18'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_18 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_19'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_19 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_20'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_20 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_21'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_21 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_22'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_22 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_23'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_23 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_24'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_24 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_25'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_25 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_26'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_26 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_27'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_27 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_28'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_28 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_29'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_29 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_30'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_30 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_31'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_31 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_32'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_32 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_33'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_33 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_34'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_34 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_35'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_35 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_36'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_36 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_37'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_37 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_38'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_38 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_39'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_39 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_40'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_40 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_41'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_41 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_42'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_42 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_43'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_43 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_44'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_44 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_45'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_45 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_46'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_46 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_47'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_47 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_48'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_48 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_49'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_49 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_50'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_50 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_51'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_51 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_52'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_52 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_53'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_53 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_54'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_54 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_55'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_55 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_56'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_56 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_57'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_57 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_58'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_58 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_59'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_59 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_60'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_60 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_61'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_61 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_62'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_62 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_63'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_63 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_64'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_64 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_65'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_65 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_66'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_66 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_67'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_67 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_68'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_68 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_69'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_69 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_70'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_70 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_71'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_71 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_72'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_72 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_73'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_73 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_74'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_74 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_75'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_75 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_76'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_76 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_77'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_77 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_78'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_78 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_79'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_79 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_80'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_80 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_81'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_81 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_82'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_82 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_83'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_83 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_84'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_84 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_85'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_85 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_86'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_86 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_87'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_87 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_88'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_88 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_89'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_89 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_90'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_90 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_91'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_91 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_92'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_92 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_93'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_93 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_94'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_94 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_95'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_95 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_96'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_96 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_97'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_97 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_98'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_98 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_99'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_99 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_100'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_100 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_101'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_101 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_102'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_102 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_103'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_103 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_104'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_104 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_105'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_105 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_106'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_106 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_107'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_107 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_108'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_108 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_109'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_scenario__mutmut_109 # type: ignore # mutmut generated

mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut['_mutmut_orig'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_1'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_2'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_3'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_4'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_4 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_5'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_5 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_6'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_6 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_7'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_7 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_8'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_8 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_9'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_9 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut['xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_10'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcompute_capacity_headroom__mutmut_10 # type: ignore # mutmut generated

mutants_xǁWhatIfScenarioSimulatorServiceǁassess_risk_level__mutmut['_mutmut_orig'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁassess_risk_level__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁassess_risk_level__mutmut['xǁWhatIfScenarioSimulatorServiceǁassess_risk_level__mutmut_1'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁassess_risk_level__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁassess_risk_level__mutmut['xǁWhatIfScenarioSimulatorServiceǁassess_risk_level__mutmut_2'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁassess_risk_level__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁassess_risk_level__mutmut['xǁWhatIfScenarioSimulatorServiceǁassess_risk_level__mutmut_3'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁassess_risk_level__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁassess_risk_level__mutmut['xǁWhatIfScenarioSimulatorServiceǁassess_risk_level__mutmut_4'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁassess_risk_level__mutmut_4 # type: ignore # mutmut generated

mutants_xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut['_mutmut_orig'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut['xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_1'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut['xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_2'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut['xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_3'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut['xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_4'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_4 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut['xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_5'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_5 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut['xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_6'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_6 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut['xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_7'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_7 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut['xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_8'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_8 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut['xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_9'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_9 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut['xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_10'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_10 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut['xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_11'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_11 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut['xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_12'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_12 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut['xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_13'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_13 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut['xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_14'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_14 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut['xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_15'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁestimate_latency_delta_percent__mutmut_15 # type: ignore # mutmut generated

mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut['_mutmut_orig'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_1'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_2'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_3'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_4'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_4 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_5'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_5 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_6'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_6 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_7'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_7 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_8'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_8 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_9'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_9 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_10'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_pdb_violation__mutmut_10 # type: ignore # mutmut generated

mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['_mutmut_orig'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_1'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_2'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_3'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_4'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_4 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_5'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_5 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_6'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_6 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_7'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_7 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_8'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_8 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_9'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_9 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_10'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_10 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_11'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_11 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_12'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_12 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_13'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_13 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_14'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_14 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_15'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_15 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_16'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_16 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_17'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_17 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_18'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_18 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_19'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_19 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_20'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_20 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_21'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_21 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_22'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_22 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_23'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_23 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_24'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_24 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_25'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_25 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_26'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_26 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_27'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_27 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_28'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_28 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_29'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_29 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_30'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_30 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_31'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_31 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_32'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_32 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_33'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_33 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_34'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_34 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_35'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_35 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_36'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_36 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_37'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_37 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_38'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_38 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_39'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_39 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_40'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_40 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_41'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_41 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_42'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_42 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_43'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_43 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut['xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_44'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁcheck_hpa_presence__mutmut_44 # type: ignore # mutmut generated

mutants_xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut['_mutmut_orig'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut['xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_1'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut['xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_2'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut['xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_3'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut['xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_4'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_4 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut['xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_5'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_5 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut['xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_6'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_6 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut['xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_7'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_7 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut['xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_8'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_8 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut['xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_9'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_9 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut['xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_10'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_10 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut['xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_11'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_11 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut['xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_12'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_12 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut['xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_13'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_13 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut['xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_14'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_14 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut['xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_15'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_15 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut['xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_16'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_16 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut['xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_17'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁdetect_circular_dependency__mutmut_17 # type: ignore # mutmut generated

mutants_xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut['_mutmut_orig'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut_1'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut_2'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut_3'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut_4'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut_4 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut_5'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_extract_dependent_services__mutmut_5 # type: ignore # mutmut generated

mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['_mutmut_orig'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_1'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_2'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_3'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_4'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_4 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_5'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_5 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_6'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_6 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_7'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_7 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_8'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_8 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_9'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_9 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_10'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_10 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_11'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_11 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_12'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_12 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_13'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_13 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_14'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_14 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_15'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_15 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_16'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_16 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_17'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_17 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_18'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_18 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_19'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_19 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_20'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_20 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_21'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_21 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_22'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_22 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_23'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_23 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_24'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_24 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_25'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_25 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_26'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_26 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_27'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_27 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_28'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_28 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_29'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_29 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_30'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_30 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_31'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_31 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_32'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_32 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_33'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_33 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_34'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_34 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_35'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_35 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_36'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_36 # type: ignore # mutmut generated
mutants_xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut['xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_37'] = WhatIfScenarioSimulatorService.xǁWhatIfScenarioSimulatorServiceǁ_build_recommendation__mutmut_37 # type: ignore # mutmut generated
mutants_x__safe_float__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__safe_float__mutmut)
def _safe_float(value: object) -> float:
    if isinstance(value, int | float):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value)
        except ValueError:
            return 0.0
    return 0.0


def x__safe_float__mutmut_orig(value: object) -> float:
    if isinstance(value, int | float):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value)
        except ValueError:
            return 0.0
    return 0.0


def x__safe_float__mutmut_1(value: object) -> float:
    if isinstance(value, int | float):
        return float(None)
    if isinstance(value, str):
        try:
            return float(value)
        except ValueError:
            return 0.0
    return 0.0


def x__safe_float__mutmut_2(value: object) -> float:
    if isinstance(value, int | float):
        return float(value)
    if isinstance(value, str):
        try:
            return float(None)
        except ValueError:
            return 0.0
    return 0.0


def x__safe_float__mutmut_3(value: object) -> float:
    if isinstance(value, int | float):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value)
        except ValueError:
            return 1.0
    return 0.0


def x__safe_float__mutmut_4(value: object) -> float:
    if isinstance(value, int | float):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value)
        except ValueError:
            return 0.0
    return 1.0

mutants_x__safe_float__mutmut['_mutmut_orig'] = x__safe_float__mutmut_orig # type: ignore # mutmut generated
mutants_x__safe_float__mutmut['x__safe_float__mutmut_1'] = x__safe_float__mutmut_1 # type: ignore # mutmut generated
mutants_x__safe_float__mutmut['x__safe_float__mutmut_2'] = x__safe_float__mutmut_2 # type: ignore # mutmut generated
mutants_x__safe_float__mutmut['x__safe_float__mutmut_3'] = x__safe_float__mutmut_3 # type: ignore # mutmut generated
mutants_x__safe_float__mutmut['x__safe_float__mutmut_4'] = x__safe_float__mutmut_4 # type: ignore # mutmut generated
