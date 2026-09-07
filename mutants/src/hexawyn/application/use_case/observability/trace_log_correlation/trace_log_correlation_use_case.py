from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.trace_log_correlation_port import TraceLogCorrelationPort
from hexawyn.application.use_case.observability.trace_log_correlation.command import (
    TraceLogCorrelationCommand,
)
from hexawyn.application.use_case.observability.trace_log_correlation.response import (
    TraceLogCorrelationResponse,
)
from hexawyn.domain.models.trace_log_correlation import TraceLogCorrelationRequest, TraceLogResult


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁTraceLogCorrelationUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class TraceLogCorrelationUseCase:
    @_mutmut_mutated(mutants_xǁTraceLogCorrelationUseCaseǁ__init____mutmut)
    def __init__(self, port: TraceLogCorrelationPort) -> None:
        self._port = port
    def xǁTraceLogCorrelationUseCaseǁ__init____mutmut_orig(self, port: TraceLogCorrelationPort) -> None:
        self._port = port
    def xǁTraceLogCorrelationUseCaseǁ__init____mutmut_1(self, port: TraceLogCorrelationPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut)
    def execute(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_orig(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_1(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = None
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_2(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=None, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_3(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=None)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_4(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_5(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, )
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_6(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = None
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_7(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(None)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_8(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_9(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[1].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_10(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = None
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_11(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(None) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_12(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = None
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_13(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=None, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_14(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=None, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_15(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=None)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_16(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_17(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_18(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, )
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_19(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=None,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_20(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=None,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_21(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=None,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_22(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=None,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_23(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=None,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_24(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=None,  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_25(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=None,  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_26(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_27(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_28(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_29(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_30(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_31(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_32(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_33(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(None) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(c) for c in r.correlated_logs],  # type: ignore
        )

    def xǁTraceLogCorrelationUseCaseǁexecute__mutmut_34(self, command: TraceLogCorrelationCommand) -> TraceLogCorrelationResponse:
        req = TraceLogCorrelationRequest(operation=command.operation, trace_id=command.trace_id)
        spans = self._port.fetch_error_spans(req)
        trace_id = spans[0].trace_id if spans else None
        logs = self._port.fetch_correlated_logs(trace_id) if trace_id else []
        r = TraceLogResult.compute(request=req, error_spans=spans, logs=logs)
        return TraceLogCorrelationResponse(
            trace_id=r.trace_id,  # type: ignore
            operation=r.operation,
            error_span_count=r.error_span_count,
            correlated_log_count=r.correlated_log_count,
            summary=r.summary,
            error_spans=[asdict(s) for s in r.error_spans],  # type: ignore
            correlated_logs=[asdict(None) for c in r.correlated_logs],  # type: ignore
        )

mutants_xǁTraceLogCorrelationUseCaseǁ__init____mutmut['_mutmut_orig'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁ__init____mutmut['xǁTraceLogCorrelationUseCaseǁ__init____mutmut_1'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['_mutmut_orig'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_1'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_2'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_3'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_4'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_5'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_6'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_7'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_8'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_9'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_10'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_11'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_12'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_13'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_14'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_15'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_16'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_17'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_18'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_19'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_20'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_21'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_22'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_23'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_24'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_25'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_26'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_27'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_28'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_29'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_30'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_31'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_32'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_33'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁTraceLogCorrelationUseCaseǁexecute__mutmut['xǁTraceLogCorrelationUseCaseǁexecute__mutmut_34'] = TraceLogCorrelationUseCase.xǁTraceLogCorrelationUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
