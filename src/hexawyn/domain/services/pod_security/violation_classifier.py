from __future__ import annotations

from hexawyn.domain.models.constants import PodSecurityConstants
from hexawyn.domain.models.pod_security import PSSLevel, Severity, ViolationType

_cfg = PodSecurityConstants()
_CRITICAL_VIOLATION_TYPES = frozenset({"privileged", "host_pid", "host_network", "host_ipc"})
_HIGH_SEVERITY_CAPABILITIES = frozenset(_cfg.high_severity_capabilities)


def classify_severity(violation_type: ViolationType, capability: str | None = None) -> Severity:
    if violation_type in _CRITICAL_VIOLATION_TYPES:
        return "critical"
    if violation_type == "run_as_root":
        return "high"
    if violation_type == "dangerous_capability":
        return "high" if capability in _HIGH_SEVERITY_CAPABILITIES else "medium"
    return "medium"


def classify_pss_level(violation_type: ViolationType) -> PSSLevel:
    return "Baseline" if violation_type in _CRITICAL_VIOLATION_TYPES else "Restricted"
