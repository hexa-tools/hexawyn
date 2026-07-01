from __future__ import annotations

from hexawyn.domain.models.simulation import ImpactReport, RiskLevel, ScenarioInput, ServiceImpact


class WhatIfScenarioSimulatorService:
    _HEADROOM_MEDIUM_THRESHOLD: float = 80.0
    _HEADROOM_HIGH_THRESHOLD: float = 150.0
    _HEADROOM_CRITICAL_THRESHOLD: float = 200.0

    # ── public orchestration ──────────────────────────────────────
    def compute_scenario(
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
        if headroom > 100:
            error_risk = "potential 503s under peak load"
        elif headroom > 80:
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

    # ── pure functions ────────────────────────────────────────────
    @staticmethod
    def compute_capacity_headroom(
        current_cpu_utilization: float,
        current_replicas: int,
        proposed_replicas: int,
    ) -> float:
        if proposed_replicas <= 0:
            return 999.0
        return round(current_cpu_utilization * current_replicas / proposed_replicas, 2)

    @classmethod
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

    @staticmethod
    def estimate_latency_delta_percent(headroom_percent: float) -> float:
        if headroom_percent <= 0:
            return 0.0
        return round(min(headroom_percent * 0.25, 200.0), 1)

    @staticmethod
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

    # ── private helpers ───────────────────────────────────────────
    @staticmethod
    def _extract_dependent_services(
        target: str,
        topology: dict[str, object],
    ) -> list[dict[str, object]]:
        raw = topology.get(target, [])
        if isinstance(raw, list):
            return [svc for svc in raw if isinstance(svc, dict)]
        return []

    @staticmethod
    def _build_recommendation(
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
                f"Headroom increase detected — scaling from {current_replicas} to {proposed_replicas} replicas adds capacity."
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


def _safe_float(value: object) -> float:
    if isinstance(value, int | float):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value)
        except ValueError:
            return 0.0
    return 0.0
