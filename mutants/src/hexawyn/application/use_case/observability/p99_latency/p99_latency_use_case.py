from __future__ import annotations

from hexawyn.application.ports.driven.latency_percentile_port import LatencyPercentilePort
from hexawyn.application.use_case.observability.p99_latency.command import P99LatencyCommand
from hexawyn.application.use_case.observability.p99_latency.response import P99LatencyResponse
from hexawyn.domain.models.p99_latency import LatencyPercentileRequest, P99Result


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁP99LatencyUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁP99LatencyUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class P99LatencyUseCase:
    @_mutmut_mutated(mutants_xǁP99LatencyUseCaseǁ__init____mutmut)
    def __init__(self, port: LatencyPercentilePort) -> None:
        self._port = port
    def xǁP99LatencyUseCaseǁ__init____mutmut_orig(self, port: LatencyPercentilePort) -> None:
        self._port = port
    def xǁP99LatencyUseCaseǁ__init____mutmut_1(self, port: LatencyPercentilePort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁP99LatencyUseCaseǁexecute__mutmut)
    def execute(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_orig(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_1(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = None
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_2(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=None,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_3(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=None,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_4(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=None,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_5(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_6(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_7(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_8(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = None
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_9(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(None)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_10(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = None
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_11(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=None, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_12(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=None)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_13(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_14(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, )
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_15(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=None,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_16(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=None,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_17(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=None,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_18(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=None,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_19(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=None,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_20(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=None,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_21(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=None,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_22(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=None,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_23(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=None,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_24(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_25(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_26(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_27(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_28(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_29(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_30(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_31(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            sample_count=r.sample_count,
        )

    def xǁP99LatencyUseCaseǁexecute__mutmut_32(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            )

mutants_xǁP99LatencyUseCaseǁ__init____mutmut['_mutmut_orig'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁ__init____mutmut['xǁP99LatencyUseCaseǁ__init____mutmut_1'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁP99LatencyUseCaseǁexecute__mutmut['_mutmut_orig'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_1'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_2'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_3'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_4'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_5'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_6'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_7'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_8'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_9'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_10'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_11'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_12'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_13'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_14'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_15'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_16'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_17'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_18'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_19'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_20'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_21'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_22'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_23'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_24'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_25'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_26'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_27'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_28'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_29'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_30'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_31'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁP99LatencyUseCaseǁexecute__mutmut['xǁP99LatencyUseCaseǁexecute__mutmut_32'] = P99LatencyUseCase.xǁP99LatencyUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
