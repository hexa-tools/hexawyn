from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.platform_reliability_port import (
    PlatformReliabilityPort,
    ReliabilityData,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ReliabilityDataSource(Protocol):
    """Assembles reliability inputs from the incident/MTTR sources and pricing
    config into the uniform ReliabilityData contract."""

    def fetch_reliability_data(self, period: str) -> ReliabilityData: ...
mutants_xǁPlatformReliabilityAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁPlatformReliabilityAdapterǁget_reliability_data__mutmut: MutantDict = {}  # type: ignore


class PlatformReliabilityAdapter(PlatformReliabilityPort):
    """Facade over the incident / MTTR / pricing sources for the CTO report.

    Delegates to an injected source that normalizes those sources into
    ReliabilityData, keeping the domain free of any knowledge of them.
    """

    @_mutmut_mutated(mutants_xǁPlatformReliabilityAdapterǁ__init____mutmut)
    def __init__(self, source: ReliabilityDataSource) -> None:
        self._source = source

    def xǁPlatformReliabilityAdapterǁ__init____mutmut_orig(self, source: ReliabilityDataSource) -> None:
        self._source = source

    def xǁPlatformReliabilityAdapterǁ__init____mutmut_1(self, source: ReliabilityDataSource) -> None:
        self._source = None

    @_mutmut_mutated(mutants_xǁPlatformReliabilityAdapterǁget_reliability_data__mutmut)
    def get_reliability_data(self, period: str) -> ReliabilityData:
        return self._source.fetch_reliability_data(period)

    def xǁPlatformReliabilityAdapterǁget_reliability_data__mutmut_orig(self, period: str) -> ReliabilityData:
        return self._source.fetch_reliability_data(period)

    def xǁPlatformReliabilityAdapterǁget_reliability_data__mutmut_1(self, period: str) -> ReliabilityData:
        return self._source.fetch_reliability_data(None)

mutants_xǁPlatformReliabilityAdapterǁ__init____mutmut['_mutmut_orig'] = PlatformReliabilityAdapter.xǁPlatformReliabilityAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityAdapterǁ__init____mutmut['xǁPlatformReliabilityAdapterǁ__init____mutmut_1'] = PlatformReliabilityAdapter.xǁPlatformReliabilityAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁPlatformReliabilityAdapterǁget_reliability_data__mutmut['_mutmut_orig'] = PlatformReliabilityAdapter.xǁPlatformReliabilityAdapterǁget_reliability_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityAdapterǁget_reliability_data__mutmut['xǁPlatformReliabilityAdapterǁget_reliability_data__mutmut_1'] = PlatformReliabilityAdapter.xǁPlatformReliabilityAdapterǁget_reliability_data__mutmut_1 # type: ignore # mutmut generated
