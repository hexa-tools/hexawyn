from __future__ import annotations

from hexawyn.application.ports.driven.engineer_workload_port import MonthNightData

_MONTHS_IN_QUARTER = 3


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut: MutantDict = {}  # type: ignore


class EmptyNightInterventionSource:
    @_mutmut_mutated(mutants_xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut)
    def fetch_night_intervention_data(self, history_months: int) -> list[MonthNightData]:
        return [
            MonthNightData(month="2026-06", night_intervention_count=0, total_nights=30)
            for _ in range(history_months)
        ]
    def xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_orig(self, history_months: int) -> list[MonthNightData]:
        return [
            MonthNightData(month="2026-06", night_intervention_count=0, total_nights=30)
            for _ in range(history_months)
        ]
    def xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_1(self, history_months: int) -> list[MonthNightData]:
        return [
            MonthNightData(month=None, night_intervention_count=0, total_nights=30)
            for _ in range(history_months)
        ]
    def xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_2(self, history_months: int) -> list[MonthNightData]:
        return [
            MonthNightData(month="2026-06", night_intervention_count=None, total_nights=30)
            for _ in range(history_months)
        ]
    def xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_3(self, history_months: int) -> list[MonthNightData]:
        return [
            MonthNightData(month="2026-06", night_intervention_count=0, total_nights=None)
            for _ in range(history_months)
        ]
    def xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_4(self, history_months: int) -> list[MonthNightData]:
        return [
            MonthNightData(night_intervention_count=0, total_nights=30)
            for _ in range(history_months)
        ]
    def xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_5(self, history_months: int) -> list[MonthNightData]:
        return [
            MonthNightData(month="2026-06", total_nights=30)
            for _ in range(history_months)
        ]
    def xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_6(self, history_months: int) -> list[MonthNightData]:
        return [
            MonthNightData(month="2026-06", night_intervention_count=0, )
            for _ in range(history_months)
        ]
    def xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_7(self, history_months: int) -> list[MonthNightData]:
        return [
            MonthNightData(month="XX2026-06XX", night_intervention_count=0, total_nights=30)
            for _ in range(history_months)
        ]
    def xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_8(self, history_months: int) -> list[MonthNightData]:
        return [
            MonthNightData(month="2026-06", night_intervention_count=1, total_nights=30)
            for _ in range(history_months)
        ]
    def xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_9(self, history_months: int) -> list[MonthNightData]:
        return [
            MonthNightData(month="2026-06", night_intervention_count=0, total_nights=31)
            for _ in range(history_months)
        ]
    def xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_10(self, history_months: int) -> list[MonthNightData]:
        return [
            MonthNightData(month="2026-06", night_intervention_count=0, total_nights=30)
            for _ in range(None)
        ]

mutants_xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut['_mutmut_orig'] = EmptyNightInterventionSource.xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut['xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_1'] = EmptyNightInterventionSource.xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_1 # type: ignore # mutmut generated
mutants_xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut['xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_2'] = EmptyNightInterventionSource.xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_2 # type: ignore # mutmut generated
mutants_xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut['xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_3'] = EmptyNightInterventionSource.xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_3 # type: ignore # mutmut generated
mutants_xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut['xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_4'] = EmptyNightInterventionSource.xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_4 # type: ignore # mutmut generated
mutants_xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut['xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_5'] = EmptyNightInterventionSource.xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_5 # type: ignore # mutmut generated
mutants_xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut['xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_6'] = EmptyNightInterventionSource.xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_6 # type: ignore # mutmut generated
mutants_xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut['xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_7'] = EmptyNightInterventionSource.xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_7 # type: ignore # mutmut generated
mutants_xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut['xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_8'] = EmptyNightInterventionSource.xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_8 # type: ignore # mutmut generated
mutants_xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut['xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_9'] = EmptyNightInterventionSource.xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_9 # type: ignore # mutmut generated
mutants_xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut['xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_10'] = EmptyNightInterventionSource.xǁEmptyNightInterventionSourceǁfetch_night_intervention_data__mutmut_10 # type: ignore # mutmut generated
