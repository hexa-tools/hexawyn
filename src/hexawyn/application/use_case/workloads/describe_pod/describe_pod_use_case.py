from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.use_case.workloads.describe_pod.command import (
    DescribePodCommand,
)
from hexawyn.application.use_case.workloads.describe_pod.response import (
    DescribePodResponse,
)


class DescribePodUseCase:
    def __init__(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port

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
