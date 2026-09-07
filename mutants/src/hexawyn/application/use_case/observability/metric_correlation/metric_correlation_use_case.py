from __future__ import annotations

from hexawyn.application.ports.driven.metric_correlation_port import MetricCorrelationPort
from hexawyn.application.use_case.observability.metric_correlation.command import (
    MetricCorrelationCommand,
)
from hexawyn.application.use_case.observability.metric_correlation.response import (
    MetricCorrelationResponse,
)
from hexawyn.domain.models.metric_correlation import CorrelationRequest, CorrelationResult


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁMetricCorrelationUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class MetricCorrelationUseCase:
    @_mutmut_mutated(mutants_xǁMetricCorrelationUseCaseǁ__init____mutmut)
    def __init__(self, port: MetricCorrelationPort) -> None:
        self._port = port
    def xǁMetricCorrelationUseCaseǁ__init____mutmut_orig(self, port: MetricCorrelationPort) -> None:
        self._port = port
    def xǁMetricCorrelationUseCaseǁ__init____mutmut_1(self, port: MetricCorrelationPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut)
    def execute(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_orig(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_1(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = None
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_2(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=None,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_3(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=None,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_4(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=None,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_5(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_6(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_7(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_8(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = None
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_9(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(None)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_10(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = None
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_11(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(None)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_12(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = None
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_13(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=None, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_14(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=None, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_15(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=None)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_16(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_17(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_18(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, )
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_19(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=None,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_20(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=None,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_21(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=None,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_22(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=None,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_23(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=None,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_24(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=None,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_25(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=None,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_26(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_27(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_28(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_29(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_30(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            hypothesis=r.hypothesis,
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_31(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            data_point_count=r.data_point_count,
        )

    def xǁMetricCorrelationUseCaseǁexecute__mutmut_32(self, command: MetricCorrelationCommand) -> MetricCorrelationResponse:
        req = CorrelationRequest(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            time_window_minutes=command.time_window_minutes,
        )
        a = self._port.fetch_primary_series(req)
        b = self._port.fetch_correlated_series(req)
        r = CorrelationResult.compute(request=req, series_a=a, series_b=b)
        return MetricCorrelationResponse(
            primary_service=command.primary_service,
            correlated_service=command.correlated_service,
            status=r.status.value,
            coefficient=r.coefficient,  # type: ignore
            lag_index=r.lag_index,  # type: ignore
            hypothesis=r.hypothesis,
            )

mutants_xǁMetricCorrelationUseCaseǁ__init____mutmut['_mutmut_orig'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁ__init____mutmut['xǁMetricCorrelationUseCaseǁ__init____mutmut_1'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['_mutmut_orig'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_1'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_2'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_3'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_4'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_5'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_6'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_7'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_8'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_9'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_10'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_11'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_12'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_13'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_14'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_15'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_16'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_17'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_18'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_19'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_20'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_21'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_22'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_23'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_24'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_25'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_26'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_27'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_28'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_29'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_30'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_31'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁMetricCorrelationUseCaseǁexecute__mutmut['xǁMetricCorrelationUseCaseǁexecute__mutmut_32'] = MetricCorrelationUseCase.xǁMetricCorrelationUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
