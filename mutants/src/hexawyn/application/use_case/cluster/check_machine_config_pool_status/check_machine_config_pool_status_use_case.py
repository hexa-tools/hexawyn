from __future__ import annotations

from hexawyn.application.ports.driven.machine_config_pool_port import (
    MachineConfigPoolPort,
)
from hexawyn.application.use_case.cluster.check_machine_config_pool_status.command import (  # noqa: E501
    CheckMachineConfigPoolStatusCommand,
)
from hexawyn.application.use_case.cluster.check_machine_config_pool_status.response import (  # noqa: E501
    CheckMachineConfigPoolStatusResponse,
)
from hexawyn.domain.services.machine_config_pool_status.machine_config_pool_status_service import (  # noqa: E501
    MachineConfigPoolStatusService,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCheckMachineConfigPoolStatusUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCheckMachineConfigPoolStatusUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CheckMachineConfigPoolStatusUseCase:
    @_mutmut_mutated(mutants_xǁCheckMachineConfigPoolStatusUseCaseǁ__init____mutmut)
    def __init__(self, machine_config_pool_port: MachineConfigPoolPort) -> None:
        self._port = machine_config_pool_port
        self._engine = MachineConfigPoolStatusService()
    def xǁCheckMachineConfigPoolStatusUseCaseǁ__init____mutmut_orig(self, machine_config_pool_port: MachineConfigPoolPort) -> None:
        self._port = machine_config_pool_port
        self._engine = MachineConfigPoolStatusService()
    def xǁCheckMachineConfigPoolStatusUseCaseǁ__init____mutmut_1(self, machine_config_pool_port: MachineConfigPoolPort) -> None:
        self._port = None
        self._engine = MachineConfigPoolStatusService()
    def xǁCheckMachineConfigPoolStatusUseCaseǁ__init____mutmut_2(self, machine_config_pool_port: MachineConfigPoolPort) -> None:
        self._port = machine_config_pool_port
        self._engine = None

    @_mutmut_mutated(mutants_xǁCheckMachineConfigPoolStatusUseCaseǁexecute__mutmut)
    def execute(
        self, command: CheckMachineConfigPoolStatusCommand
    ) -> CheckMachineConfigPoolStatusResponse:
        pools = self._port.list_machine_config_pools()
        result = self._engine.evaluate(pools)
        return CheckMachineConfigPoolStatusResponse(result=result)

    def xǁCheckMachineConfigPoolStatusUseCaseǁexecute__mutmut_orig(
        self, command: CheckMachineConfigPoolStatusCommand
    ) -> CheckMachineConfigPoolStatusResponse:
        pools = self._port.list_machine_config_pools()
        result = self._engine.evaluate(pools)
        return CheckMachineConfigPoolStatusResponse(result=result)

    def xǁCheckMachineConfigPoolStatusUseCaseǁexecute__mutmut_1(
        self, command: CheckMachineConfigPoolStatusCommand
    ) -> CheckMachineConfigPoolStatusResponse:
        pools = None
        result = self._engine.evaluate(pools)
        return CheckMachineConfigPoolStatusResponse(result=result)

    def xǁCheckMachineConfigPoolStatusUseCaseǁexecute__mutmut_2(
        self, command: CheckMachineConfigPoolStatusCommand
    ) -> CheckMachineConfigPoolStatusResponse:
        pools = self._port.list_machine_config_pools()
        result = None
        return CheckMachineConfigPoolStatusResponse(result=result)

    def xǁCheckMachineConfigPoolStatusUseCaseǁexecute__mutmut_3(
        self, command: CheckMachineConfigPoolStatusCommand
    ) -> CheckMachineConfigPoolStatusResponse:
        pools = self._port.list_machine_config_pools()
        result = self._engine.evaluate(None)
        return CheckMachineConfigPoolStatusResponse(result=result)

    def xǁCheckMachineConfigPoolStatusUseCaseǁexecute__mutmut_4(
        self, command: CheckMachineConfigPoolStatusCommand
    ) -> CheckMachineConfigPoolStatusResponse:
        pools = self._port.list_machine_config_pools()
        result = self._engine.evaluate(pools)
        return CheckMachineConfigPoolStatusResponse(result=None)

mutants_xǁCheckMachineConfigPoolStatusUseCaseǁ__init____mutmut['_mutmut_orig'] = CheckMachineConfigPoolStatusUseCase.xǁCheckMachineConfigPoolStatusUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCheckMachineConfigPoolStatusUseCaseǁ__init____mutmut['xǁCheckMachineConfigPoolStatusUseCaseǁ__init____mutmut_1'] = CheckMachineConfigPoolStatusUseCase.xǁCheckMachineConfigPoolStatusUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁCheckMachineConfigPoolStatusUseCaseǁ__init____mutmut['xǁCheckMachineConfigPoolStatusUseCaseǁ__init____mutmut_2'] = CheckMachineConfigPoolStatusUseCase.xǁCheckMachineConfigPoolStatusUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁCheckMachineConfigPoolStatusUseCaseǁexecute__mutmut['_mutmut_orig'] = CheckMachineConfigPoolStatusUseCase.xǁCheckMachineConfigPoolStatusUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCheckMachineConfigPoolStatusUseCaseǁexecute__mutmut['xǁCheckMachineConfigPoolStatusUseCaseǁexecute__mutmut_1'] = CheckMachineConfigPoolStatusUseCase.xǁCheckMachineConfigPoolStatusUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCheckMachineConfigPoolStatusUseCaseǁexecute__mutmut['xǁCheckMachineConfigPoolStatusUseCaseǁexecute__mutmut_2'] = CheckMachineConfigPoolStatusUseCase.xǁCheckMachineConfigPoolStatusUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCheckMachineConfigPoolStatusUseCaseǁexecute__mutmut['xǁCheckMachineConfigPoolStatusUseCaseǁexecute__mutmut_3'] = CheckMachineConfigPoolStatusUseCase.xǁCheckMachineConfigPoolStatusUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCheckMachineConfigPoolStatusUseCaseǁexecute__mutmut['xǁCheckMachineConfigPoolStatusUseCaseǁexecute__mutmut_4'] = CheckMachineConfigPoolStatusUseCase.xǁCheckMachineConfigPoolStatusUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
