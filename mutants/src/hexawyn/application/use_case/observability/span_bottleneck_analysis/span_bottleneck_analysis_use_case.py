from __future__ import annotations

from hexawyn.application.ports.driven.span_bottleneck_port import SpanBottleneckPort
from hexawyn.application.use_case.observability.span_bottleneck_analysis.command import (
    SpanBottleneckAnalysisCommand,
)
from hexawyn.application.use_case.observability.span_bottleneck_analysis.response import (
    SpanBottleneckAnalysisResponse,
)
from hexawyn.domain.models.span_bottleneck import BottleneckRequest, BottleneckResult


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁSpanBottleneckAnalysisUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class SpanBottleneckAnalysisUseCase:
    @_mutmut_mutated(mutants_xǁSpanBottleneckAnalysisUseCaseǁ__init____mutmut)
    def __init__(self, port: SpanBottleneckPort) -> None:
        self._port = port
    def xǁSpanBottleneckAnalysisUseCaseǁ__init____mutmut_orig(self, port: SpanBottleneckPort) -> None:
        self._port = port
    def xǁSpanBottleneckAnalysisUseCaseǁ__init____mutmut_1(self, port: SpanBottleneckPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut)
    def execute(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_orig(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_1(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = None
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_2(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=None)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_3(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = None
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_4(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(None)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_5(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = None
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_6(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(None)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_7(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = None
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_8(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=None, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_9(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=None, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_10(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=None)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_11(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_12(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_13(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, )
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_14(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=None,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_15(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=None,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_16(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=None,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_17(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=None,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_18(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=None,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_19(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_20(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_21(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=None,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_22(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_23(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_24(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_25(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_26(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_27(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_28(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_29(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_30(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 1.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 0.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

    def xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_31(self, command: SpanBottleneckAnalysisCommand) -> SpanBottleneckAnalysisResponse:
        req = BottleneckRequest(time_window_minutes=command.time_window_minutes)
        db_spans = self._port.fetch_db_spans(req)
        redis_spans = self._port.fetch_redis_spans(req)
        result = BottleneckResult.compute(request=req, db_spans=db_spans, redis_spans=redis_spans)
        return SpanBottleneckAnalysisResponse(
            bottleneck=result.bottleneck.value,
            confidence=result.confidence.value,
            bottleneck_pct_of_total=result.bottleneck_pct_of_total,  # type: ignore
            db_avg_ms=result.db_breakdown.avg_ms if result.db_breakdown else 0.0,  # type: ignore
            redis_avg_ms=result.redis_breakdown.avg_ms if result.redis_breakdown else 1.0,  # type: ignore
            db_slowest=result.db_breakdown.slowest_operation if result.db_breakdown else None,  # type: ignore
            redis_slowest=result.redis_breakdown.slowest_operation  # type: ignore
            if result.redis_breakdown
            else None,
            reasons=result.reasons,  # type: ignore
        )

mutants_xǁSpanBottleneckAnalysisUseCaseǁ__init____mutmut['_mutmut_orig'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁ__init____mutmut['xǁSpanBottleneckAnalysisUseCaseǁ__init____mutmut_1'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['_mutmut_orig'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_1'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_2'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_3'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_4'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_5'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_6'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_7'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_8'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_9'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_10'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_11'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_12'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_13'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_14'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_15'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_16'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_17'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_18'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_19'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_20'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_21'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_22'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_23'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_24'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_25'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_26'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_27'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_28'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_29'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_30'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut['xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_31'] = SpanBottleneckAnalysisUseCase.xǁSpanBottleneckAnalysisUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
