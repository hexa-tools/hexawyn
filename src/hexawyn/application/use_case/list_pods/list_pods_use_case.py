from hexawyn.application.ports.driven.k8s_port import K8sPort, PodInfo
from hexawyn.application.use_case.list_pods.command import ListPodsCommand
from hexawyn.application.use_case.list_pods.response import ListPodsResponse

_UNHEALTHY: dict[str, int] = {
    "CrashLoop": 0,
    "CrashLoopBackOff": 0,
    "Error": 1,
    "ImagePullBackOff": 1,
    "Pending": 2,
    "Unknown": 3,
    "Terminating": 4,
}


class ListPodsUseCase:
    def __init__(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port

    def execute(self, command: ListPodsCommand) -> ListPodsResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        return ListPodsResponse(pods=sorted(pods, key=_sort_key))


def _sort_key(pod: PodInfo) -> tuple[int, str]:
    return (_UNHEALTHY.get(pod["status"], 99), pod["name"])
