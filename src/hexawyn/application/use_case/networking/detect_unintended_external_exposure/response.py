from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict


class ExcludedExposureDict(TypedDict):
    name: str
    namespace: str
    reason: str


class ExternalExposureFindingDict(TypedDict):
    name: str
    namespace: str
    service_type: str
    ports: list[int]
    external_ip: str | None
    external_hostname: str | None
    node_port: int | None
    is_pending: bool
    risk_level: str
    note: str


@dataclass
class DetectUnintendedExternalExposureResponse:
    findings: list[ExternalExposureFindingDict] | None = None
    excluded_exposures: list[ExcludedExposureDict] | None = None
    total_external_services_checked: int = 0
    summary: str = ""
    error: str | None = None
