from __future__ import annotations

from hexawyn.application.ports.driven.trace_query_port import TraceQueryPort
from hexawyn.domain.models.latency_diagnostic import (
    LatencyDiagnosticRequest,
    TraceSpan,
)
from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_client import search_jaeger_traces


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOTelHTTPAdapterǁfetch_total_traces__mutmut: MutantDict = {}  # type: ignore


class OTelHTTPAdapter(TraceQueryPort):
    @_mutmut_mutated(mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut)
    def fetch_slow_spans(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_orig(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_1(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_2(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = None
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_3(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=None,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_4(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min=None,
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_5(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=None,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_6(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_7(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_8(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_9(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="XX50msXX",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_10(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50MS",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_11(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=11,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_12(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = None
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_13(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = None
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_14(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=None,
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_15(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=None,
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_16(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=None,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_17(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_18(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_19(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_20(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["XXtraceIDXX"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_21(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceid"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_22(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["TRACEID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_23(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['XXtraceIDXX'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_24(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceid'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_25(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['TRACEID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_26(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:9]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_27(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) * 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_28(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(None) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_29(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get(None, 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_30(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", None)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_31(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get(0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_32(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", )) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_33(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("XXdurationXX", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_34(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("DURATION", 0)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_35(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 1)) / 1000.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_36(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1001.0,
                )
            ]
            result.append(spans)
        return result
    def xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_37(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        if not request.service_name:
            return []

        traces = search_jaeger_traces(
            service=request.service_name,
            duration_min="50ms",
            limit=10,
        )
        result: list[list[TraceSpan]] = []
        for trace in traces:
            spans = [
                TraceSpan(
                    trace_id=trace["traceID"],
                    span_name=f"trace:{trace['traceID'][:8]}",
                    duration_ms=float(trace.get("duration", 0)) / 1000.0,
                )
            ]
            result.append(None)
        return result

    @_mutmut_mutated(mutants_xǁOTelHTTPAdapterǁfetch_total_traces__mutmut)
    def fetch_total_traces(self, request: LatencyDiagnosticRequest) -> int:
        if not request.service_name:
            return 0

        traces = search_jaeger_traces(
            service=request.service_name,
            limit=100,
        )
        return len(traces)

    def xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_orig(self, request: LatencyDiagnosticRequest) -> int:
        if not request.service_name:
            return 0

        traces = search_jaeger_traces(
            service=request.service_name,
            limit=100,
        )
        return len(traces)

    def xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_1(self, request: LatencyDiagnosticRequest) -> int:
        if request.service_name:
            return 0

        traces = search_jaeger_traces(
            service=request.service_name,
            limit=100,
        )
        return len(traces)

    def xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_2(self, request: LatencyDiagnosticRequest) -> int:
        if not request.service_name:
            return 1

        traces = search_jaeger_traces(
            service=request.service_name,
            limit=100,
        )
        return len(traces)

    def xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_3(self, request: LatencyDiagnosticRequest) -> int:
        if not request.service_name:
            return 0

        traces = None
        return len(traces)

    def xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_4(self, request: LatencyDiagnosticRequest) -> int:
        if not request.service_name:
            return 0

        traces = search_jaeger_traces(
            service=None,
            limit=100,
        )
        return len(traces)

    def xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_5(self, request: LatencyDiagnosticRequest) -> int:
        if not request.service_name:
            return 0

        traces = search_jaeger_traces(
            service=request.service_name,
            limit=None,
        )
        return len(traces)

    def xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_6(self, request: LatencyDiagnosticRequest) -> int:
        if not request.service_name:
            return 0

        traces = search_jaeger_traces(
            limit=100,
        )
        return len(traces)

    def xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_7(self, request: LatencyDiagnosticRequest) -> int:
        if not request.service_name:
            return 0

        traces = search_jaeger_traces(
            service=request.service_name,
            )
        return len(traces)

    def xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_8(self, request: LatencyDiagnosticRequest) -> int:
        if not request.service_name:
            return 0

        traces = search_jaeger_traces(
            service=request.service_name,
            limit=101,
        )
        return len(traces)

mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['_mutmut_orig'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_1'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_2'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_3'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_4'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_5'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_6'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_7'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_8'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_9'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_10'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_11'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_12'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_13'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_14'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_15'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_16'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_17'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_18'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_19'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_19 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_20'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_20 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_21'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_21 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_22'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_22 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_23'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_23 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_24'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_24 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_25'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_25 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_26'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_26 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_27'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_27 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_28'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_28 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_29'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_29 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_30'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_30 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_31'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_31 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_32'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_32 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_33'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_33 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_34'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_34 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_35'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_35 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_36'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_36 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut['xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_37'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_slow_spans__mutmut_37 # type: ignore # mutmut generated

mutants_xǁOTelHTTPAdapterǁfetch_total_traces__mutmut['_mutmut_orig'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_total_traces__mutmut['xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_1'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_total_traces__mutmut['xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_2'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_total_traces__mutmut['xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_3'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_total_traces__mutmut['xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_4'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_total_traces__mutmut['xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_5'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_total_traces__mutmut['xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_6'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_total_traces__mutmut['xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_7'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOTelHTTPAdapterǁfetch_total_traces__mutmut['xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_8'] = OTelHTTPAdapter.xǁOTelHTTPAdapterǁfetch_total_traces__mutmut_8 # type: ignore # mutmut generated
