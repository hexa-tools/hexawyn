from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class RunWhatIfSimulationResponse:
    target_service: str = ""
    namespace: str = ""
    current_replicas: int = 0
    proposed_replicas: int = 0
    risk: str = ""
    risk_level: int = 0
    affected_services: list[dict[str, object]] = field(default_factory=list)
    estimated_latency_increase_percent: float = 0.0
    error_risk: str = ""
    pdb_violation: bool = False
    hpa_detected: bool = False
    circular_dependency: bool = False
    recommendation: str = ""
    error: str | None = None

    @classmethod
    def from_impact_report(cls, impact: object) -> RunWhatIfSimulationResponse:
        return cls(
            target_service=getattr(impact, "target_service", ""),
            namespace=getattr(impact, "namespace", ""),
            current_replicas=getattr(impact, "current_replicas", 0),
            proposed_replicas=getattr(impact, "proposed_replicas", 0),
            risk=str(getattr(impact, "risk", "")),
            risk_level=int(getattr(impact, "risk", 0)),
            affected_services=[
                {
                    "name": svc.name,
                    "calls_per_second": svc.calls_per_second,
                    "estimated_latency_delta_percent": svc.estimated_latency_delta_percent,
                }
                for svc in getattr(impact, "affected_services", [])
            ],
            estimated_latency_increase_percent=getattr(
                impact, "estimated_latency_increase_percent", 0.0
            ),
            error_risk=getattr(impact, "error_risk", ""),
            pdb_violation=getattr(impact, "pdb_violation", False),
            hpa_detected=getattr(impact, "hpa_detected", False),
            circular_dependency=getattr(impact, "circular_dependency", False),
            recommendation=getattr(impact, "recommendation", ""),
        )
