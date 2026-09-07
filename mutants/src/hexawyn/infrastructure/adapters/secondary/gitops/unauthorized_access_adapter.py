from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.unauthorized_access_port import (
    UnauthorizedAccessPort,
    UnauthorizedAccessRaw,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class UnauthorizedAccessSource(Protocol):
    def fetch_unauthorized_access_data(self) -> UnauthorizedAccessRaw: ...
mutants_xǁUnauthorizedAccessAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore


class UnauthorizedAccessAdapter(UnauthorizedAccessPort):
    @_mutmut_mutated(mutants_xǁUnauthorizedAccessAdapterǁ__init____mutmut)
    def __init__(self, source: UnauthorizedAccessSource) -> None:
        self._source = source
    def xǁUnauthorizedAccessAdapterǁ__init____mutmut_orig(self, source: UnauthorizedAccessSource) -> None:
        self._source = source
    def xǁUnauthorizedAccessAdapterǁ__init____mutmut_1(self, source: UnauthorizedAccessSource) -> None:
        self._source = None

    def get_unauthorized_access_data(self) -> UnauthorizedAccessRaw:
        return self._source.fetch_unauthorized_access_data()

mutants_xǁUnauthorizedAccessAdapterǁ__init____mutmut['_mutmut_orig'] = UnauthorizedAccessAdapter.xǁUnauthorizedAccessAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁUnauthorizedAccessAdapterǁ__init____mutmut['xǁUnauthorizedAccessAdapterǁ__init____mutmut_1'] = UnauthorizedAccessAdapter.xǁUnauthorizedAccessAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
