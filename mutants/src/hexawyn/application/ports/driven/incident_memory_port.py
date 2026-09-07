from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.domain.models.incident_memory import IncidentMemoryRecord


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class IncidentMemoryPort(ABC):
    @abstractmethod
    def store_incident(self, record: IncidentMemoryRecord) -> None:
        """Persist a completed investigation for later similarity retrieval.

        Best-effort: implementations must not raise on storage failure — the
        caller treats this as non-blocking persistence. Records that are not
        storable (missing embedding, cluster, or tool name) are skipped.
        """
