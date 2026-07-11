from abc import ABC, abstractmethod
from typing import TypedDict


class WorkloadComplianceRaw(TypedDict):
    workload: str
    namespace: str
    category: str
    compliant: bool
    exempt: bool
    detail: str


class SecurityPosturePort(ABC):
    """Driven port — provides normalized per-workload compliance records.

    A secondary adapter fans out to the individual security audits (TLS, RBAC,
    Pod Security, image scanning, secret rotation) and normalizes each result
    into a WorkloadComplianceRaw record. The domain never touches the
    individual audits — only this uniform contract.
    """

    @abstractmethod
    def list_workload_compliance(self) -> list[WorkloadComplianceRaw]:
        """Return one compliance record per (workload, category).

        Raises ClusterUnreachableError on cluster/API failures.
        """

    @abstractmethod
    def get_defined_categories(self) -> list[str]:
        """Return the compliance categories that have a policy defined.

        A category absent from this list is reported as ``policy_not_defined``
        rather than silently treated as compliant.
        """

    @abstractmethod
    def is_partial(self) -> bool:
        """True when the compliance scan returned partial results (e.g. it
        timed out on a large cluster), so the report can be flagged."""
