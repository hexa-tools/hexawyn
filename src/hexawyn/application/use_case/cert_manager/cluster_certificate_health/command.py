from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ClusterCertificateHealthCommand:
    warning_days: int = 30
    critical_days: int = 7
    timeout_seconds: float = 10.0
    namespace: str = ""
