from hexawyn.application.ports.driven.pod_resource_metrics_port import PodResourceMetricsPort
from hexawyn.application.use_case.cluster.check_resource_constraints.command import (
    CheckResourceConstraintsCommand,
)
from hexawyn.application.use_case.cluster.check_resource_constraints.response import (
    CheckResourceConstraintsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCheckResourceConstraintsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CheckResourceConstraintsUseCase:
    @_mutmut_mutated(mutants_xǁCheckResourceConstraintsUseCaseǁ__init____mutmut)
    def __init__(self, port: PodResourceMetricsPort) -> None:
        self._port = port
    def xǁCheckResourceConstraintsUseCaseǁ__init____mutmut_orig(self, port: PodResourceMetricsPort) -> None:
        self._port = port
    def xǁCheckResourceConstraintsUseCaseǁ__init____mutmut_1(self, port: PodResourceMetricsPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut)
    def execute(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 0) > 0 or r.get("memory_limit_mib", 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_orig(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 0) > 0 or r.get("memory_limit_mib", 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_1(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = None  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 0) > 0 or r.get("memory_limit_mib", 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_2(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = None
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_3(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 0) > 0 and r.get("memory_limit_mib", 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_4(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get(None, 0) > 0 or r.get("memory_limit_mib", 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_5(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", None) > 0 or r.get("memory_limit_mib", 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_6(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get(0) > 0 or r.get("memory_limit_mib", 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_7(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", ) > 0 or r.get("memory_limit_mib", 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_8(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("XXcpu_limit_millicoresXX", 0) > 0 or r.get("memory_limit_mib", 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_9(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("CPU_LIMIT_MILLICORES", 0) > 0 or r.get("memory_limit_mib", 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_10(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 1) > 0 or r.get("memory_limit_mib", 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_11(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 0) >= 0 or r.get("memory_limit_mib", 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_12(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 0) > 1 or r.get("memory_limit_mib", 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_13(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 0) > 0 or r.get(None, 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_14(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 0) > 0 or r.get("memory_limit_mib", None) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_15(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 0) > 0 or r.get(0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_16(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 0) > 0 or r.get("memory_limit_mib", ) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_17(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 0) > 0 or r.get("XXmemory_limit_mibXX", 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_18(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 0) > 0 or r.get("MEMORY_LIMIT_MIB", 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_19(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 0) > 0 or r.get("memory_limit_mib", 1) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_20(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 0) > 0 or r.get("memory_limit_mib", 0) >= 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_21(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 0) > 0 or r.get("memory_limit_mib", 0) > 1  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_22(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 0) > 0 or r.get("memory_limit_mib", 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report=None
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_23(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 0) > 0 or r.get("memory_limit_mib", 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "XXtotal_containersXX": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_24(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 0) > 0 or r.get("memory_limit_mib", 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "TOTAL_CONTAINERS": len(resources),
                "constrained_containers": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_25(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 0) > 0 or r.get("memory_limit_mib", 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "XXconstrained_containersXX": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_26(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 0) > 0 or r.get("memory_limit_mib", 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "CONSTRAINED_CONTAINERS": len(constrained),
                "containers": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_27(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 0) > 0 or r.get("memory_limit_mib", 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "XXcontainersXX": constrained,
            }
        )

    def xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_28(self, command: CheckResourceConstraintsCommand) -> CheckResourceConstraintsResponse:
        resources = self._port.list_container_resources()  # type: ignore
        constrained = [
            r
            for r in resources
            if r.get("cpu_limit_millicores", 0) > 0 or r.get("memory_limit_mib", 0) > 0  # type: ignore
        ]
        return CheckResourceConstraintsResponse(
            report={  # type: ignore
                "total_containers": len(resources),
                "constrained_containers": len(constrained),
                "CONTAINERS": constrained,
            }
        )

mutants_xǁCheckResourceConstraintsUseCaseǁ__init____mutmut['_mutmut_orig'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁ__init____mutmut['xǁCheckResourceConstraintsUseCaseǁ__init____mutmut_1'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['_mutmut_orig'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_1'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_2'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_3'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_4'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_5'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_6'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_7'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_8'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_9'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_10'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_11'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_12'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_13'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_14'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_15'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_16'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_17'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_18'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_19'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_20'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_21'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_22'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_23'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_24'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_25'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_26'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_27'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁCheckResourceConstraintsUseCaseǁexecute__mutmut['xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_28'] = CheckResourceConstraintsUseCase.xǁCheckResourceConstraintsUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
