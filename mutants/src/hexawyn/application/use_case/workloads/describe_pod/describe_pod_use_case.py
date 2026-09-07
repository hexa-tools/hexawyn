from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.use_case.workloads.describe_pod.command import (
    DescribePodCommand,
)
from hexawyn.application.use_case.workloads.describe_pod.response import (
    DescribePodResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDescribePodUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDescribePodUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class DescribePodUseCase:
    @_mutmut_mutated(mutants_xǁDescribePodUseCaseǁ__init____mutmut)
    def __init__(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port
    def xǁDescribePodUseCaseǁ__init____mutmut_orig(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port
    def xǁDescribePodUseCaseǁ__init____mutmut_1(self, k8s_port: K8sPort) -> None:
        self._k8s = None

    @_mutmut_mutated(mutants_xǁDescribePodUseCaseǁexecute__mutmut)
    def execute(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_orig(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_1(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = None
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_2(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=None)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_3(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = None
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_4(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get(None) == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_5(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("XXnameXX") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_6(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("NAME") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_7(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") != pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_8(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=None,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_9(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=None,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_10(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=None,
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_11(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=None,
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_12(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=None,
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_13(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=None,
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_14(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_15(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_16(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_17(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_18(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_19(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_20(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(None),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_21(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get(None, "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_22(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", None)),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_23(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_24(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", )),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_25(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("XXstatusXX", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_26(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("STATUS", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_27(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "XXXX")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_28(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(None),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_29(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get(None, 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_30(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", None)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_31(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get(0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_32(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", )),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_33(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("XXrestartsXX", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_34(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("RESTARTS", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_35(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 1)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_36(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(None),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_37(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get(None, "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_38(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", None)),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_39(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_40(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", )),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_41(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("XXnodeXX", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_42(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("NODE", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_43(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "XXXX")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_44(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(None),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_45(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get(None, "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_46(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", None)),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_47(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_48(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", )),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_49(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("XXageXX", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_50(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("AGE", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_51(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "XXXX")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_52(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=None,
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_53(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=None,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_54(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status=None,
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_55(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            namespace=command.namespace,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_56(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            status="NotFound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_57(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            )

    def xǁDescribePodUseCaseǁexecute__mutmut_58(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="XXNotFoundXX",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_59(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="notfound",
        )

    def xǁDescribePodUseCaseǁexecute__mutmut_60(self, command: DescribePodCommand) -> DescribePodResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        pod_name = command.pod_name
        for pod in pods:
            if pod.get("name") == pod_name:
                return DescribePodResponse(
                    pod_name=pod_name,
                    namespace=command.namespace,
                    status=str(pod.get("status", "")),
                    restarts=int(pod.get("restarts", 0)),
                    node=str(pod.get("node", "")),
                    age=str(pod.get("age", "")),
                )
        return DescribePodResponse(
            pod_name=pod_name,
            namespace=command.namespace,
            status="NOTFOUND",
        )

mutants_xǁDescribePodUseCaseǁ__init____mutmut['_mutmut_orig'] = DescribePodUseCase.xǁDescribePodUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁ__init____mutmut['xǁDescribePodUseCaseǁ__init____mutmut_1'] = DescribePodUseCase.xǁDescribePodUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁDescribePodUseCaseǁexecute__mutmut['_mutmut_orig'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_1'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_2'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_3'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_4'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_5'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_6'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_7'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_8'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_9'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_10'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_11'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_12'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_13'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_14'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_15'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_16'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_17'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_18'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_19'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_20'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_21'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_22'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_23'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_24'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_25'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_26'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_27'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_28'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_29'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_30'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_31'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_32'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_33'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_34'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_35'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_36'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_37'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_38'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_39'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_40'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_41'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_42'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_43'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_44'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_45'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_46'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_47'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_48'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_48 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_49'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_49 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_50'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_50 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_51'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_51 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_52'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_52 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_53'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_53 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_54'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_54 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_55'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_55 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_56'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_56 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_57'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_57 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_58'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_58 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_59'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_59 # type: ignore # mutmut generated
mutants_xǁDescribePodUseCaseǁexecute__mutmut['xǁDescribePodUseCaseǁexecute__mutmut_60'] = DescribePodUseCase.xǁDescribePodUseCaseǁexecute__mutmut_60 # type: ignore # mutmut generated
