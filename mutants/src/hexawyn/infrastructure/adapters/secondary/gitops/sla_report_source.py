from __future__ import annotations

from hexawyn.application.ports.driven.sla_report_port import QuarterSlaData


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut: MutantDict = {}  # type: ignore


class EmptyQuarterSlaSource:
    """Default quarterly SLA source used until a persistent reliability roll-up
    is wired in. Reports no data, so the domain warns about missing data rather
    than presenting a misleading 100% uptime."""

    @_mutmut_mutated(mutants_xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut)
    def fetch_quarter_sla_data(self, quarter: str) -> QuarterSlaData:
        return QuarterSlaData(has_data=False, services=[], breaches=[])

    def xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut_orig(self, quarter: str) -> QuarterSlaData:
        return QuarterSlaData(has_data=False, services=[], breaches=[])

    def xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut_1(self, quarter: str) -> QuarterSlaData:
        return QuarterSlaData(has_data=None, services=[], breaches=[])

    def xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut_2(self, quarter: str) -> QuarterSlaData:
        return QuarterSlaData(has_data=False, services=None, breaches=[])

    def xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut_3(self, quarter: str) -> QuarterSlaData:
        return QuarterSlaData(has_data=False, services=[], breaches=None)

    def xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut_4(self, quarter: str) -> QuarterSlaData:
        return QuarterSlaData(services=[], breaches=[])

    def xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut_5(self, quarter: str) -> QuarterSlaData:
        return QuarterSlaData(has_data=False, breaches=[])

    def xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut_6(self, quarter: str) -> QuarterSlaData:
        return QuarterSlaData(has_data=False, services=[], )

    def xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut_7(self, quarter: str) -> QuarterSlaData:
        return QuarterSlaData(has_data=True, services=[], breaches=[])

    def fetch_previous_quarter_avg_uptime(self, quarter: str) -> float | None:
        return None

mutants_xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut['_mutmut_orig'] = EmptyQuarterSlaSource.xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut['xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut_1'] = EmptyQuarterSlaSource.xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut_1 # type: ignore # mutmut generated
mutants_xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut['xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut_2'] = EmptyQuarterSlaSource.xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut_2 # type: ignore # mutmut generated
mutants_xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut['xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut_3'] = EmptyQuarterSlaSource.xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut_3 # type: ignore # mutmut generated
mutants_xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut['xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut_4'] = EmptyQuarterSlaSource.xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut_4 # type: ignore # mutmut generated
mutants_xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut['xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut_5'] = EmptyQuarterSlaSource.xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut_5 # type: ignore # mutmut generated
mutants_xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut['xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut_6'] = EmptyQuarterSlaSource.xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut_6 # type: ignore # mutmut generated
mutants_xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut['xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut_7'] = EmptyQuarterSlaSource.xǁEmptyQuarterSlaSourceǁfetch_quarter_sla_data__mutmut_7 # type: ignore # mutmut generated
