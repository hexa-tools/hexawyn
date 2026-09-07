from __future__ import annotations

from hexawyn.application.ports.driven.slow_trace_search_port import SlowTraceSearchPort
from hexawyn.domain.models.slowest_traces import SlowestTracesRequest, SlowTrace
from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_client import search_jaeger_traces


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut: MutantDict = {}  # type: ignore


class OTelPodTraceAdapter(SlowTraceSearchPort):
    @_mutmut_mutated(mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut)
    def search_pod_traces(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_orig(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_1(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = None
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_2(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service=None,
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_3(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min=None,
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_4(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=None,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_5(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_6(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_7(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_8(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="XXXX",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_9(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="XX100msXX",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_10(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100MS",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_11(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = None
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_12(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                None
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_13(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=None,
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_14(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=None,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_15(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation=None,
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_16(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=None,
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_17(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_18(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_19(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_20(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_21(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["XXtraceIDXX"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_22(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceid"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_23(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["TRACEID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_24(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) * 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_25(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(None) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_26(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get(None, 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_27(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", None)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_28(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get(0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_29(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", )) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_30(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("XXdurationXX", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_31(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("DURATION", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_32(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 1)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_33(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1001.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_34(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="XXXX",
                    span_count=int(trace.get("spanCount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_35(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(None),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_36(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get(None, 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_37(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", None)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_38(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get(0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_39(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", )),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_40(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("XXspanCountXX", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_41(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spancount", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_42(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("SPANCOUNT", 0)),
                )
            )
        return result
    def xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_43(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        traces = search_jaeger_traces(
            service="",
            duration_min="100ms",
            limit=request.top_n,
        )
        result: list[SlowTrace] = []
        for trace in traces:
            result.append(
                SlowTrace(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                    operation="",
                    span_count=int(trace.get("spanCount", 1)),
                )
            )
        return result

mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['_mutmut_orig'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_1'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_2'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_3'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_4'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_5'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_6'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_7'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_8'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_9'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_10'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_11'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_12'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_13'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_14'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_15'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_16'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_17'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_18'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_19'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_19 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_20'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_20 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_21'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_21 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_22'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_22 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_23'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_23 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_24'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_24 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_25'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_25 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_26'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_26 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_27'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_27 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_28'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_28 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_29'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_29 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_30'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_30 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_31'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_31 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_32'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_32 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_33'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_33 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_34'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_34 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_35'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_35 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_36'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_36 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_37'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_37 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_38'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_38 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_39'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_39 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_40'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_40 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_41'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_41 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_42'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_42 # type: ignore # mutmut generated
mutants_xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut['xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_43'] = OTelPodTraceAdapter.xǁOTelPodTraceAdapterǁsearch_pod_traces__mutmut_43 # type: ignore # mutmut generated
