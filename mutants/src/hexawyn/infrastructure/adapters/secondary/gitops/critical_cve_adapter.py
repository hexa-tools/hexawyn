from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.critical_cve_port import CriticalCvePort, CveRaw


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CriticalCveSource(Protocol):
    def fetch_critical_cves(self) -> list[CveRaw]: ...
mutants_xǁCriticalCveAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore


class CriticalCveAdapter(CriticalCvePort):
    @_mutmut_mutated(mutants_xǁCriticalCveAdapterǁ__init____mutmut)
    def __init__(self, source: CriticalCveSource) -> None:
        self._source = source
    def xǁCriticalCveAdapterǁ__init____mutmut_orig(self, source: CriticalCveSource) -> None:
        self._source = source
    def xǁCriticalCveAdapterǁ__init____mutmut_1(self, source: CriticalCveSource) -> None:
        self._source = None

    def get_critical_cves(self) -> list[CveRaw]:
        return self._source.fetch_critical_cves()

mutants_xǁCriticalCveAdapterǁ__init____mutmut['_mutmut_orig'] = CriticalCveAdapter.xǁCriticalCveAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCriticalCveAdapterǁ__init____mutmut['xǁCriticalCveAdapterǁ__init____mutmut_1'] = CriticalCveAdapter.xǁCriticalCveAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
