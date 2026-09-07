from __future__ import annotations

from hexawyn.application.ports.driven.critical_cve_port import CveRaw


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class EmptyCriticalCveSource:
    def fetch_critical_cves(self) -> list[CveRaw]:
        return []
