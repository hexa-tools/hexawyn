from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.use_case.workloads.list_pods.command import ListPodsCommand
from hexawyn.application.use_case.workloads.list_pods.response import ListPodsResponse
from hexawyn.application.use_case.workloads.list_pods.sort_pods import sort_pods_unsafe_first


class ListPodsUseCase:
    """Lists pods in a namespace, sorted unhealthy first."""

    def __init__(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port

    def execute(self, command: ListPodsCommand) -> ListPodsResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        sorted_pods = sort_pods_unsafe_first(pods)
        return ListPodsResponse(pods=sorted_pods)
