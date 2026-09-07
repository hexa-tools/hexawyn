from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.sla_report_port import QuarterSlaData, SlaReportPort


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class QuarterSlaSource(Protocol):
    """Assembles quarter-level SLA data from the weekly reliability / SLO
    sources into the uniform QuarterSlaData contract."""

    def fetch_quarter_sla_data(self, quarter: str) -> QuarterSlaData: ...

    def fetch_previous_quarter_avg_uptime(self, quarter: str) -> float | None: ...
mutants_xǁSlaReportAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁSlaReportAdapterǁget_quarter_sla_data__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSlaReportAdapterǁget_previous_quarter_avg_uptime__mutmut: MutantDict = {}  # type: ignore


class SlaReportAdapter(SlaReportPort):
    """Facade over the reliability/SLO sources for quarterly SLA reporting.

    Delegates to an injected source that rolls up weekly reliability data into
    quarter-level records, keeping the domain free of those sources.
    """

    @_mutmut_mutated(mutants_xǁSlaReportAdapterǁ__init____mutmut)
    def __init__(self, source: QuarterSlaSource) -> None:
        self._source = source

    def xǁSlaReportAdapterǁ__init____mutmut_orig(self, source: QuarterSlaSource) -> None:
        self._source = source

    def xǁSlaReportAdapterǁ__init____mutmut_1(self, source: QuarterSlaSource) -> None:
        self._source = None

    @_mutmut_mutated(mutants_xǁSlaReportAdapterǁget_quarter_sla_data__mutmut)
    def get_quarter_sla_data(self, quarter: str) -> QuarterSlaData:
        return self._source.fetch_quarter_sla_data(quarter)

    def xǁSlaReportAdapterǁget_quarter_sla_data__mutmut_orig(self, quarter: str) -> QuarterSlaData:
        return self._source.fetch_quarter_sla_data(quarter)

    def xǁSlaReportAdapterǁget_quarter_sla_data__mutmut_1(self, quarter: str) -> QuarterSlaData:
        return self._source.fetch_quarter_sla_data(None)

    @_mutmut_mutated(mutants_xǁSlaReportAdapterǁget_previous_quarter_avg_uptime__mutmut)
    def get_previous_quarter_avg_uptime(self, quarter: str) -> float | None:
        return self._source.fetch_previous_quarter_avg_uptime(quarter)

    def xǁSlaReportAdapterǁget_previous_quarter_avg_uptime__mutmut_orig(self, quarter: str) -> float | None:
        return self._source.fetch_previous_quarter_avg_uptime(quarter)

    def xǁSlaReportAdapterǁget_previous_quarter_avg_uptime__mutmut_1(self, quarter: str) -> float | None:
        return self._source.fetch_previous_quarter_avg_uptime(None)

mutants_xǁSlaReportAdapterǁ__init____mutmut['_mutmut_orig'] = SlaReportAdapter.xǁSlaReportAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁSlaReportAdapterǁ__init____mutmut['xǁSlaReportAdapterǁ__init____mutmut_1'] = SlaReportAdapter.xǁSlaReportAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁSlaReportAdapterǁget_quarter_sla_data__mutmut['_mutmut_orig'] = SlaReportAdapter.xǁSlaReportAdapterǁget_quarter_sla_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSlaReportAdapterǁget_quarter_sla_data__mutmut['xǁSlaReportAdapterǁget_quarter_sla_data__mutmut_1'] = SlaReportAdapter.xǁSlaReportAdapterǁget_quarter_sla_data__mutmut_1 # type: ignore # mutmut generated

mutants_xǁSlaReportAdapterǁget_previous_quarter_avg_uptime__mutmut['_mutmut_orig'] = SlaReportAdapter.xǁSlaReportAdapterǁget_previous_quarter_avg_uptime__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSlaReportAdapterǁget_previous_quarter_avg_uptime__mutmut['xǁSlaReportAdapterǁget_previous_quarter_avg_uptime__mutmut_1'] = SlaReportAdapter.xǁSlaReportAdapterǁget_previous_quarter_avg_uptime__mutmut_1 # type: ignore # mutmut generated
