from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.engineer_workload_port import (
    EngineerWorkloadPort,
    MonthNightData,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class NightInterventionSource(Protocol):
    def fetch_night_intervention_data(self, history_months: int) -> list[MonthNightData]: ...
mutants_xǁNightInterventionAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁNightInterventionAdapterǁget_night_intervention_data__mutmut: MutantDict = {}  # type: ignore


class NightInterventionAdapter(EngineerWorkloadPort):
    @_mutmut_mutated(mutants_xǁNightInterventionAdapterǁ__init____mutmut)
    def __init__(self, source: NightInterventionSource) -> None:
        self._source = source
    def xǁNightInterventionAdapterǁ__init____mutmut_orig(self, source: NightInterventionSource) -> None:
        self._source = source
    def xǁNightInterventionAdapterǁ__init____mutmut_1(self, source: NightInterventionSource) -> None:
        self._source = None

    @_mutmut_mutated(mutants_xǁNightInterventionAdapterǁget_night_intervention_data__mutmut)
    def get_night_intervention_data(self, history_months: int) -> list[MonthNightData]:
        return self._source.fetch_night_intervention_data(history_months)

    def xǁNightInterventionAdapterǁget_night_intervention_data__mutmut_orig(self, history_months: int) -> list[MonthNightData]:
        return self._source.fetch_night_intervention_data(history_months)

    def xǁNightInterventionAdapterǁget_night_intervention_data__mutmut_1(self, history_months: int) -> list[MonthNightData]:
        return self._source.fetch_night_intervention_data(None)

mutants_xǁNightInterventionAdapterǁ__init____mutmut['_mutmut_orig'] = NightInterventionAdapter.xǁNightInterventionAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁNightInterventionAdapterǁ__init____mutmut['xǁNightInterventionAdapterǁ__init____mutmut_1'] = NightInterventionAdapter.xǁNightInterventionAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁNightInterventionAdapterǁget_night_intervention_data__mutmut['_mutmut_orig'] = NightInterventionAdapter.xǁNightInterventionAdapterǁget_night_intervention_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁNightInterventionAdapterǁget_night_intervention_data__mutmut['xǁNightInterventionAdapterǁget_night_intervention_data__mutmut_1'] = NightInterventionAdapter.xǁNightInterventionAdapterǁget_night_intervention_data__mutmut_1 # type: ignore # mutmut generated
