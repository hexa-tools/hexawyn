from __future__ import annotations

from hexawyn.application.ports.driven.canary_comparison_port import CanaryComparisonPort
from hexawyn.application.use_case.pipelines.canary_comparison.command import (
    CanaryComparisonCommand,
)
from hexawyn.application.use_case.pipelines.canary_comparison.response import (
    CanaryComparisonResponse,
)
from hexawyn.domain.models.canary_comparison import CanaryComparisonRequest, ComparisonResult


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCanaryComparisonUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CanaryComparisonUseCase:
    @_mutmut_mutated(mutants_xǁCanaryComparisonUseCaseǁ__init____mutmut)
    def __init__(self, port: CanaryComparisonPort) -> None:
        self._port = port
    def xǁCanaryComparisonUseCaseǁ__init____mutmut_orig(self, port: CanaryComparisonPort) -> None:
        self._port = port
    def xǁCanaryComparisonUseCaseǁ__init____mutmut_1(self, port: CanaryComparisonPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut)
    def execute(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_orig(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_1(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = None
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_2(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=None,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_3(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=None,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_4(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=None,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_5(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_6(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_7(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_8(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = None
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_9(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(None)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_10(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = None
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_11(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(None)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_12(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = None
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_13(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=None,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_14(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=None,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_15(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=None,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_16(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=None,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_17(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_18(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_19(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_20(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_21(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=None,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_22(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=None,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_23(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=None,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_24(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=None,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_25(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=None,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_26(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=None,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_27(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=None,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_28(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=None,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_29(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=None,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_30(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=None,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_31(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=None,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_32(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_33(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_34(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_35(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_36(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_37(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_38(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_39(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_40(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_41(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            reasons=result.reasons,
        )

    def xǁCanaryComparisonUseCaseǁexecute__mutmut_42(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            )

mutants_xǁCanaryComparisonUseCaseǁ__init____mutmut['_mutmut_orig'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁ__init____mutmut['xǁCanaryComparisonUseCaseǁ__init____mutmut_1'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['_mutmut_orig'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_1'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_2'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_3'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_4'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_5'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_6'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_7'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_8'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_9'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_10'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_11'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_12'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_13'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_14'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_15'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_16'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_17'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_18'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_19'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_20'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_21'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_22'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_23'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_24'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_25'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_26'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_27'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_28'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_29'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_30'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_31'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_32'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_33'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_34'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_35'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_36'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_37'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_38'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_39'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_40'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_41'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁCanaryComparisonUseCaseǁexecute__mutmut['xǁCanaryComparisonUseCaseǁexecute__mutmut_42'] = CanaryComparisonUseCase.xǁCanaryComparisonUseCaseǁexecute__mutmut_42 # type: ignore # mutmut generated
