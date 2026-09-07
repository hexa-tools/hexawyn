from __future__ import annotations

from hexawyn.application.ports.driven.cluster_operator_status_port import (
    ClusterOperatorStatusPort,
)
from hexawyn.application.use_case.cluster.check_cluster_operator_health.command import (  # noqa: E501
    CheckClusterOperatorHealthCommand,
)
from hexawyn.application.use_case.cluster.check_cluster_operator_health.response import (  # noqa: E501
    CheckClusterOperatorHealthResponse,
)
from hexawyn.domain.services.cluster_operator_health.cluster_operator_health_service import (
    ClusterOperatorHealthService,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCheckClusterOperatorHealthUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCheckClusterOperatorHealthUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CheckClusterOperatorHealthUseCase:
    @_mutmut_mutated(mutants_xǁCheckClusterOperatorHealthUseCaseǁ__init____mutmut)
    def __init__(self, operator_port: ClusterOperatorStatusPort) -> None:
        self._port = operator_port
        self._engine = ClusterOperatorHealthService()
    def xǁCheckClusterOperatorHealthUseCaseǁ__init____mutmut_orig(self, operator_port: ClusterOperatorStatusPort) -> None:
        self._port = operator_port
        self._engine = ClusterOperatorHealthService()
    def xǁCheckClusterOperatorHealthUseCaseǁ__init____mutmut_1(self, operator_port: ClusterOperatorStatusPort) -> None:
        self._port = None
        self._engine = ClusterOperatorHealthService()
    def xǁCheckClusterOperatorHealthUseCaseǁ__init____mutmut_2(self, operator_port: ClusterOperatorStatusPort) -> None:
        self._port = operator_port
        self._engine = None

    @_mutmut_mutated(mutants_xǁCheckClusterOperatorHealthUseCaseǁexecute__mutmut)
    def execute(
        self, command: CheckClusterOperatorHealthCommand
    ) -> CheckClusterOperatorHealthResponse:
        operators = self._port.list_cluster_operators()
        result = self._engine.evaluate(operators)
        return CheckClusterOperatorHealthResponse(result=result)

    def xǁCheckClusterOperatorHealthUseCaseǁexecute__mutmut_orig(
        self, command: CheckClusterOperatorHealthCommand
    ) -> CheckClusterOperatorHealthResponse:
        operators = self._port.list_cluster_operators()
        result = self._engine.evaluate(operators)
        return CheckClusterOperatorHealthResponse(result=result)

    def xǁCheckClusterOperatorHealthUseCaseǁexecute__mutmut_1(
        self, command: CheckClusterOperatorHealthCommand
    ) -> CheckClusterOperatorHealthResponse:
        operators = None
        result = self._engine.evaluate(operators)
        return CheckClusterOperatorHealthResponse(result=result)

    def xǁCheckClusterOperatorHealthUseCaseǁexecute__mutmut_2(
        self, command: CheckClusterOperatorHealthCommand
    ) -> CheckClusterOperatorHealthResponse:
        operators = self._port.list_cluster_operators()
        result = None
        return CheckClusterOperatorHealthResponse(result=result)

    def xǁCheckClusterOperatorHealthUseCaseǁexecute__mutmut_3(
        self, command: CheckClusterOperatorHealthCommand
    ) -> CheckClusterOperatorHealthResponse:
        operators = self._port.list_cluster_operators()
        result = self._engine.evaluate(None)
        return CheckClusterOperatorHealthResponse(result=result)

    def xǁCheckClusterOperatorHealthUseCaseǁexecute__mutmut_4(
        self, command: CheckClusterOperatorHealthCommand
    ) -> CheckClusterOperatorHealthResponse:
        operators = self._port.list_cluster_operators()
        result = self._engine.evaluate(operators)
        return CheckClusterOperatorHealthResponse(result=None)

mutants_xǁCheckClusterOperatorHealthUseCaseǁ__init____mutmut['_mutmut_orig'] = CheckClusterOperatorHealthUseCase.xǁCheckClusterOperatorHealthUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCheckClusterOperatorHealthUseCaseǁ__init____mutmut['xǁCheckClusterOperatorHealthUseCaseǁ__init____mutmut_1'] = CheckClusterOperatorHealthUseCase.xǁCheckClusterOperatorHealthUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁCheckClusterOperatorHealthUseCaseǁ__init____mutmut['xǁCheckClusterOperatorHealthUseCaseǁ__init____mutmut_2'] = CheckClusterOperatorHealthUseCase.xǁCheckClusterOperatorHealthUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁCheckClusterOperatorHealthUseCaseǁexecute__mutmut['_mutmut_orig'] = CheckClusterOperatorHealthUseCase.xǁCheckClusterOperatorHealthUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCheckClusterOperatorHealthUseCaseǁexecute__mutmut['xǁCheckClusterOperatorHealthUseCaseǁexecute__mutmut_1'] = CheckClusterOperatorHealthUseCase.xǁCheckClusterOperatorHealthUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCheckClusterOperatorHealthUseCaseǁexecute__mutmut['xǁCheckClusterOperatorHealthUseCaseǁexecute__mutmut_2'] = CheckClusterOperatorHealthUseCase.xǁCheckClusterOperatorHealthUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCheckClusterOperatorHealthUseCaseǁexecute__mutmut['xǁCheckClusterOperatorHealthUseCaseǁexecute__mutmut_3'] = CheckClusterOperatorHealthUseCase.xǁCheckClusterOperatorHealthUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCheckClusterOperatorHealthUseCaseǁexecute__mutmut['xǁCheckClusterOperatorHealthUseCaseǁexecute__mutmut_4'] = CheckClusterOperatorHealthUseCase.xǁCheckClusterOperatorHealthUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
