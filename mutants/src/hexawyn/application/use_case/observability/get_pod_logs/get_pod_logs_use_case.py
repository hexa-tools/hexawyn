from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.use_case.observability.get_pod_logs.command import (
    GetPodLogsUseCaseCommand,
)
from hexawyn.application.use_case.observability.get_pod_logs.response import (
    GetPodLogsUseCaseResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGetPodLogsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class GetPodLogsUseCase:
    """Retrieves logs for a specific pod."""

    @_mutmut_mutated(mutants_xǁGetPodLogsUseCaseǁ__init____mutmut)
    def __init__(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port

    def xǁGetPodLogsUseCaseǁ__init____mutmut_orig(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port

    def xǁGetPodLogsUseCaseǁ__init____mutmut_1(self, k8s_port: K8sPort) -> None:
        self._k8s = None

    @_mutmut_mutated(mutants_xǁGetPodLogsUseCaseǁexecute__mutmut)
    def execute(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_orig(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_1(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = None
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_2(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(None)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_3(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=None,
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_4(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=None,
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_5(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=None,
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_6(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_7(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_8(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_9(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace and "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_10(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "XXXX",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_11(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "XXnameXX": p.get("name", ""),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_12(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "NAME": p.get("name", ""),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_13(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get(None, ""),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_14(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", None),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_15(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get(""),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_16(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_17(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("XXnameXX", ""),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_18(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("NAME", ""),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_19(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", "XXXX"),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_20(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "XXstatusXX": p.get("status", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_21(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "STATUS": p.get("status", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_22(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get(None, ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_23(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("status", None),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_24(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get(""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_25(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("status", ),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_26(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("XXstatusXX", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_27(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("STATUS", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_28(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("status", "XXXX"),
                    "restarts": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_29(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("status", ""),
                    "XXrestartsXX": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_30(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("status", ""),
                    "RESTARTS": p.get("restarts", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_31(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("status", ""),
                    "restarts": p.get(None, 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_32(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", None),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_33(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("status", ""),
                    "restarts": p.get(0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_34(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", ),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_35(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("status", ""),
                    "restarts": p.get("XXrestartsXX", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_36(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("status", ""),
                    "restarts": p.get("RESTARTS", 0),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

    def xǁGetPodLogsUseCaseǁexecute__mutmut_37(self, command: GetPodLogsUseCaseCommand) -> GetPodLogsUseCaseResponse:
        pods = self._k8s.list_pods(command.namespace)
        return GetPodLogsUseCaseResponse(
            namespace=command.namespace or "",
            pods=[
                {
                    "name": p.get("name", ""),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", 1),
                }
                for p in pods
            ],
            total_pods=len(pods),
        )

mutants_xǁGetPodLogsUseCaseǁ__init____mutmut['_mutmut_orig'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁ__init____mutmut['xǁGetPodLogsUseCaseǁ__init____mutmut_1'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['_mutmut_orig'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_1'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_2'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_3'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_4'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_5'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_6'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_7'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_8'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_9'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_10'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_11'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_12'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_13'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_14'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_15'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_16'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_17'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_18'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_19'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_20'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_21'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_22'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_23'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_24'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_25'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_26'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_27'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_28'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_29'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_30'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_31'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_32'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_33'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_34'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_35'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_36'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGetPodLogsUseCaseǁexecute__mutmut['xǁGetPodLogsUseCaseǁexecute__mutmut_37'] = GetPodLogsUseCase.xǁGetPodLogsUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
