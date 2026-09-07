from hexawyn.application.ports.driven.k8s_port import PodInfo
from hexawyn.domain.models.constants import POD_UNHEALTHY_ORDER


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_sort_pods_unsafe_first__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_sort_pods_unsafe_first__mutmut)
def sort_pods_unsafe_first(pods: list[PodInfo]) -> list[PodInfo]:
    return sorted(pods, key=_sort_key)


def x_sort_pods_unsafe_first__mutmut_orig(pods: list[PodInfo]) -> list[PodInfo]:
    return sorted(pods, key=_sort_key)


def x_sort_pods_unsafe_first__mutmut_1(pods: list[PodInfo]) -> list[PodInfo]:
    return sorted(None, key=_sort_key)


def x_sort_pods_unsafe_first__mutmut_2(pods: list[PodInfo]) -> list[PodInfo]:
    return sorted(pods, key=None)


def x_sort_pods_unsafe_first__mutmut_3(pods: list[PodInfo]) -> list[PodInfo]:
    return sorted(key=_sort_key)


def x_sort_pods_unsafe_first__mutmut_4(pods: list[PodInfo]) -> list[PodInfo]:
    return sorted(pods, )

mutants_x_sort_pods_unsafe_first__mutmut['_mutmut_orig'] = x_sort_pods_unsafe_first__mutmut_orig # type: ignore # mutmut generated
mutants_x_sort_pods_unsafe_first__mutmut['x_sort_pods_unsafe_first__mutmut_1'] = x_sort_pods_unsafe_first__mutmut_1 # type: ignore # mutmut generated
mutants_x_sort_pods_unsafe_first__mutmut['x_sort_pods_unsafe_first__mutmut_2'] = x_sort_pods_unsafe_first__mutmut_2 # type: ignore # mutmut generated
mutants_x_sort_pods_unsafe_first__mutmut['x_sort_pods_unsafe_first__mutmut_3'] = x_sort_pods_unsafe_first__mutmut_3 # type: ignore # mutmut generated
mutants_x_sort_pods_unsafe_first__mutmut['x_sort_pods_unsafe_first__mutmut_4'] = x_sort_pods_unsafe_first__mutmut_4 # type: ignore # mutmut generated
mutants_x__sort_key__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__sort_key__mutmut)
def _sort_key(pod: PodInfo) -> tuple[int, str]:
    order = POD_UNHEALTHY_ORDER.get(pod["status"], 99)
    return (order, pod["name"])


def x__sort_key__mutmut_orig(pod: PodInfo) -> tuple[int, str]:
    order = POD_UNHEALTHY_ORDER.get(pod["status"], 99)
    return (order, pod["name"])


def x__sort_key__mutmut_1(pod: PodInfo) -> tuple[int, str]:
    order = None
    return (order, pod["name"])


def x__sort_key__mutmut_2(pod: PodInfo) -> tuple[int, str]:
    order = POD_UNHEALTHY_ORDER.get(None, 99)
    return (order, pod["name"])


def x__sort_key__mutmut_3(pod: PodInfo) -> tuple[int, str]:
    order = POD_UNHEALTHY_ORDER.get(pod["status"], None)
    return (order, pod["name"])


def x__sort_key__mutmut_4(pod: PodInfo) -> tuple[int, str]:
    order = POD_UNHEALTHY_ORDER.get(99)
    return (order, pod["name"])


def x__sort_key__mutmut_5(pod: PodInfo) -> tuple[int, str]:
    order = POD_UNHEALTHY_ORDER.get(pod["status"], )
    return (order, pod["name"])


def x__sort_key__mutmut_6(pod: PodInfo) -> tuple[int, str]:
    order = POD_UNHEALTHY_ORDER.get(pod["XXstatusXX"], 99)
    return (order, pod["name"])


def x__sort_key__mutmut_7(pod: PodInfo) -> tuple[int, str]:
    order = POD_UNHEALTHY_ORDER.get(pod["STATUS"], 99)
    return (order, pod["name"])


def x__sort_key__mutmut_8(pod: PodInfo) -> tuple[int, str]:
    order = POD_UNHEALTHY_ORDER.get(pod["status"], 100)
    return (order, pod["name"])


def x__sort_key__mutmut_9(pod: PodInfo) -> tuple[int, str]:
    order = POD_UNHEALTHY_ORDER.get(pod["status"], 99)
    return (order, pod["XXnameXX"])


def x__sort_key__mutmut_10(pod: PodInfo) -> tuple[int, str]:
    order = POD_UNHEALTHY_ORDER.get(pod["status"], 99)
    return (order, pod["NAME"])

mutants_x__sort_key__mutmut['_mutmut_orig'] = x__sort_key__mutmut_orig # type: ignore # mutmut generated
mutants_x__sort_key__mutmut['x__sort_key__mutmut_1'] = x__sort_key__mutmut_1 # type: ignore # mutmut generated
mutants_x__sort_key__mutmut['x__sort_key__mutmut_2'] = x__sort_key__mutmut_2 # type: ignore # mutmut generated
mutants_x__sort_key__mutmut['x__sort_key__mutmut_3'] = x__sort_key__mutmut_3 # type: ignore # mutmut generated
mutants_x__sort_key__mutmut['x__sort_key__mutmut_4'] = x__sort_key__mutmut_4 # type: ignore # mutmut generated
mutants_x__sort_key__mutmut['x__sort_key__mutmut_5'] = x__sort_key__mutmut_5 # type: ignore # mutmut generated
mutants_x__sort_key__mutmut['x__sort_key__mutmut_6'] = x__sort_key__mutmut_6 # type: ignore # mutmut generated
mutants_x__sort_key__mutmut['x__sort_key__mutmut_7'] = x__sort_key__mutmut_7 # type: ignore # mutmut generated
mutants_x__sort_key__mutmut['x__sort_key__mutmut_8'] = x__sort_key__mutmut_8 # type: ignore # mutmut generated
mutants_x__sort_key__mutmut['x__sort_key__mutmut_9'] = x__sort_key__mutmut_9 # type: ignore # mutmut generated
mutants_x__sort_key__mutmut['x__sort_key__mutmut_10'] = x__sort_key__mutmut_10 # type: ignore # mutmut generated
