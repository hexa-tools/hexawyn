"""Domain service: pure waste ratio computation, ranking, and exclusion logic."""

from __future__ import annotations

from hexawyn.domain.models.namespace_waste import (
    ExcludedNamespace,
    NamespaceRawData,
    NamespaceWaste,
    OverProvisioningReport,
)

_OVER_PROVISION_THRESHOLD_PCT = 50.0
_MIN_AGE_HOURS = 24.0
_REASON_NO_REQUESTS = "No resource requests set — burstable or BestEffort pods excluded"
_REASON_TOO_RECENT = "Namespace age < 24h — insufficient data for 7-day waste analysis"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut: MutantDict = {}  # type: ignore


class NamespaceOverProvisioningService:
    """Computes waste ratios and produces a ranked over-provisioning report.

    Pure domain logic — no infra dependencies, no try/catch.
    """

    @_mutmut_mutated(mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut)
    def analyze(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(wastes, key=lambda w: w.max_waste_pct, reverse=True)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_orig(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(wastes, key=lambda w: w.max_waste_pct, reverse=True)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_1(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = None
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(wastes, key=lambda w: w.max_waste_pct, reverse=True)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_2(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(None)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(wastes, key=lambda w: w.max_waste_pct, reverse=True)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_3(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = None
        ranked = sorted(wastes, key=lambda w: w.max_waste_pct, reverse=True)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_4(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(None) for item in eligible]
        ranked = sorted(wastes, key=lambda w: w.max_waste_pct, reverse=True)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_5(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = None
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_6(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(None, key=lambda w: w.max_waste_pct, reverse=True)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_7(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(wastes, key=None, reverse=True)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_8(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(wastes, key=lambda w: w.max_waste_pct, reverse=None)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_9(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(key=lambda w: w.max_waste_pct, reverse=True)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_10(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(wastes, reverse=True)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_11(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(wastes, key=lambda w: w.max_waste_pct, )[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_12(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(wastes, key=lambda w: None, reverse=True)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_13(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(wastes, key=lambda w: w.max_waste_pct, reverse=False)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_14(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(wastes, key=lambda w: w.max_waste_pct, reverse=True)[:top_n]
        return OverProvisioningReport(
            namespaces=None,
            excluded=excluded,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_15(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(wastes, key=lambda w: w.max_waste_pct, reverse=True)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=None,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_16(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(wastes, key=lambda w: w.max_waste_pct, reverse=True)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_cpu_cores=None,
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_17(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(wastes, key=lambda w: w.max_waste_pct, reverse=True)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=None,
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_18(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(wastes, key=lambda w: w.max_waste_pct, reverse=True)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=None,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_19(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(wastes, key=lambda w: w.max_waste_pct, reverse=True)[:top_n]
        return OverProvisioningReport(
            excluded=excluded,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_20(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(wastes, key=lambda w: w.max_waste_pct, reverse=True)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_21(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(wastes, key=lambda w: w.max_waste_pct, reverse=True)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_22(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(wastes, key=lambda w: w.max_waste_pct, reverse=True)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_23(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(wastes, key=lambda w: w.max_waste_pct, reverse=True)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_24(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(wastes, key=lambda w: w.max_waste_pct, reverse=True)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_cpu_cores=sum(None),
            total_wasted_memory_gb=sum(w.memory_wasted_gb for w in ranked),
            analysis_window_days=analysis_window_days,
        )

    def xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_25(
        self,
        raw_data: list[NamespaceRawData],
        top_n: int,
        analysis_window_days: int,
    ) -> OverProvisioningReport:
        eligible, excluded = _partition(raw_data)
        wastes = [_compute_namespace_waste(item) for item in eligible]
        ranked = sorted(wastes, key=lambda w: w.max_waste_pct, reverse=True)[:top_n]
        return OverProvisioningReport(
            namespaces=ranked,
            excluded=excluded,
            total_wasted_cpu_cores=sum(w.cpu_wasted_cores for w in ranked),
            total_wasted_memory_gb=sum(None),
            analysis_window_days=analysis_window_days,
        )

mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['_mutmut_orig'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_orig # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_1'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_1 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_2'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_2 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_3'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_3 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_4'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_4 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_5'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_5 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_6'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_6 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_7'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_7 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_8'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_8 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_9'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_9 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_10'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_10 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_11'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_11 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_12'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_12 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_13'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_13 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_14'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_14 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_15'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_15 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_16'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_16 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_17'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_17 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_18'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_18 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_19'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_19 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_20'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_20 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_21'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_21 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_22'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_22 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_23'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_23 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_24'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_24 # type: ignore # mutmut generated
mutants_xǁNamespaceOverProvisioningServiceǁanalyze__mutmut['xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_25'] = NamespaceOverProvisioningService.xǁNamespaceOverProvisioningServiceǁanalyze__mutmut_25 # type: ignore # mutmut generated
mutants_x__partition__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__partition__mutmut)
def _partition(
    raw_data: list[NamespaceRawData],
) -> tuple[list[NamespaceRawData], list[ExcludedNamespace]]:
    eligible: list[NamespaceRawData] = []
    excluded: list[ExcludedNamespace] = []
    for item in raw_data:
        reason = _exclusion_reason(item)
        if reason:
            excluded.append(ExcludedNamespace(namespace=item["namespace"], reason=reason))
        else:
            eligible.append(item)
    return eligible, excluded


def x__partition__mutmut_orig(
    raw_data: list[NamespaceRawData],
) -> tuple[list[NamespaceRawData], list[ExcludedNamespace]]:
    eligible: list[NamespaceRawData] = []
    excluded: list[ExcludedNamespace] = []
    for item in raw_data:
        reason = _exclusion_reason(item)
        if reason:
            excluded.append(ExcludedNamespace(namespace=item["namespace"], reason=reason))
        else:
            eligible.append(item)
    return eligible, excluded


def x__partition__mutmut_1(
    raw_data: list[NamespaceRawData],
) -> tuple[list[NamespaceRawData], list[ExcludedNamespace]]:
    eligible: list[NamespaceRawData] = None
    excluded: list[ExcludedNamespace] = []
    for item in raw_data:
        reason = _exclusion_reason(item)
        if reason:
            excluded.append(ExcludedNamespace(namespace=item["namespace"], reason=reason))
        else:
            eligible.append(item)
    return eligible, excluded


def x__partition__mutmut_2(
    raw_data: list[NamespaceRawData],
) -> tuple[list[NamespaceRawData], list[ExcludedNamespace]]:
    eligible: list[NamespaceRawData] = []
    excluded: list[ExcludedNamespace] = None
    for item in raw_data:
        reason = _exclusion_reason(item)
        if reason:
            excluded.append(ExcludedNamespace(namespace=item["namespace"], reason=reason))
        else:
            eligible.append(item)
    return eligible, excluded


def x__partition__mutmut_3(
    raw_data: list[NamespaceRawData],
) -> tuple[list[NamespaceRawData], list[ExcludedNamespace]]:
    eligible: list[NamespaceRawData] = []
    excluded: list[ExcludedNamespace] = []
    for item in raw_data:
        reason = None
        if reason:
            excluded.append(ExcludedNamespace(namespace=item["namespace"], reason=reason))
        else:
            eligible.append(item)
    return eligible, excluded


def x__partition__mutmut_4(
    raw_data: list[NamespaceRawData],
) -> tuple[list[NamespaceRawData], list[ExcludedNamespace]]:
    eligible: list[NamespaceRawData] = []
    excluded: list[ExcludedNamespace] = []
    for item in raw_data:
        reason = _exclusion_reason(None)
        if reason:
            excluded.append(ExcludedNamespace(namespace=item["namespace"], reason=reason))
        else:
            eligible.append(item)
    return eligible, excluded


def x__partition__mutmut_5(
    raw_data: list[NamespaceRawData],
) -> tuple[list[NamespaceRawData], list[ExcludedNamespace]]:
    eligible: list[NamespaceRawData] = []
    excluded: list[ExcludedNamespace] = []
    for item in raw_data:
        reason = _exclusion_reason(item)
        if reason:
            excluded.append(None)
        else:
            eligible.append(item)
    return eligible, excluded


def x__partition__mutmut_6(
    raw_data: list[NamespaceRawData],
) -> tuple[list[NamespaceRawData], list[ExcludedNamespace]]:
    eligible: list[NamespaceRawData] = []
    excluded: list[ExcludedNamespace] = []
    for item in raw_data:
        reason = _exclusion_reason(item)
        if reason:
            excluded.append(ExcludedNamespace(namespace=None, reason=reason))
        else:
            eligible.append(item)
    return eligible, excluded


def x__partition__mutmut_7(
    raw_data: list[NamespaceRawData],
) -> tuple[list[NamespaceRawData], list[ExcludedNamespace]]:
    eligible: list[NamespaceRawData] = []
    excluded: list[ExcludedNamespace] = []
    for item in raw_data:
        reason = _exclusion_reason(item)
        if reason:
            excluded.append(ExcludedNamespace(namespace=item["namespace"], reason=None))
        else:
            eligible.append(item)
    return eligible, excluded


def x__partition__mutmut_8(
    raw_data: list[NamespaceRawData],
) -> tuple[list[NamespaceRawData], list[ExcludedNamespace]]:
    eligible: list[NamespaceRawData] = []
    excluded: list[ExcludedNamespace] = []
    for item in raw_data:
        reason = _exclusion_reason(item)
        if reason:
            excluded.append(ExcludedNamespace(reason=reason))
        else:
            eligible.append(item)
    return eligible, excluded


def x__partition__mutmut_9(
    raw_data: list[NamespaceRawData],
) -> tuple[list[NamespaceRawData], list[ExcludedNamespace]]:
    eligible: list[NamespaceRawData] = []
    excluded: list[ExcludedNamespace] = []
    for item in raw_data:
        reason = _exclusion_reason(item)
        if reason:
            excluded.append(ExcludedNamespace(namespace=item["namespace"], ))
        else:
            eligible.append(item)
    return eligible, excluded


def x__partition__mutmut_10(
    raw_data: list[NamespaceRawData],
) -> tuple[list[NamespaceRawData], list[ExcludedNamespace]]:
    eligible: list[NamespaceRawData] = []
    excluded: list[ExcludedNamespace] = []
    for item in raw_data:
        reason = _exclusion_reason(item)
        if reason:
            excluded.append(ExcludedNamespace(namespace=item["XXnamespaceXX"], reason=reason))
        else:
            eligible.append(item)
    return eligible, excluded


def x__partition__mutmut_11(
    raw_data: list[NamespaceRawData],
) -> tuple[list[NamespaceRawData], list[ExcludedNamespace]]:
    eligible: list[NamespaceRawData] = []
    excluded: list[ExcludedNamespace] = []
    for item in raw_data:
        reason = _exclusion_reason(item)
        if reason:
            excluded.append(ExcludedNamespace(namespace=item["NAMESPACE"], reason=reason))
        else:
            eligible.append(item)
    return eligible, excluded


def x__partition__mutmut_12(
    raw_data: list[NamespaceRawData],
) -> tuple[list[NamespaceRawData], list[ExcludedNamespace]]:
    eligible: list[NamespaceRawData] = []
    excluded: list[ExcludedNamespace] = []
    for item in raw_data:
        reason = _exclusion_reason(item)
        if reason:
            excluded.append(ExcludedNamespace(namespace=item["namespace"], reason=reason))
        else:
            eligible.append(None)
    return eligible, excluded

mutants_x__partition__mutmut['_mutmut_orig'] = x__partition__mutmut_orig # type: ignore # mutmut generated
mutants_x__partition__mutmut['x__partition__mutmut_1'] = x__partition__mutmut_1 # type: ignore # mutmut generated
mutants_x__partition__mutmut['x__partition__mutmut_2'] = x__partition__mutmut_2 # type: ignore # mutmut generated
mutants_x__partition__mutmut['x__partition__mutmut_3'] = x__partition__mutmut_3 # type: ignore # mutmut generated
mutants_x__partition__mutmut['x__partition__mutmut_4'] = x__partition__mutmut_4 # type: ignore # mutmut generated
mutants_x__partition__mutmut['x__partition__mutmut_5'] = x__partition__mutmut_5 # type: ignore # mutmut generated
mutants_x__partition__mutmut['x__partition__mutmut_6'] = x__partition__mutmut_6 # type: ignore # mutmut generated
mutants_x__partition__mutmut['x__partition__mutmut_7'] = x__partition__mutmut_7 # type: ignore # mutmut generated
mutants_x__partition__mutmut['x__partition__mutmut_8'] = x__partition__mutmut_8 # type: ignore # mutmut generated
mutants_x__partition__mutmut['x__partition__mutmut_9'] = x__partition__mutmut_9 # type: ignore # mutmut generated
mutants_x__partition__mutmut['x__partition__mutmut_10'] = x__partition__mutmut_10 # type: ignore # mutmut generated
mutants_x__partition__mutmut['x__partition__mutmut_11'] = x__partition__mutmut_11 # type: ignore # mutmut generated
mutants_x__partition__mutmut['x__partition__mutmut_12'] = x__partition__mutmut_12 # type: ignore # mutmut generated
mutants_x__exclusion_reason__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__exclusion_reason__mutmut)
def _exclusion_reason(item: NamespaceRawData) -> str | None:
    if not item["has_resource_requests"]:
        return _REASON_NO_REQUESTS
    if item["age_hours"] < _MIN_AGE_HOURS:
        return _REASON_TOO_RECENT
    return None


def x__exclusion_reason__mutmut_orig(item: NamespaceRawData) -> str | None:
    if not item["has_resource_requests"]:
        return _REASON_NO_REQUESTS
    if item["age_hours"] < _MIN_AGE_HOURS:
        return _REASON_TOO_RECENT
    return None


def x__exclusion_reason__mutmut_1(item: NamespaceRawData) -> str | None:
    if item["has_resource_requests"]:
        return _REASON_NO_REQUESTS
    if item["age_hours"] < _MIN_AGE_HOURS:
        return _REASON_TOO_RECENT
    return None


def x__exclusion_reason__mutmut_2(item: NamespaceRawData) -> str | None:
    if not item["XXhas_resource_requestsXX"]:
        return _REASON_NO_REQUESTS
    if item["age_hours"] < _MIN_AGE_HOURS:
        return _REASON_TOO_RECENT
    return None


def x__exclusion_reason__mutmut_3(item: NamespaceRawData) -> str | None:
    if not item["HAS_RESOURCE_REQUESTS"]:
        return _REASON_NO_REQUESTS
    if item["age_hours"] < _MIN_AGE_HOURS:
        return _REASON_TOO_RECENT
    return None


def x__exclusion_reason__mutmut_4(item: NamespaceRawData) -> str | None:
    if not item["has_resource_requests"]:
        return _REASON_NO_REQUESTS
    if item["XXage_hoursXX"] < _MIN_AGE_HOURS:
        return _REASON_TOO_RECENT
    return None


def x__exclusion_reason__mutmut_5(item: NamespaceRawData) -> str | None:
    if not item["has_resource_requests"]:
        return _REASON_NO_REQUESTS
    if item["AGE_HOURS"] < _MIN_AGE_HOURS:
        return _REASON_TOO_RECENT
    return None


def x__exclusion_reason__mutmut_6(item: NamespaceRawData) -> str | None:
    if not item["has_resource_requests"]:
        return _REASON_NO_REQUESTS
    if item["age_hours"] <= _MIN_AGE_HOURS:
        return _REASON_TOO_RECENT
    return None

mutants_x__exclusion_reason__mutmut['_mutmut_orig'] = x__exclusion_reason__mutmut_orig # type: ignore # mutmut generated
mutants_x__exclusion_reason__mutmut['x__exclusion_reason__mutmut_1'] = x__exclusion_reason__mutmut_1 # type: ignore # mutmut generated
mutants_x__exclusion_reason__mutmut['x__exclusion_reason__mutmut_2'] = x__exclusion_reason__mutmut_2 # type: ignore # mutmut generated
mutants_x__exclusion_reason__mutmut['x__exclusion_reason__mutmut_3'] = x__exclusion_reason__mutmut_3 # type: ignore # mutmut generated
mutants_x__exclusion_reason__mutmut['x__exclusion_reason__mutmut_4'] = x__exclusion_reason__mutmut_4 # type: ignore # mutmut generated
mutants_x__exclusion_reason__mutmut['x__exclusion_reason__mutmut_5'] = x__exclusion_reason__mutmut_5 # type: ignore # mutmut generated
mutants_x__exclusion_reason__mutmut['x__exclusion_reason__mutmut_6'] = x__exclusion_reason__mutmut_6 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__compute_namespace_waste__mutmut)
def _compute_namespace_waste(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_orig(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_1(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = None
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_2(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] and 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_3(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["XXcpu_requested_coresXX"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_4(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["CPU_REQUESTED_CORES"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_5(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 1.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_6(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = None
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_7(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] and 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_8(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["XXmemory_requested_gbXX"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_9(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["MEMORY_REQUESTED_GB"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_10(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 1.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_11(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_12(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["XXcpu_actual_avg_coresXX"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_13(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["CPU_ACTUAL_AVG_CORES"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_14(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["XXcpu_actual_avg_coresXX"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_15(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["CPU_ACTUAL_AVG_CORES"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_16(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_17(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_18(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["XXmemory_actual_avg_gbXX"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_19(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["MEMORY_ACTUAL_AVG_GB"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_20(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["XXmemory_actual_avg_gbXX"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_21(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["MEMORY_ACTUAL_AVG_GB"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_22(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_23(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = None
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_24(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(None, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_25(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, None)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_26(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_27(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, )
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_28(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = None

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_29(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(None, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_30(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, None)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_31(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_32(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, )

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_33(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=None,
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_34(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=None,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_35(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=None,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_36(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=None,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_37(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=None,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_38(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=None,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_39(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=None,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_40(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=None,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_41(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=None,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_42(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=None,
    )


def x__compute_namespace_waste__mutmut_43(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_44(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_45(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_46(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_47(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_48(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_49(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_50(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_51(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_52(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        )


def x__compute_namespace_waste__mutmut_53(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["XXnamespaceXX"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_54(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["NAMESPACE"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_55(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_56(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 1.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_57(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_58(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 1.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_59(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(None, mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_60(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, None) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_61(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(mem_waste_pct) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_62(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, ) > _OVER_PROVISION_THRESHOLD_PCT,
    )


def x__compute_namespace_waste__mutmut_63(item: NamespaceRawData) -> NamespaceWaste:
    cpu_req = item["cpu_requested_cores"] or 0.0
    mem_req = item["memory_requested_gb"] or 0.0
    cpu_actual = item["cpu_actual_avg_cores"] if item["cpu_actual_avg_cores"] is not None else None
    mem_actual = item["memory_actual_avg_gb"] if item["memory_actual_avg_gb"] is not None else None

    cpu_waste_pct, cpu_wasted = _waste_pair(cpu_req, cpu_actual)
    mem_waste_pct, mem_wasted = _waste_pair(mem_req, mem_actual)

    return NamespaceWaste(
        namespace=item["namespace"],
        cpu_requested_cores=cpu_req,
        cpu_actual_avg_cores=cpu_actual if cpu_actual is not None else 0.0,
        cpu_waste_pct=cpu_waste_pct,
        cpu_wasted_cores=cpu_wasted,
        memory_requested_gb=mem_req,
        memory_actual_avg_gb=mem_actual if mem_actual is not None else 0.0,
        memory_waste_pct=mem_waste_pct,
        memory_wasted_gb=mem_wasted,
        is_over_provisioned=max(cpu_waste_pct, mem_waste_pct) >= _OVER_PROVISION_THRESHOLD_PCT,
    )

mutants_x__compute_namespace_waste__mutmut['_mutmut_orig'] = x__compute_namespace_waste__mutmut_orig # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_1'] = x__compute_namespace_waste__mutmut_1 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_2'] = x__compute_namespace_waste__mutmut_2 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_3'] = x__compute_namespace_waste__mutmut_3 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_4'] = x__compute_namespace_waste__mutmut_4 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_5'] = x__compute_namespace_waste__mutmut_5 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_6'] = x__compute_namespace_waste__mutmut_6 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_7'] = x__compute_namespace_waste__mutmut_7 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_8'] = x__compute_namespace_waste__mutmut_8 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_9'] = x__compute_namespace_waste__mutmut_9 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_10'] = x__compute_namespace_waste__mutmut_10 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_11'] = x__compute_namespace_waste__mutmut_11 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_12'] = x__compute_namespace_waste__mutmut_12 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_13'] = x__compute_namespace_waste__mutmut_13 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_14'] = x__compute_namespace_waste__mutmut_14 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_15'] = x__compute_namespace_waste__mutmut_15 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_16'] = x__compute_namespace_waste__mutmut_16 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_17'] = x__compute_namespace_waste__mutmut_17 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_18'] = x__compute_namespace_waste__mutmut_18 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_19'] = x__compute_namespace_waste__mutmut_19 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_20'] = x__compute_namespace_waste__mutmut_20 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_21'] = x__compute_namespace_waste__mutmut_21 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_22'] = x__compute_namespace_waste__mutmut_22 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_23'] = x__compute_namespace_waste__mutmut_23 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_24'] = x__compute_namespace_waste__mutmut_24 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_25'] = x__compute_namespace_waste__mutmut_25 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_26'] = x__compute_namespace_waste__mutmut_26 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_27'] = x__compute_namespace_waste__mutmut_27 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_28'] = x__compute_namespace_waste__mutmut_28 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_29'] = x__compute_namespace_waste__mutmut_29 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_30'] = x__compute_namespace_waste__mutmut_30 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_31'] = x__compute_namespace_waste__mutmut_31 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_32'] = x__compute_namespace_waste__mutmut_32 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_33'] = x__compute_namespace_waste__mutmut_33 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_34'] = x__compute_namespace_waste__mutmut_34 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_35'] = x__compute_namespace_waste__mutmut_35 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_36'] = x__compute_namespace_waste__mutmut_36 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_37'] = x__compute_namespace_waste__mutmut_37 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_38'] = x__compute_namespace_waste__mutmut_38 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_39'] = x__compute_namespace_waste__mutmut_39 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_40'] = x__compute_namespace_waste__mutmut_40 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_41'] = x__compute_namespace_waste__mutmut_41 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_42'] = x__compute_namespace_waste__mutmut_42 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_43'] = x__compute_namespace_waste__mutmut_43 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_44'] = x__compute_namespace_waste__mutmut_44 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_45'] = x__compute_namespace_waste__mutmut_45 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_46'] = x__compute_namespace_waste__mutmut_46 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_47'] = x__compute_namespace_waste__mutmut_47 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_48'] = x__compute_namespace_waste__mutmut_48 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_49'] = x__compute_namespace_waste__mutmut_49 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_50'] = x__compute_namespace_waste__mutmut_50 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_51'] = x__compute_namespace_waste__mutmut_51 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_52'] = x__compute_namespace_waste__mutmut_52 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_53'] = x__compute_namespace_waste__mutmut_53 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_54'] = x__compute_namespace_waste__mutmut_54 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_55'] = x__compute_namespace_waste__mutmut_55 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_56'] = x__compute_namespace_waste__mutmut_56 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_57'] = x__compute_namespace_waste__mutmut_57 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_58'] = x__compute_namespace_waste__mutmut_58 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_59'] = x__compute_namespace_waste__mutmut_59 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_60'] = x__compute_namespace_waste__mutmut_60 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_61'] = x__compute_namespace_waste__mutmut_61 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_62'] = x__compute_namespace_waste__mutmut_62 # type: ignore # mutmut generated
mutants_x__compute_namespace_waste__mutmut['x__compute_namespace_waste__mutmut_63'] = x__compute_namespace_waste__mutmut_63 # type: ignore # mutmut generated
mutants_x_any_actual_usage_present__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_any_actual_usage_present__mutmut)
def any_actual_usage_present(raw_data: list[NamespaceRawData]) -> bool:
    return any(
        (rd["cpu_actual_avg_cores"] is not None and rd["cpu_actual_avg_cores"] > 0)
        or (rd["memory_actual_avg_gb"] is not None and rd["memory_actual_avg_gb"] > 0)
        for rd in raw_data
    )


def x_any_actual_usage_present__mutmut_orig(raw_data: list[NamespaceRawData]) -> bool:
    return any(
        (rd["cpu_actual_avg_cores"] is not None and rd["cpu_actual_avg_cores"] > 0)
        or (rd["memory_actual_avg_gb"] is not None and rd["memory_actual_avg_gb"] > 0)
        for rd in raw_data
    )


def x_any_actual_usage_present__mutmut_1(raw_data: list[NamespaceRawData]) -> bool:
    return any(
        None
    )


def x_any_actual_usage_present__mutmut_2(raw_data: list[NamespaceRawData]) -> bool:
    return any(
        (rd["cpu_actual_avg_cores"] is not None and rd["cpu_actual_avg_cores"] > 0) and (rd["memory_actual_avg_gb"] is not None and rd["memory_actual_avg_gb"] > 0)
        for rd in raw_data
    )


def x_any_actual_usage_present__mutmut_3(raw_data: list[NamespaceRawData]) -> bool:
    return any(
        (rd["cpu_actual_avg_cores"] is not None or rd["cpu_actual_avg_cores"] > 0)
        or (rd["memory_actual_avg_gb"] is not None and rd["memory_actual_avg_gb"] > 0)
        for rd in raw_data
    )


def x_any_actual_usage_present__mutmut_4(raw_data: list[NamespaceRawData]) -> bool:
    return any(
        (rd["XXcpu_actual_avg_coresXX"] is not None and rd["cpu_actual_avg_cores"] > 0)
        or (rd["memory_actual_avg_gb"] is not None and rd["memory_actual_avg_gb"] > 0)
        for rd in raw_data
    )


def x_any_actual_usage_present__mutmut_5(raw_data: list[NamespaceRawData]) -> bool:
    return any(
        (rd["CPU_ACTUAL_AVG_CORES"] is not None and rd["cpu_actual_avg_cores"] > 0)
        or (rd["memory_actual_avg_gb"] is not None and rd["memory_actual_avg_gb"] > 0)
        for rd in raw_data
    )


def x_any_actual_usage_present__mutmut_6(raw_data: list[NamespaceRawData]) -> bool:
    return any(
        (rd["cpu_actual_avg_cores"] is None and rd["cpu_actual_avg_cores"] > 0)
        or (rd["memory_actual_avg_gb"] is not None and rd["memory_actual_avg_gb"] > 0)
        for rd in raw_data
    )


def x_any_actual_usage_present__mutmut_7(raw_data: list[NamespaceRawData]) -> bool:
    return any(
        (rd["cpu_actual_avg_cores"] is not None and rd["XXcpu_actual_avg_coresXX"] > 0)
        or (rd["memory_actual_avg_gb"] is not None and rd["memory_actual_avg_gb"] > 0)
        for rd in raw_data
    )


def x_any_actual_usage_present__mutmut_8(raw_data: list[NamespaceRawData]) -> bool:
    return any(
        (rd["cpu_actual_avg_cores"] is not None and rd["CPU_ACTUAL_AVG_CORES"] > 0)
        or (rd["memory_actual_avg_gb"] is not None and rd["memory_actual_avg_gb"] > 0)
        for rd in raw_data
    )


def x_any_actual_usage_present__mutmut_9(raw_data: list[NamespaceRawData]) -> bool:
    return any(
        (rd["cpu_actual_avg_cores"] is not None and rd["cpu_actual_avg_cores"] >= 0)
        or (rd["memory_actual_avg_gb"] is not None and rd["memory_actual_avg_gb"] > 0)
        for rd in raw_data
    )


def x_any_actual_usage_present__mutmut_10(raw_data: list[NamespaceRawData]) -> bool:
    return any(
        (rd["cpu_actual_avg_cores"] is not None and rd["cpu_actual_avg_cores"] > 1)
        or (rd["memory_actual_avg_gb"] is not None and rd["memory_actual_avg_gb"] > 0)
        for rd in raw_data
    )


def x_any_actual_usage_present__mutmut_11(raw_data: list[NamespaceRawData]) -> bool:
    return any(
        (rd["cpu_actual_avg_cores"] is not None and rd["cpu_actual_avg_cores"] > 0)
        or (rd["memory_actual_avg_gb"] is not None or rd["memory_actual_avg_gb"] > 0)
        for rd in raw_data
    )


def x_any_actual_usage_present__mutmut_12(raw_data: list[NamespaceRawData]) -> bool:
    return any(
        (rd["cpu_actual_avg_cores"] is not None and rd["cpu_actual_avg_cores"] > 0)
        or (rd["XXmemory_actual_avg_gbXX"] is not None and rd["memory_actual_avg_gb"] > 0)
        for rd in raw_data
    )


def x_any_actual_usage_present__mutmut_13(raw_data: list[NamespaceRawData]) -> bool:
    return any(
        (rd["cpu_actual_avg_cores"] is not None and rd["cpu_actual_avg_cores"] > 0)
        or (rd["MEMORY_ACTUAL_AVG_GB"] is not None and rd["memory_actual_avg_gb"] > 0)
        for rd in raw_data
    )


def x_any_actual_usage_present__mutmut_14(raw_data: list[NamespaceRawData]) -> bool:
    return any(
        (rd["cpu_actual_avg_cores"] is not None and rd["cpu_actual_avg_cores"] > 0)
        or (rd["memory_actual_avg_gb"] is None and rd["memory_actual_avg_gb"] > 0)
        for rd in raw_data
    )


def x_any_actual_usage_present__mutmut_15(raw_data: list[NamespaceRawData]) -> bool:
    return any(
        (rd["cpu_actual_avg_cores"] is not None and rd["cpu_actual_avg_cores"] > 0)
        or (rd["memory_actual_avg_gb"] is not None and rd["XXmemory_actual_avg_gbXX"] > 0)
        for rd in raw_data
    )


def x_any_actual_usage_present__mutmut_16(raw_data: list[NamespaceRawData]) -> bool:
    return any(
        (rd["cpu_actual_avg_cores"] is not None and rd["cpu_actual_avg_cores"] > 0)
        or (rd["memory_actual_avg_gb"] is not None and rd["MEMORY_ACTUAL_AVG_GB"] > 0)
        for rd in raw_data
    )


def x_any_actual_usage_present__mutmut_17(raw_data: list[NamespaceRawData]) -> bool:
    return any(
        (rd["cpu_actual_avg_cores"] is not None and rd["cpu_actual_avg_cores"] > 0)
        or (rd["memory_actual_avg_gb"] is not None and rd["memory_actual_avg_gb"] >= 0)
        for rd in raw_data
    )


def x_any_actual_usage_present__mutmut_18(raw_data: list[NamespaceRawData]) -> bool:
    return any(
        (rd["cpu_actual_avg_cores"] is not None and rd["cpu_actual_avg_cores"] > 0)
        or (rd["memory_actual_avg_gb"] is not None and rd["memory_actual_avg_gb"] > 1)
        for rd in raw_data
    )

mutants_x_any_actual_usage_present__mutmut['_mutmut_orig'] = x_any_actual_usage_present__mutmut_orig # type: ignore # mutmut generated
mutants_x_any_actual_usage_present__mutmut['x_any_actual_usage_present__mutmut_1'] = x_any_actual_usage_present__mutmut_1 # type: ignore # mutmut generated
mutants_x_any_actual_usage_present__mutmut['x_any_actual_usage_present__mutmut_2'] = x_any_actual_usage_present__mutmut_2 # type: ignore # mutmut generated
mutants_x_any_actual_usage_present__mutmut['x_any_actual_usage_present__mutmut_3'] = x_any_actual_usage_present__mutmut_3 # type: ignore # mutmut generated
mutants_x_any_actual_usage_present__mutmut['x_any_actual_usage_present__mutmut_4'] = x_any_actual_usage_present__mutmut_4 # type: ignore # mutmut generated
mutants_x_any_actual_usage_present__mutmut['x_any_actual_usage_present__mutmut_5'] = x_any_actual_usage_present__mutmut_5 # type: ignore # mutmut generated
mutants_x_any_actual_usage_present__mutmut['x_any_actual_usage_present__mutmut_6'] = x_any_actual_usage_present__mutmut_6 # type: ignore # mutmut generated
mutants_x_any_actual_usage_present__mutmut['x_any_actual_usage_present__mutmut_7'] = x_any_actual_usage_present__mutmut_7 # type: ignore # mutmut generated
mutants_x_any_actual_usage_present__mutmut['x_any_actual_usage_present__mutmut_8'] = x_any_actual_usage_present__mutmut_8 # type: ignore # mutmut generated
mutants_x_any_actual_usage_present__mutmut['x_any_actual_usage_present__mutmut_9'] = x_any_actual_usage_present__mutmut_9 # type: ignore # mutmut generated
mutants_x_any_actual_usage_present__mutmut['x_any_actual_usage_present__mutmut_10'] = x_any_actual_usage_present__mutmut_10 # type: ignore # mutmut generated
mutants_x_any_actual_usage_present__mutmut['x_any_actual_usage_present__mutmut_11'] = x_any_actual_usage_present__mutmut_11 # type: ignore # mutmut generated
mutants_x_any_actual_usage_present__mutmut['x_any_actual_usage_present__mutmut_12'] = x_any_actual_usage_present__mutmut_12 # type: ignore # mutmut generated
mutants_x_any_actual_usage_present__mutmut['x_any_actual_usage_present__mutmut_13'] = x_any_actual_usage_present__mutmut_13 # type: ignore # mutmut generated
mutants_x_any_actual_usage_present__mutmut['x_any_actual_usage_present__mutmut_14'] = x_any_actual_usage_present__mutmut_14 # type: ignore # mutmut generated
mutants_x_any_actual_usage_present__mutmut['x_any_actual_usage_present__mutmut_15'] = x_any_actual_usage_present__mutmut_15 # type: ignore # mutmut generated
mutants_x_any_actual_usage_present__mutmut['x_any_actual_usage_present__mutmut_16'] = x_any_actual_usage_present__mutmut_16 # type: ignore # mutmut generated
mutants_x_any_actual_usage_present__mutmut['x_any_actual_usage_present__mutmut_17'] = x_any_actual_usage_present__mutmut_17 # type: ignore # mutmut generated
mutants_x_any_actual_usage_present__mutmut['x_any_actual_usage_present__mutmut_18'] = x_any_actual_usage_present__mutmut_18 # type: ignore # mutmut generated
mutants_x__waste_pair__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__waste_pair__mutmut)
def _waste_pair(requested: float, actual: float | None) -> tuple[float, float]:
    """Return (waste_pct, wasted_units). Returns (0.0, 0.0) when actual is unknown."""
    if actual is None or requested == 0.0:
        return 0.0, 0.0
    wasted = max(0.0, requested - actual)
    waste_pct = wasted / requested * 100.0
    return waste_pct, wasted


def x__waste_pair__mutmut_orig(requested: float, actual: float | None) -> tuple[float, float]:
    """Return (waste_pct, wasted_units). Returns (0.0, 0.0) when actual is unknown."""
    if actual is None or requested == 0.0:
        return 0.0, 0.0
    wasted = max(0.0, requested - actual)
    waste_pct = wasted / requested * 100.0
    return waste_pct, wasted


def x__waste_pair__mutmut_1(requested: float, actual: float | None) -> tuple[float, float]:
    """Return (waste_pct, wasted_units). Returns (0.0, 0.0) when actual is unknown."""
    if actual is None and requested == 0.0:
        return 0.0, 0.0
    wasted = max(0.0, requested - actual)
    waste_pct = wasted / requested * 100.0
    return waste_pct, wasted


def x__waste_pair__mutmut_2(requested: float, actual: float | None) -> tuple[float, float]:
    """Return (waste_pct, wasted_units). Returns (0.0, 0.0) when actual is unknown."""
    if actual is not None or requested == 0.0:
        return 0.0, 0.0
    wasted = max(0.0, requested - actual)
    waste_pct = wasted / requested * 100.0
    return waste_pct, wasted


def x__waste_pair__mutmut_3(requested: float, actual: float | None) -> tuple[float, float]:
    """Return (waste_pct, wasted_units). Returns (0.0, 0.0) when actual is unknown."""
    if actual is None or requested != 0.0:
        return 0.0, 0.0
    wasted = max(0.0, requested - actual)
    waste_pct = wasted / requested * 100.0
    return waste_pct, wasted


def x__waste_pair__mutmut_4(requested: float, actual: float | None) -> tuple[float, float]:
    """Return (waste_pct, wasted_units). Returns (0.0, 0.0) when actual is unknown."""
    if actual is None or requested == 1.0:
        return 0.0, 0.0
    wasted = max(0.0, requested - actual)
    waste_pct = wasted / requested * 100.0
    return waste_pct, wasted


def x__waste_pair__mutmut_5(requested: float, actual: float | None) -> tuple[float, float]:
    """Return (waste_pct, wasted_units). Returns (0.0, 0.0) when actual is unknown."""
    if actual is None or requested == 0.0:
        return 1.0, 0.0
    wasted = max(0.0, requested - actual)
    waste_pct = wasted / requested * 100.0
    return waste_pct, wasted


def x__waste_pair__mutmut_6(requested: float, actual: float | None) -> tuple[float, float]:
    """Return (waste_pct, wasted_units). Returns (0.0, 0.0) when actual is unknown."""
    if actual is None or requested == 0.0:
        return 0.0, 1.0
    wasted = max(0.0, requested - actual)
    waste_pct = wasted / requested * 100.0
    return waste_pct, wasted


def x__waste_pair__mutmut_7(requested: float, actual: float | None) -> tuple[float, float]:
    """Return (waste_pct, wasted_units). Returns (0.0, 0.0) when actual is unknown."""
    if actual is None or requested == 0.0:
        return 0.0, 0.0
    wasted = None
    waste_pct = wasted / requested * 100.0
    return waste_pct, wasted


def x__waste_pair__mutmut_8(requested: float, actual: float | None) -> tuple[float, float]:
    """Return (waste_pct, wasted_units). Returns (0.0, 0.0) when actual is unknown."""
    if actual is None or requested == 0.0:
        return 0.0, 0.0
    wasted = max(None, requested - actual)
    waste_pct = wasted / requested * 100.0
    return waste_pct, wasted


def x__waste_pair__mutmut_9(requested: float, actual: float | None) -> tuple[float, float]:
    """Return (waste_pct, wasted_units). Returns (0.0, 0.0) when actual is unknown."""
    if actual is None or requested == 0.0:
        return 0.0, 0.0
    wasted = max(0.0, None)
    waste_pct = wasted / requested * 100.0
    return waste_pct, wasted


def x__waste_pair__mutmut_10(requested: float, actual: float | None) -> tuple[float, float]:
    """Return (waste_pct, wasted_units). Returns (0.0, 0.0) when actual is unknown."""
    if actual is None or requested == 0.0:
        return 0.0, 0.0
    wasted = max(requested - actual)
    waste_pct = wasted / requested * 100.0
    return waste_pct, wasted


def x__waste_pair__mutmut_11(requested: float, actual: float | None) -> tuple[float, float]:
    """Return (waste_pct, wasted_units). Returns (0.0, 0.0) when actual is unknown."""
    if actual is None or requested == 0.0:
        return 0.0, 0.0
    wasted = max(0.0, )
    waste_pct = wasted / requested * 100.0
    return waste_pct, wasted


def x__waste_pair__mutmut_12(requested: float, actual: float | None) -> tuple[float, float]:
    """Return (waste_pct, wasted_units). Returns (0.0, 0.0) when actual is unknown."""
    if actual is None or requested == 0.0:
        return 0.0, 0.0
    wasted = max(1.0, requested - actual)
    waste_pct = wasted / requested * 100.0
    return waste_pct, wasted


def x__waste_pair__mutmut_13(requested: float, actual: float | None) -> tuple[float, float]:
    """Return (waste_pct, wasted_units). Returns (0.0, 0.0) when actual is unknown."""
    if actual is None or requested == 0.0:
        return 0.0, 0.0
    wasted = max(0.0, requested + actual)
    waste_pct = wasted / requested * 100.0
    return waste_pct, wasted


def x__waste_pair__mutmut_14(requested: float, actual: float | None) -> tuple[float, float]:
    """Return (waste_pct, wasted_units). Returns (0.0, 0.0) when actual is unknown."""
    if actual is None or requested == 0.0:
        return 0.0, 0.0
    wasted = max(0.0, requested - actual)
    waste_pct = None
    return waste_pct, wasted


def x__waste_pair__mutmut_15(requested: float, actual: float | None) -> tuple[float, float]:
    """Return (waste_pct, wasted_units). Returns (0.0, 0.0) when actual is unknown."""
    if actual is None or requested == 0.0:
        return 0.0, 0.0
    wasted = max(0.0, requested - actual)
    waste_pct = wasted / requested / 100.0
    return waste_pct, wasted


def x__waste_pair__mutmut_16(requested: float, actual: float | None) -> tuple[float, float]:
    """Return (waste_pct, wasted_units). Returns (0.0, 0.0) when actual is unknown."""
    if actual is None or requested == 0.0:
        return 0.0, 0.0
    wasted = max(0.0, requested - actual)
    waste_pct = wasted * requested * 100.0
    return waste_pct, wasted


def x__waste_pair__mutmut_17(requested: float, actual: float | None) -> tuple[float, float]:
    """Return (waste_pct, wasted_units). Returns (0.0, 0.0) when actual is unknown."""
    if actual is None or requested == 0.0:
        return 0.0, 0.0
    wasted = max(0.0, requested - actual)
    waste_pct = wasted / requested * 101.0
    return waste_pct, wasted

mutants_x__waste_pair__mutmut['_mutmut_orig'] = x__waste_pair__mutmut_orig # type: ignore # mutmut generated
mutants_x__waste_pair__mutmut['x__waste_pair__mutmut_1'] = x__waste_pair__mutmut_1 # type: ignore # mutmut generated
mutants_x__waste_pair__mutmut['x__waste_pair__mutmut_2'] = x__waste_pair__mutmut_2 # type: ignore # mutmut generated
mutants_x__waste_pair__mutmut['x__waste_pair__mutmut_3'] = x__waste_pair__mutmut_3 # type: ignore # mutmut generated
mutants_x__waste_pair__mutmut['x__waste_pair__mutmut_4'] = x__waste_pair__mutmut_4 # type: ignore # mutmut generated
mutants_x__waste_pair__mutmut['x__waste_pair__mutmut_5'] = x__waste_pair__mutmut_5 # type: ignore # mutmut generated
mutants_x__waste_pair__mutmut['x__waste_pair__mutmut_6'] = x__waste_pair__mutmut_6 # type: ignore # mutmut generated
mutants_x__waste_pair__mutmut['x__waste_pair__mutmut_7'] = x__waste_pair__mutmut_7 # type: ignore # mutmut generated
mutants_x__waste_pair__mutmut['x__waste_pair__mutmut_8'] = x__waste_pair__mutmut_8 # type: ignore # mutmut generated
mutants_x__waste_pair__mutmut['x__waste_pair__mutmut_9'] = x__waste_pair__mutmut_9 # type: ignore # mutmut generated
mutants_x__waste_pair__mutmut['x__waste_pair__mutmut_10'] = x__waste_pair__mutmut_10 # type: ignore # mutmut generated
mutants_x__waste_pair__mutmut['x__waste_pair__mutmut_11'] = x__waste_pair__mutmut_11 # type: ignore # mutmut generated
mutants_x__waste_pair__mutmut['x__waste_pair__mutmut_12'] = x__waste_pair__mutmut_12 # type: ignore # mutmut generated
mutants_x__waste_pair__mutmut['x__waste_pair__mutmut_13'] = x__waste_pair__mutmut_13 # type: ignore # mutmut generated
mutants_x__waste_pair__mutmut['x__waste_pair__mutmut_14'] = x__waste_pair__mutmut_14 # type: ignore # mutmut generated
mutants_x__waste_pair__mutmut['x__waste_pair__mutmut_15'] = x__waste_pair__mutmut_15 # type: ignore # mutmut generated
mutants_x__waste_pair__mutmut['x__waste_pair__mutmut_16'] = x__waste_pair__mutmut_16 # type: ignore # mutmut generated
mutants_x__waste_pair__mutmut['x__waste_pair__mutmut_17'] = x__waste_pair__mutmut_17 # type: ignore # mutmut generated
