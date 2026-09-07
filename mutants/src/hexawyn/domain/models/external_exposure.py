from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

ServiceType = Literal["LoadBalancer", "NodePort"]
RiskLevel = Literal["critical", "high", "medium", "low"]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class ExternalExposureFinding:
    name: str
    namespace: str
    service_type: ServiceType
    ports: list[int]
    external_ip: str | None
    external_hostname: str | None
    node_port: int | None
    is_pending: bool
    risk_level: RiskLevel
    note: str | None


@dataclass(frozen=True)
class ExcludedExposure:
    name: str
    namespace: str
    reason: str


@dataclass(frozen=True)
class ExternalExposureReport:
    findings: list[ExternalExposureFinding]
    excluded_exposures: list[ExcludedExposure]
    total_external_services_checked: int
    summary: str
