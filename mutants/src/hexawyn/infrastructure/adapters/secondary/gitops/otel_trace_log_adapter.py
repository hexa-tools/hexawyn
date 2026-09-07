from __future__ import annotations

from hexawyn.application.ports.driven.trace_log_correlation_port import (
    TraceLogCorrelationPort,
)
from hexawyn.domain.models.trace_log_correlation import (
    CorrelatedLog,
    TraceLogCorrelationRequest,
    TraceLogSpan,
)
from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_client import search_jaeger_traces


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut: MutantDict = {}  # type: ignore


class OTelTraceLogAdapter(TraceLogCorrelationPort):
    @_mutmut_mutated(mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut)
    def fetch_error_spans(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_orig(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_1(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_2(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = None
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_3(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service=None,
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_4(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=None,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_5(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=None,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_6(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_7(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_8(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_9(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="XXXX",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_10(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=False,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_11(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=21,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_12(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = None
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_13(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                None
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_14(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=None,
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_15(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=None,
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_16(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message=None,
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_17(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp=None,
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_18(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_19(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_20(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_21(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_22(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["XXtraceIDXX"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_23(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceid"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_24(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["TRACEID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_25(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["XXtraceIDXX"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_26(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceid"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_27(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["TRACEID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_28(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:17],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_29(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="XXerror detectedXX" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_30(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="ERROR DETECTED" if trace.get("hasErrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_31(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get(None) else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_32(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("XXhasErrorsXX") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_33(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("haserrors") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_34(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("HASERRORS") else "",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_35(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "XXXX",
                    timestamp="",
                )
            )
        return result
    def xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_36(self, request: TraceLogCorrelationRequest) -> list[TraceLogSpan]:
        if not request.operation:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
            limit=20,
        )
        result: list[TraceLogSpan] = []
        for trace in traces:
            result.append(
                TraceLogSpan(
                    trace_id=trace["traceID"],
                    span_name=trace["traceID"][:16],
                    error_message="error detected" if trace.get("hasErrors") else "",
                    timestamp="XXXX",
                )
            )
        return result

    @_mutmut_mutated(mutants_xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut)
    def fetch_correlated_logs(self, trace_id: str) -> list[CorrelatedLog]:
        if not trace_id:
            return []

        return [
            CorrelatedLog(
                timestamp="",
                level="info",
                message="log data not available without log backend",
            )
        ]

    def xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_orig(self, trace_id: str) -> list[CorrelatedLog]:
        if not trace_id:
            return []

        return [
            CorrelatedLog(
                timestamp="",
                level="info",
                message="log data not available without log backend",
            )
        ]

    def xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_1(self, trace_id: str) -> list[CorrelatedLog]:
        if trace_id:
            return []

        return [
            CorrelatedLog(
                timestamp="",
                level="info",
                message="log data not available without log backend",
            )
        ]

    def xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_2(self, trace_id: str) -> list[CorrelatedLog]:
        if not trace_id:
            return []

        return [
            CorrelatedLog(
                timestamp=None,
                level="info",
                message="log data not available without log backend",
            )
        ]

    def xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_3(self, trace_id: str) -> list[CorrelatedLog]:
        if not trace_id:
            return []

        return [
            CorrelatedLog(
                timestamp="",
                level=None,
                message="log data not available without log backend",
            )
        ]

    def xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_4(self, trace_id: str) -> list[CorrelatedLog]:
        if not trace_id:
            return []

        return [
            CorrelatedLog(
                timestamp="",
                level="info",
                message=None,
            )
        ]

    def xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_5(self, trace_id: str) -> list[CorrelatedLog]:
        if not trace_id:
            return []

        return [
            CorrelatedLog(
                level="info",
                message="log data not available without log backend",
            )
        ]

    def xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_6(self, trace_id: str) -> list[CorrelatedLog]:
        if not trace_id:
            return []

        return [
            CorrelatedLog(
                timestamp="",
                message="log data not available without log backend",
            )
        ]

    def xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_7(self, trace_id: str) -> list[CorrelatedLog]:
        if not trace_id:
            return []

        return [
            CorrelatedLog(
                timestamp="",
                level="info",
                )
        ]

    def xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_8(self, trace_id: str) -> list[CorrelatedLog]:
        if not trace_id:
            return []

        return [
            CorrelatedLog(
                timestamp="XXXX",
                level="info",
                message="log data not available without log backend",
            )
        ]

    def xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_9(self, trace_id: str) -> list[CorrelatedLog]:
        if not trace_id:
            return []

        return [
            CorrelatedLog(
                timestamp="",
                level="XXinfoXX",
                message="log data not available without log backend",
            )
        ]

    def xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_10(self, trace_id: str) -> list[CorrelatedLog]:
        if not trace_id:
            return []

        return [
            CorrelatedLog(
                timestamp="",
                level="INFO",
                message="log data not available without log backend",
            )
        ]

    def xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_11(self, trace_id: str) -> list[CorrelatedLog]:
        if not trace_id:
            return []

        return [
            CorrelatedLog(
                timestamp="",
                level="info",
                message="XXlog data not available without log backendXX",
            )
        ]

    def xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_12(self, trace_id: str) -> list[CorrelatedLog]:
        if not trace_id:
            return []

        return [
            CorrelatedLog(
                timestamp="",
                level="info",
                message="LOG DATA NOT AVAILABLE WITHOUT LOG BACKEND",
            )
        ]

mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['_mutmut_orig'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_1'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_2'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_3'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_4'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_5'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_6'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_7'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_8'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_9'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_10'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_11'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_12'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_13'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_14'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_15'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_16'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_17'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_18'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_19'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_19 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_20'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_20 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_21'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_21 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_22'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_22 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_23'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_23 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_24'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_24 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_25'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_25 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_26'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_26 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_27'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_27 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_28'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_28 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_29'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_29 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_30'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_30 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_31'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_31 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_32'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_32 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_33'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_33 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_34'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_34 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_35'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_35 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut['xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_36'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_error_spans__mutmut_36 # type: ignore # mutmut generated

mutants_xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut['_mutmut_orig'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut['xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_1'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut['xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_2'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut['xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_3'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut['xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_4'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut['xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_5'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut['xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_6'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut['xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_7'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut['xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_8'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut['xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_9'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut['xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_10'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut['xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_11'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut['xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_12'] = OTelTraceLogAdapter.xǁOTelTraceLogAdapterǁfetch_correlated_logs__mutmut_12 # type: ignore # mutmut generated
