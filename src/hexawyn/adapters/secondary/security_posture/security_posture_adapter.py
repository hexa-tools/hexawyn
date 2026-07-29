from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.security_posture_port import (  # type: ignore
    SecurityPosturePort,
    WorkloadComplianceRaw,
)


class ComplianceCategoryProvider(Protocol):
    """One security-audit category normalized into posture records.

    Each provider wraps an existing audit (TLS, RBAC, Pod Security, image
    scanning, secret rotation) and returns its results as WorkloadComplianceRaw.
    """

    def category(self) -> str: ...

    def fetch(self) -> list[WorkloadComplianceRaw]: ...


class SecurityPostureAdapter(SecurityPosturePort):
    """Facade over the individual security audits.

    Fans out to each injected category provider, normalizing heterogeneous
    audit results into a single uniform contract for the domain. A provider
    that fails (e.g. times out on a large cluster) is skipped and its category
    is left undefined, marking the overall scan partial — the report degrades
    gracefully instead of crashing.
    """

    def __init__(self, providers: list[ComplianceCategoryProvider]) -> None:
        self._providers = providers
        self._defined_categories: list[str] = []
        self._partial = False

    def list_workload_compliance(self) -> list[WorkloadComplianceRaw]:
        records: list[WorkloadComplianceRaw] = []
        defined: list[str] = []
        partial = False
        for provider in self._providers:
            try:
                provider_records = provider.fetch()
            except Exception:
                partial = True
                continue
            records.extend(provider_records)
            defined.append(provider.category())
        self._defined_categories = defined
        self._partial = partial
        return records

    def get_defined_categories(self) -> list[str]:
        return self._defined_categories

    def is_partial(self) -> bool:
        return self._partial
