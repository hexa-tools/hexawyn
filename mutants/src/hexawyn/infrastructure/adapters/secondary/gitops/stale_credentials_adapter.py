from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.stale_credentials_port import (
    StaleCredentialRaw,
    StaleCredentialsPort,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class StaleCredentialsSource(Protocol):
    def fetch_stale_credentials(self, min_days: int) -> list[StaleCredentialRaw]: ...
mutants_xǁStaleCredentialsAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁStaleCredentialsAdapterǁget_stale_credentials__mutmut: MutantDict = {}  # type: ignore


class StaleCredentialsAdapter(StaleCredentialsPort):
    @_mutmut_mutated(mutants_xǁStaleCredentialsAdapterǁ__init____mutmut)
    def __init__(self, source: StaleCredentialsSource) -> None:
        self._source = source
    def xǁStaleCredentialsAdapterǁ__init____mutmut_orig(self, source: StaleCredentialsSource) -> None:
        self._source = source
    def xǁStaleCredentialsAdapterǁ__init____mutmut_1(self, source: StaleCredentialsSource) -> None:
        self._source = None

    @_mutmut_mutated(mutants_xǁStaleCredentialsAdapterǁget_stale_credentials__mutmut)
    def get_stale_credentials(self, min_days: int) -> list[StaleCredentialRaw]:
        return self._source.fetch_stale_credentials(min_days)

    def xǁStaleCredentialsAdapterǁget_stale_credentials__mutmut_orig(self, min_days: int) -> list[StaleCredentialRaw]:
        return self._source.fetch_stale_credentials(min_days)

    def xǁStaleCredentialsAdapterǁget_stale_credentials__mutmut_1(self, min_days: int) -> list[StaleCredentialRaw]:
        return self._source.fetch_stale_credentials(None)

mutants_xǁStaleCredentialsAdapterǁ__init____mutmut['_mutmut_orig'] = StaleCredentialsAdapter.xǁStaleCredentialsAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁStaleCredentialsAdapterǁ__init____mutmut['xǁStaleCredentialsAdapterǁ__init____mutmut_1'] = StaleCredentialsAdapter.xǁStaleCredentialsAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁStaleCredentialsAdapterǁget_stale_credentials__mutmut['_mutmut_orig'] = StaleCredentialsAdapter.xǁStaleCredentialsAdapterǁget_stale_credentials__mutmut_orig # type: ignore # mutmut generated
mutants_xǁStaleCredentialsAdapterǁget_stale_credentials__mutmut['xǁStaleCredentialsAdapterǁget_stale_credentials__mutmut_1'] = StaleCredentialsAdapter.xǁStaleCredentialsAdapterǁget_stale_credentials__mutmut_1 # type: ignore # mutmut generated
