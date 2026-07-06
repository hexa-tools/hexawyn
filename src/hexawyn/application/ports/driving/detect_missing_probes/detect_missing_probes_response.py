from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.probe_audit import ProbeAuditResult


@dataclass
class DetectMissingProbesResponse:
    result: ProbeAuditResult
