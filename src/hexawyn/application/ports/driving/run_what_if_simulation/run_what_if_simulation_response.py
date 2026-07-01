from __future__ import annotations

from dataclasses import dataclass, field

from hexawyn.domain.models.simulation import ImpactReport, RiskLevel


@dataclass
class RunWhatIfSimulationResponse:
    target_service: str = ""
    namespace: str = ""
    current_replicas: int = 0
    proposed_replicas: int = 0
    risk: RiskLevel = RiskLevel.LOW
    affected_services: list[str] = field(default_factory=list)
    estimated_latency_increase_percent: float = 0.0
    error_risk: str = ""
    pdb_violation: bool = False
    hpa_detected: bool = False
    circular_dependency: bool = False
    recommendation: str = ""

    @classmethod
    def from_impact_report(cls, report: ImpactReport) -> RunWhatIfSimulationResponse:
        return cls(
            target_service=report.target_service,
            namespace=report.namespace,
            current_replicas=report.current_replicas,
            proposed_replicas=report.proposed_replicas,
            risk=report.risk,
            affected_services=[svc.name for svc in report.affected_services],
            estimated_latency_increase_percent=report.estimated_latency_increase_percent,
            error_risk=report.error_risk,
            pdb_violation=report.pdb_violation,
            hpa_detected=report.hpa_detected,
            circular_dependency=report.circular_dependency,
            recommendation=report.recommendation,
        )
