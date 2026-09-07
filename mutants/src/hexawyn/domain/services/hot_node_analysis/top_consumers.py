from __future__ import annotations

from hexawyn.domain.models.hot_node_analysis import TopConsumer


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_select_top_consumers__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_select_top_consumers__mutmut)
def select_top_consumers(pods: list[TopConsumer], count: int) -> list[TopConsumer]:
    return sorted(pods, key=lambda pod: pod.cpu_usage_cores, reverse=True)[:count]


def x_select_top_consumers__mutmut_orig(pods: list[TopConsumer], count: int) -> list[TopConsumer]:
    return sorted(pods, key=lambda pod: pod.cpu_usage_cores, reverse=True)[:count]


def x_select_top_consumers__mutmut_1(pods: list[TopConsumer], count: int) -> list[TopConsumer]:
    return sorted(None, key=lambda pod: pod.cpu_usage_cores, reverse=True)[:count]


def x_select_top_consumers__mutmut_2(pods: list[TopConsumer], count: int) -> list[TopConsumer]:
    return sorted(pods, key=None, reverse=True)[:count]


def x_select_top_consumers__mutmut_3(pods: list[TopConsumer], count: int) -> list[TopConsumer]:
    return sorted(pods, key=lambda pod: pod.cpu_usage_cores, reverse=None)[:count]


def x_select_top_consumers__mutmut_4(pods: list[TopConsumer], count: int) -> list[TopConsumer]:
    return sorted(key=lambda pod: pod.cpu_usage_cores, reverse=True)[:count]


def x_select_top_consumers__mutmut_5(pods: list[TopConsumer], count: int) -> list[TopConsumer]:
    return sorted(pods, reverse=True)[:count]


def x_select_top_consumers__mutmut_6(pods: list[TopConsumer], count: int) -> list[TopConsumer]:
    return sorted(pods, key=lambda pod: pod.cpu_usage_cores, )[:count]


def x_select_top_consumers__mutmut_7(pods: list[TopConsumer], count: int) -> list[TopConsumer]:
    return sorted(pods, key=lambda pod: None, reverse=True)[:count]


def x_select_top_consumers__mutmut_8(pods: list[TopConsumer], count: int) -> list[TopConsumer]:
    return sorted(pods, key=lambda pod: pod.cpu_usage_cores, reverse=False)[:count]

mutants_x_select_top_consumers__mutmut['_mutmut_orig'] = x_select_top_consumers__mutmut_orig # type: ignore # mutmut generated
mutants_x_select_top_consumers__mutmut['x_select_top_consumers__mutmut_1'] = x_select_top_consumers__mutmut_1 # type: ignore # mutmut generated
mutants_x_select_top_consumers__mutmut['x_select_top_consumers__mutmut_2'] = x_select_top_consumers__mutmut_2 # type: ignore # mutmut generated
mutants_x_select_top_consumers__mutmut['x_select_top_consumers__mutmut_3'] = x_select_top_consumers__mutmut_3 # type: ignore # mutmut generated
mutants_x_select_top_consumers__mutmut['x_select_top_consumers__mutmut_4'] = x_select_top_consumers__mutmut_4 # type: ignore # mutmut generated
mutants_x_select_top_consumers__mutmut['x_select_top_consumers__mutmut_5'] = x_select_top_consumers__mutmut_5 # type: ignore # mutmut generated
mutants_x_select_top_consumers__mutmut['x_select_top_consumers__mutmut_6'] = x_select_top_consumers__mutmut_6 # type: ignore # mutmut generated
mutants_x_select_top_consumers__mutmut['x_select_top_consumers__mutmut_7'] = x_select_top_consumers__mutmut_7 # type: ignore # mutmut generated
mutants_x_select_top_consumers__mutmut['x_select_top_consumers__mutmut_8'] = x_select_top_consumers__mutmut_8 # type: ignore # mutmut generated
