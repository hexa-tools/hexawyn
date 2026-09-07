from __future__ import annotations

from hexawyn.application.ports.driven.platform_reliability_port import ReliabilityData

_MINUTES_IN_THIRTY_DAYS = 43200


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut: MutantDict = {}  # type: ignore


class EmptyReliabilityDataSource:
    """Default reliability source used until the incident/MTTR roll-up is wired
    in. Reports a healthy 30-day period with no incidents and no pricing, so
    the report reads "Plateforme stable" rather than fabricating figures."""

    @_mutmut_mutated(mutants_xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut)
    def fetch_reliability_data(self, period: str) -> ReliabilityData:
        return ReliabilityData(
            period_minutes=_MINUTES_IN_THIRTY_DAYS,
            incidents=[],
            previous_avg_resolution_minutes=None,
            cost_per_downtime_minute_eur=None,
        )

    def xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut_orig(self, period: str) -> ReliabilityData:
        return ReliabilityData(
            period_minutes=_MINUTES_IN_THIRTY_DAYS,
            incidents=[],
            previous_avg_resolution_minutes=None,
            cost_per_downtime_minute_eur=None,
        )

    def xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut_1(self, period: str) -> ReliabilityData:
        return ReliabilityData(
            period_minutes=None,
            incidents=[],
            previous_avg_resolution_minutes=None,
            cost_per_downtime_minute_eur=None,
        )

    def xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut_2(self, period: str) -> ReliabilityData:
        return ReliabilityData(
            period_minutes=_MINUTES_IN_THIRTY_DAYS,
            incidents=None,
            previous_avg_resolution_minutes=None,
            cost_per_downtime_minute_eur=None,
        )

    def xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut_3(self, period: str) -> ReliabilityData:
        return ReliabilityData(
            incidents=[],
            previous_avg_resolution_minutes=None,
            cost_per_downtime_minute_eur=None,
        )

    def xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut_4(self, period: str) -> ReliabilityData:
        return ReliabilityData(
            period_minutes=_MINUTES_IN_THIRTY_DAYS,
            previous_avg_resolution_minutes=None,
            cost_per_downtime_minute_eur=None,
        )

    def xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut_5(self, period: str) -> ReliabilityData:
        return ReliabilityData(
            period_minutes=_MINUTES_IN_THIRTY_DAYS,
            incidents=[],
            cost_per_downtime_minute_eur=None,
        )

    def xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut_6(self, period: str) -> ReliabilityData:
        return ReliabilityData(
            period_minutes=_MINUTES_IN_THIRTY_DAYS,
            incidents=[],
            previous_avg_resolution_minutes=None,
            )

mutants_xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut['_mutmut_orig'] = EmptyReliabilityDataSource.xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut['xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut_1'] = EmptyReliabilityDataSource.xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut_1 # type: ignore # mutmut generated
mutants_xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut['xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut_2'] = EmptyReliabilityDataSource.xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut_2 # type: ignore # mutmut generated
mutants_xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut['xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut_3'] = EmptyReliabilityDataSource.xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut_3 # type: ignore # mutmut generated
mutants_xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut['xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut_4'] = EmptyReliabilityDataSource.xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut_4 # type: ignore # mutmut generated
mutants_xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut['xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut_5'] = EmptyReliabilityDataSource.xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut_5 # type: ignore # mutmut generated
mutants_xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut['xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut_6'] = EmptyReliabilityDataSource.xǁEmptyReliabilityDataSourceǁfetch_reliability_data__mutmut_6 # type: ignore # mutmut generated
