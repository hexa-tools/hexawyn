from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal, TypedDict


class ExternalExposureFindingDict(TypedDict):
    name: str
    namespace: str
    service_type: Literal["LoadBalancer", "NodePort"]
    ports: list[int]
    external_ip: str | None
    external_hostname: str | None
    node_port: int | None
    is_pending: bool
    risk_level: Literal["critical", "high", "medium", "low"]
    note: str | None


class ExcludedExposureDict(TypedDict):
    name: str
    namespace: str
    reason: str


@dataclass
class DetectUnintendedExternalExposureResponse:
    findings: list[ExternalExposureFindingDict] = field(default_factory=list)
    excluded_exposures: list[ExcludedExposureDict] = field(default_factory=list)
    total_external_services_checked: int = 0
    summary: str = ""
    error: str | None = None
