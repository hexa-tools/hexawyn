from __future__ import annotations

from hexawyn.application.ports.driven.metrics_query_port import MetricsQueryPort
from hexawyn.application.use_case.observability.execute_prometheus_query.command import (
    ExecutePrometheusQueryCommand,
)
from hexawyn.application.use_case.observability.execute_prometheus_query.response import (
    ExecutePrometheusQueryResponse,
    MetricResultDict,
)
from hexawyn.domain.models.metrics_query import PrometheusMetricResult, PrometheusQueryResult
from hexawyn.domain.services.metrics_query.result_parser import (
    parse_instant_results,
    parse_range_results,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁPrometheusQueryUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class PrometheusQueryUseCase:
    @_mutmut_mutated(mutants_xǁPrometheusQueryUseCaseǁ__init____mutmut)
    def __init__(self, port: MetricsQueryPort) -> None:
        self._port = port
    def xǁPrometheusQueryUseCaseǁ__init____mutmut_orig(self, port: MetricsQueryPort) -> None:
        self._port = port
    def xǁPrometheusQueryUseCaseǁ__init____mutmut_1(self, port: MetricsQueryPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut)
    def execute(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_orig(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_1(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type != "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_2(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "XXrangeXX":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_3(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "RANGE":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_4(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_5(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "XXrange query requires startXX"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_6(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "RANGE QUERY REQUIRES START"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_7(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_8(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "XXrange query requires endXX"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_9(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "RANGE QUERY REQUIRES END"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_10(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = None
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_11(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                None,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_12(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=None,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_13(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=None,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_14(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=None,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_15(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=None,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_16(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_17(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_18(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_19(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_20(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_21(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = None
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_22(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                None,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_23(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=None,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_24(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=None,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_25(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_26(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_27(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_28(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = None
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_29(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                None, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_30(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=None
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_31(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_32(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_33(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = None
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_34(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                None,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_35(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=None,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_36(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=None,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_37(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_38(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_39(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                )
        return _to_response(result)

    def xǁPrometheusQueryUseCaseǁexecute__mutmut_40(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant,
                promql=command.promql,
                unit_hint=command.unit_hint,  # type: ignore
            )
        return _to_response(None)

mutants_xǁPrometheusQueryUseCaseǁ__init____mutmut['_mutmut_orig'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁ__init____mutmut['xǁPrometheusQueryUseCaseǁ__init____mutmut_1'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['_mutmut_orig'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_1'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_2'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_3'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_4'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_5'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_6'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_7'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_8'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_9'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_10'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_11'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_12'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_13'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_14'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_15'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_16'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_17'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_18'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_19'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_20'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_21'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_22'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_23'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_24'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_25'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_26'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_27'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_28'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_29'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_30'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_31'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_32'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_33'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_34'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_35'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_36'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_37'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_38'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_39'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryUseCaseǁexecute__mutmut['xǁPrometheusQueryUseCaseǁexecute__mutmut_40'] = PrometheusQueryUseCase.xǁPrometheusQueryUseCaseǁexecute__mutmut_40 # type: ignore # mutmut generated
mutants_x__to_response__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_response__mutmut)
def _to_response(result: PrometheusQueryResult) -> ExecutePrometheusQueryResponse:
    return ExecutePrometheusQueryResponse(
        query=result.query,
        query_type=result.query_type,
        results=[_to_result_dict(item) for item in result.results],
        result_count=result.result_count,
        truncated=result.truncated,
        no_data=result.no_data,
        summary=result.summary,
    )


def x__to_response__mutmut_orig(result: PrometheusQueryResult) -> ExecutePrometheusQueryResponse:
    return ExecutePrometheusQueryResponse(
        query=result.query,
        query_type=result.query_type,
        results=[_to_result_dict(item) for item in result.results],
        result_count=result.result_count,
        truncated=result.truncated,
        no_data=result.no_data,
        summary=result.summary,
    )


def x__to_response__mutmut_1(result: PrometheusQueryResult) -> ExecutePrometheusQueryResponse:
    return ExecutePrometheusQueryResponse(
        query=None,
        query_type=result.query_type,
        results=[_to_result_dict(item) for item in result.results],
        result_count=result.result_count,
        truncated=result.truncated,
        no_data=result.no_data,
        summary=result.summary,
    )


def x__to_response__mutmut_2(result: PrometheusQueryResult) -> ExecutePrometheusQueryResponse:
    return ExecutePrometheusQueryResponse(
        query=result.query,
        query_type=None,
        results=[_to_result_dict(item) for item in result.results],
        result_count=result.result_count,
        truncated=result.truncated,
        no_data=result.no_data,
        summary=result.summary,
    )


def x__to_response__mutmut_3(result: PrometheusQueryResult) -> ExecutePrometheusQueryResponse:
    return ExecutePrometheusQueryResponse(
        query=result.query,
        query_type=result.query_type,
        results=None,
        result_count=result.result_count,
        truncated=result.truncated,
        no_data=result.no_data,
        summary=result.summary,
    )


def x__to_response__mutmut_4(result: PrometheusQueryResult) -> ExecutePrometheusQueryResponse:
    return ExecutePrometheusQueryResponse(
        query=result.query,
        query_type=result.query_type,
        results=[_to_result_dict(item) for item in result.results],
        result_count=None,
        truncated=result.truncated,
        no_data=result.no_data,
        summary=result.summary,
    )


def x__to_response__mutmut_5(result: PrometheusQueryResult) -> ExecutePrometheusQueryResponse:
    return ExecutePrometheusQueryResponse(
        query=result.query,
        query_type=result.query_type,
        results=[_to_result_dict(item) for item in result.results],
        result_count=result.result_count,
        truncated=None,
        no_data=result.no_data,
        summary=result.summary,
    )


def x__to_response__mutmut_6(result: PrometheusQueryResult) -> ExecutePrometheusQueryResponse:
    return ExecutePrometheusQueryResponse(
        query=result.query,
        query_type=result.query_type,
        results=[_to_result_dict(item) for item in result.results],
        result_count=result.result_count,
        truncated=result.truncated,
        no_data=None,
        summary=result.summary,
    )


def x__to_response__mutmut_7(result: PrometheusQueryResult) -> ExecutePrometheusQueryResponse:
    return ExecutePrometheusQueryResponse(
        query=result.query,
        query_type=result.query_type,
        results=[_to_result_dict(item) for item in result.results],
        result_count=result.result_count,
        truncated=result.truncated,
        no_data=result.no_data,
        summary=None,
    )


def x__to_response__mutmut_8(result: PrometheusQueryResult) -> ExecutePrometheusQueryResponse:
    return ExecutePrometheusQueryResponse(
        query_type=result.query_type,
        results=[_to_result_dict(item) for item in result.results],
        result_count=result.result_count,
        truncated=result.truncated,
        no_data=result.no_data,
        summary=result.summary,
    )


def x__to_response__mutmut_9(result: PrometheusQueryResult) -> ExecutePrometheusQueryResponse:
    return ExecutePrometheusQueryResponse(
        query=result.query,
        results=[_to_result_dict(item) for item in result.results],
        result_count=result.result_count,
        truncated=result.truncated,
        no_data=result.no_data,
        summary=result.summary,
    )


def x__to_response__mutmut_10(result: PrometheusQueryResult) -> ExecutePrometheusQueryResponse:
    return ExecutePrometheusQueryResponse(
        query=result.query,
        query_type=result.query_type,
        result_count=result.result_count,
        truncated=result.truncated,
        no_data=result.no_data,
        summary=result.summary,
    )


def x__to_response__mutmut_11(result: PrometheusQueryResult) -> ExecutePrometheusQueryResponse:
    return ExecutePrometheusQueryResponse(
        query=result.query,
        query_type=result.query_type,
        results=[_to_result_dict(item) for item in result.results],
        truncated=result.truncated,
        no_data=result.no_data,
        summary=result.summary,
    )


def x__to_response__mutmut_12(result: PrometheusQueryResult) -> ExecutePrometheusQueryResponse:
    return ExecutePrometheusQueryResponse(
        query=result.query,
        query_type=result.query_type,
        results=[_to_result_dict(item) for item in result.results],
        result_count=result.result_count,
        no_data=result.no_data,
        summary=result.summary,
    )


def x__to_response__mutmut_13(result: PrometheusQueryResult) -> ExecutePrometheusQueryResponse:
    return ExecutePrometheusQueryResponse(
        query=result.query,
        query_type=result.query_type,
        results=[_to_result_dict(item) for item in result.results],
        result_count=result.result_count,
        truncated=result.truncated,
        summary=result.summary,
    )


def x__to_response__mutmut_14(result: PrometheusQueryResult) -> ExecutePrometheusQueryResponse:
    return ExecutePrometheusQueryResponse(
        query=result.query,
        query_type=result.query_type,
        results=[_to_result_dict(item) for item in result.results],
        result_count=result.result_count,
        truncated=result.truncated,
        no_data=result.no_data,
        )


def x__to_response__mutmut_15(result: PrometheusQueryResult) -> ExecutePrometheusQueryResponse:
    return ExecutePrometheusQueryResponse(
        query=result.query,
        query_type=result.query_type,
        results=[_to_result_dict(None) for item in result.results],
        result_count=result.result_count,
        truncated=result.truncated,
        no_data=result.no_data,
        summary=result.summary,
    )

mutants_x__to_response__mutmut['_mutmut_orig'] = x__to_response__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_1'] = x__to_response__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_2'] = x__to_response__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_3'] = x__to_response__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_4'] = x__to_response__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_5'] = x__to_response__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_6'] = x__to_response__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_7'] = x__to_response__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_8'] = x__to_response__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_9'] = x__to_response__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_10'] = x__to_response__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_11'] = x__to_response__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_12'] = x__to_response__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_13'] = x__to_response__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_14'] = x__to_response__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_15'] = x__to_response__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_result_dict__mutmut)
def _to_result_dict(item: PrometheusMetricResult) -> MetricResultDict:
    return MetricResultDict(
        labels=item.labels,
        value=item.value,  # type: ignore
        values=item.values,  # type: ignore
        formatted_value=item.formatted_value,
    )


def x__to_result_dict__mutmut_orig(item: PrometheusMetricResult) -> MetricResultDict:
    return MetricResultDict(
        labels=item.labels,
        value=item.value,  # type: ignore
        values=item.values,  # type: ignore
        formatted_value=item.formatted_value,
    )


def x__to_result_dict__mutmut_1(item: PrometheusMetricResult) -> MetricResultDict:
    return MetricResultDict(
        labels=None,
        value=item.value,  # type: ignore
        values=item.values,  # type: ignore
        formatted_value=item.formatted_value,
    )


def x__to_result_dict__mutmut_2(item: PrometheusMetricResult) -> MetricResultDict:
    return MetricResultDict(
        labels=item.labels,
        value=None,  # type: ignore
        values=item.values,  # type: ignore
        formatted_value=item.formatted_value,
    )


def x__to_result_dict__mutmut_3(item: PrometheusMetricResult) -> MetricResultDict:
    return MetricResultDict(
        labels=item.labels,
        value=item.value,  # type: ignore
        values=None,  # type: ignore
        formatted_value=item.formatted_value,
    )


def x__to_result_dict__mutmut_4(item: PrometheusMetricResult) -> MetricResultDict:
    return MetricResultDict(
        labels=item.labels,
        value=item.value,  # type: ignore
        values=item.values,  # type: ignore
        formatted_value=None,
    )


def x__to_result_dict__mutmut_5(item: PrometheusMetricResult) -> MetricResultDict:
    return MetricResultDict(
        value=item.value,  # type: ignore
        values=item.values,  # type: ignore
        formatted_value=item.formatted_value,
    )


def x__to_result_dict__mutmut_6(item: PrometheusMetricResult) -> MetricResultDict:
    return MetricResultDict(
        labels=item.labels,
        values=item.values,  # type: ignore
        formatted_value=item.formatted_value,
    )


def x__to_result_dict__mutmut_7(item: PrometheusMetricResult) -> MetricResultDict:
    return MetricResultDict(
        labels=item.labels,
        value=item.value,  # type: ignore
        formatted_value=item.formatted_value,
    )


def x__to_result_dict__mutmut_8(item: PrometheusMetricResult) -> MetricResultDict:
    return MetricResultDict(
        labels=item.labels,
        value=item.value,  # type: ignore
        values=item.values,  # type: ignore
        )

mutants_x__to_result_dict__mutmut['_mutmut_orig'] = x__to_result_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_1'] = x__to_result_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_2'] = x__to_result_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_3'] = x__to_result_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_4'] = x__to_result_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_5'] = x__to_result_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_6'] = x__to_result_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_7'] = x__to_result_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_8'] = x__to_result_dict__mutmut_8 # type: ignore # mutmut generated
