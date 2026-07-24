from hexawyn.application.ports.driven.k8s_port import K8sPort, PodInfo
from hexawyn.application.use_case.list_pods.command import ListPodsCommand
from hexawyn.application.use_case.list_pods.response import ListPodsResponse
from hexawyn.application.ports.driving.list_pods.list_pods_service_port import (
    ListPodsServicePort,
)

_UNHEALTHY_ORDER: dict[str, int] = {
    "CrashLoop": 0,
    "CrashLoopBackOff": 0,
    "Error": 1,
    "ImagePullBackOff": 1,
    "Pending": 2,
    "Unknown": 3,
    "Terminating": 4,
}


class ListPodsService(ListPodsServicePort):
    """Lists pods in a namespace, sorted unhealthy first."""

    def __init__(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port

    def list_pods(self, command: ListPodsCommand) -> ListPodsResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        sorted_pods = sorted(pods, key=_sort_key)
        return ListPodsResponse(pods=sorted_pods)


def _sort_key(pod: PodInfo) -> tuple[int, str]:
    order = _UNHEALTHY_ORDER.get(pod["status"], 99)
    return (order, pod["name"])
