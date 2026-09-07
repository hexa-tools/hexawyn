from __future__ import annotations

from hexawyn.application.ports.driven.metrics_query_port import MetricsQueryPort
from hexawyn.application.use_case.observability.execute_prometheus_query.command import (
    ExecutePrometheusQueryCommand,
)
from hexawyn.application.use_case.observability.execute_prometheus_query.response import (
    ExecutePrometheusQueryResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁExecutePrometheusQueryUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ExecutePrometheusQueryUseCase:
    @_mutmut_mutated(mutants_xǁExecutePrometheusQueryUseCaseǁ__init____mutmut)
    def __init__(self, port: MetricsQueryPort) -> None:
        self._port = port
    def xǁExecutePrometheusQueryUseCaseǁ__init____mutmut_orig(self, port: MetricsQueryPort) -> None:
        self._port = port
    def xǁExecutePrometheusQueryUseCaseǁ__init____mutmut_1(self, port: MetricsQueryPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut)
    def execute(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_orig(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_1(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = None
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_2(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=None,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_3(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=None,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_4(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=None,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_5(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=None,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_6(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_7(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_8(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_9(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_10(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=None,
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_11(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=None,
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_12(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=None,
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_13(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_14(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_15(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_16(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(None),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_17(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get(None, "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_18(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", None)),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_19(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_20(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", )),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_21(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("XXstatusXX", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_22(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("STATUS", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_23(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "XXXX")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_24(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(None),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_25(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get(None, "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_26(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", None)),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_27(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_28(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", )),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_29(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get(None, {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_30(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", None).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_31(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get({}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_32(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", ).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_33(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("XXdataXX", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_34(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("DATA", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_35(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("XXresultTypeXX", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_36(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resulttype", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_37(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("RESULTTYPE", "")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_38(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "XXXX")),
            results=result.get("data", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_39(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get(None, []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_40(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", None),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_41(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get([]),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_42(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", ),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_43(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get(None, {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_44(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", None).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_45(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get({}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_46(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", ).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_47(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("XXdataXX", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_48(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("DATA", {}).get("result", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_49(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("XXresultXX", []),
        )

    def xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_50(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("RESULT", []),
        )

mutants_xǁExecutePrometheusQueryUseCaseǁ__init____mutmut['_mutmut_orig'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁ__init____mutmut['xǁExecutePrometheusQueryUseCaseǁ__init____mutmut_1'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['_mutmut_orig'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_1'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_2'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_3'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_4'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_5'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_6'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_7'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_8'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_9'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_10'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_11'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_12'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_13'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_14'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_15'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_16'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_17'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_18'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_19'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_20'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_21'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_22'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_23'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_24'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_25'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_26'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_27'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_28'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_29'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_30'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_31'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_32'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_33'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_34'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_35'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_36'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_37'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_38'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_39'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_40'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_41'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_42'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_43'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_44'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_45'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_46'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_47'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_48'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_48 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_49'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_49 # type: ignore # mutmut generated
mutants_xǁExecutePrometheusQueryUseCaseǁexecute__mutmut['xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_50'] = ExecutePrometheusQueryUseCase.xǁExecutePrometheusQueryUseCaseǁexecute__mutmut_50 # type: ignore # mutmut generated
