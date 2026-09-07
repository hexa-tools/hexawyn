from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.trace_query_port import TraceQueryPort
from hexawyn.application.use_case.observability.latency_diagnostic.command import (
    LatencyDiagnosticCommand,
)
from hexawyn.application.use_case.observability.latency_diagnostic.response import (
    LatencyDiagnosticResponse,
)
from hexawyn.domain.models.latency_diagnostic import (
    LatencyDiagnosticRequest,
    LatencyDiagnosticResult,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁLatencyDiagnosticUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class LatencyDiagnosticUseCase:
    @_mutmut_mutated(mutants_xǁLatencyDiagnosticUseCaseǁ__init____mutmut)
    def __init__(self, port: TraceQueryPort) -> None:
        self._port = port
    def xǁLatencyDiagnosticUseCaseǁ__init____mutmut_orig(self, port: TraceQueryPort) -> None:
        self._port = port
    def xǁLatencyDiagnosticUseCaseǁ__init____mutmut_1(self, port: TraceQueryPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut)
    def execute(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_orig(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_1(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = None
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_2(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=None,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_3(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=None,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_4(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=None,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_5(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_6(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_7(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_8(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = None
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_9(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(None)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_10(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = None
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_11(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(None)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_12(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = None
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_13(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=None, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_14(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=None, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_15(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=None)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_16(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_17(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_18(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, )
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_19(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=None,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_20(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=None,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_21(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=None,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_22(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=None,
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_23(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_24(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_25(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_26(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_27(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_28(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_29(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(None) for b in r.bottlenecks],
            slowest_span=asdict(r.slowest_span) if r.slowest_span else None,
        )

    def xǁLatencyDiagnosticUseCaseǁexecute__mutmut_30(self, command: LatencyDiagnosticCommand) -> LatencyDiagnosticResponse:
        req = LatencyDiagnosticRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            threshold_ms=command.threshold_ms,
        )
        spans = self._port.fetch_slow_spans(req)
        total = self._port.fetch_total_traces(req)
        r = LatencyDiagnosticResult.compute(request=req, slow_spans=spans, total_traces=total)
        return LatencyDiagnosticResponse(
            service_name=r.service_name,
            slow_trace_count=r.slow_trace_count,
            total_traces=r.total_traces,
            bottlenecks=[asdict(b) for b in r.bottlenecks],
            slowest_span=asdict(None) if r.slowest_span else None,
        )

mutants_xǁLatencyDiagnosticUseCaseǁ__init____mutmut['_mutmut_orig'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁ__init____mutmut['xǁLatencyDiagnosticUseCaseǁ__init____mutmut_1'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['_mutmut_orig'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_1'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_2'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_3'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_4'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_5'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_6'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_7'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_8'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_9'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_10'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_11'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_12'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_13'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_14'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_15'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_16'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_17'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_18'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_19'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_20'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_21'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_22'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_23'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_24'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_25'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_26'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_27'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_28'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_29'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁLatencyDiagnosticUseCaseǁexecute__mutmut['xǁLatencyDiagnosticUseCaseǁexecute__mutmut_30'] = LatencyDiagnosticUseCase.xǁLatencyDiagnosticUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
