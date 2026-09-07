from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.disruption_risk_port import (
    DisruptionRiskPort,
    RiskEventRaw,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class DisruptionRiskSource(Protocol):
    def fetch_disruption_risks(self, warning_days: int) -> list[RiskEventRaw]: ...
mutants_xǁDisruptionRiskAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDisruptionRiskAdapterǁget_disruption_risks__mutmut: MutantDict = {}  # type: ignore


class DisruptionRiskAdapter(DisruptionRiskPort):
    @_mutmut_mutated(mutants_xǁDisruptionRiskAdapterǁ__init____mutmut)
    def __init__(self, source: DisruptionRiskSource) -> None:
        self._source = source
    def xǁDisruptionRiskAdapterǁ__init____mutmut_orig(self, source: DisruptionRiskSource) -> None:
        self._source = source
    def xǁDisruptionRiskAdapterǁ__init____mutmut_1(self, source: DisruptionRiskSource) -> None:
        self._source = None

    @_mutmut_mutated(mutants_xǁDisruptionRiskAdapterǁget_disruption_risks__mutmut)
    def get_disruption_risks(self, warning_days: int) -> list[RiskEventRaw]:
        return self._source.fetch_disruption_risks(warning_days)

    def xǁDisruptionRiskAdapterǁget_disruption_risks__mutmut_orig(self, warning_days: int) -> list[RiskEventRaw]:
        return self._source.fetch_disruption_risks(warning_days)

    def xǁDisruptionRiskAdapterǁget_disruption_risks__mutmut_1(self, warning_days: int) -> list[RiskEventRaw]:
        return self._source.fetch_disruption_risks(None)

mutants_xǁDisruptionRiskAdapterǁ__init____mutmut['_mutmut_orig'] = DisruptionRiskAdapter.xǁDisruptionRiskAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDisruptionRiskAdapterǁ__init____mutmut['xǁDisruptionRiskAdapterǁ__init____mutmut_1'] = DisruptionRiskAdapter.xǁDisruptionRiskAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁDisruptionRiskAdapterǁget_disruption_risks__mutmut['_mutmut_orig'] = DisruptionRiskAdapter.xǁDisruptionRiskAdapterǁget_disruption_risks__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDisruptionRiskAdapterǁget_disruption_risks__mutmut['xǁDisruptionRiskAdapterǁget_disruption_risks__mutmut_1'] = DisruptionRiskAdapter.xǁDisruptionRiskAdapterǁget_disruption_risks__mutmut_1 # type: ignore # mutmut generated
