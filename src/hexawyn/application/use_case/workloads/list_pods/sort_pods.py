from hexawyn.application.ports.driven.k8s_port import PodInfo
from hexawyn.domain.models.constants import POD_UNHEALTHY_ORDER


def sort_pods_unsafe_first(pods: list[PodInfo]) -> list[PodInfo]:
    return sorted(pods, key=_sort_key)


def _sort_key(pod: PodInfo) -> tuple[int, str]:
    order = POD_UNHEALTHY_ORDER.get(pod["status"], 99)
    return (order, pod["name"])
