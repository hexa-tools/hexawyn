from __future__ import annotations

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.use_case.keda.keda_scaledjob_get.command import (
    KedaScaledjobGetCommand,
)
from hexawyn.application.use_case.keda.keda_scaledjob_get.response import (
    KedaScaledjobGetResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKedaScaledjobGetUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class KedaScaledjobGetUseCase:
    @_mutmut_mutated(mutants_xǁKedaScaledjobGetUseCaseǁ__init____mutmut)
    def __init__(self, port: KedaPort) -> None:
        self._port = port
    def xǁKedaScaledjobGetUseCaseǁ__init____mutmut_orig(self, port: KedaPort) -> None:
        self._port = port
    def xǁKedaScaledjobGetUseCaseǁ__init____mutmut_1(self, port: KedaPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut)
    def execute(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=j.namespace,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_orig(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=j.namespace,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_1(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = None
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=j.namespace,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_2(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=None, namespace=command.namespace)
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=j.namespace,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_3(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=None)
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=j.namespace,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_4(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(namespace=command.namespace)
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=j.namespace,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_5(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, )
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=j.namespace,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_6(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledjobGetResponse(
            name=None,
            namespace=j.namespace,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_7(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=None,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_8(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=j.namespace,
            phase=None,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_9(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=j.namespace,
            phase=j.phase.value,
            successful_jobs=None,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_10(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=j.namespace,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            failed_jobs=None,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_11(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=j.namespace,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            last_execution_time=None,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_12(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=j.namespace,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=None,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_13(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=j.namespace,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=None,
            max_replica_count=j.max_replica_count,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_14(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=j.namespace,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=None,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_15(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=j.namespace,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            message=None,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_16(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledjobGetResponse(
            namespace=j.namespace,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_17(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledjobGetResponse(
            name=j.name,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_18(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=j.namespace,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_19(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=j.namespace,
            phase=j.phase.value,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_20(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=j.namespace,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_21(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=j.namespace,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_22(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=j.namespace,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_23(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=j.namespace,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            max_replica_count=j.max_replica_count,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_24(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=j.namespace,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            message=j.message,  # type: ignore
        )

    def xǁKedaScaledjobGetUseCaseǁexecute__mutmut_25(self, command: KedaScaledjobGetCommand) -> KedaScaledjobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledjobGetResponse(
            name=j.name,
            namespace=j.namespace,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            )

mutants_xǁKedaScaledjobGetUseCaseǁ__init____mutmut['_mutmut_orig'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁ__init____mutmut['xǁKedaScaledjobGetUseCaseǁ__init____mutmut_1'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['_mutmut_orig'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_1'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_2'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_3'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_4'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_5'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_6'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_7'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_8'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_9'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_10'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_11'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_12'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_13'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_14'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_15'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_16'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_17'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_18'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_19'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_20'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_21'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_22'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_23'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_24'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKedaScaledjobGetUseCaseǁexecute__mutmut['xǁKedaScaledjobGetUseCaseǁexecute__mutmut_25'] = KedaScaledjobGetUseCase.xǁKedaScaledjobGetUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
