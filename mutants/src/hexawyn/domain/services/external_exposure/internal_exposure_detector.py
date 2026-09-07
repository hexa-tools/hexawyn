from __future__ import annotations


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_is_internal_load_balancer__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_internal_load_balancer__mutmut)
def is_internal_load_balancer(
    annotations: dict[str, str], internal_annotations: tuple[tuple[str, str], ...]
) -> bool:
    return any(annotations.get(key) == value for key, value in internal_annotations)


def x_is_internal_load_balancer__mutmut_orig(
    annotations: dict[str, str], internal_annotations: tuple[tuple[str, str], ...]
) -> bool:
    return any(annotations.get(key) == value for key, value in internal_annotations)


def x_is_internal_load_balancer__mutmut_1(
    annotations: dict[str, str], internal_annotations: tuple[tuple[str, str], ...]
) -> bool:
    return any(None)


def x_is_internal_load_balancer__mutmut_2(
    annotations: dict[str, str], internal_annotations: tuple[tuple[str, str], ...]
) -> bool:
    return any(annotations.get(None) == value for key, value in internal_annotations)


def x_is_internal_load_balancer__mutmut_3(
    annotations: dict[str, str], internal_annotations: tuple[tuple[str, str], ...]
) -> bool:
    return any(annotations.get(key) != value for key, value in internal_annotations)

mutants_x_is_internal_load_balancer__mutmut['_mutmut_orig'] = x_is_internal_load_balancer__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_internal_load_balancer__mutmut['x_is_internal_load_balancer__mutmut_1'] = x_is_internal_load_balancer__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_internal_load_balancer__mutmut['x_is_internal_load_balancer__mutmut_2'] = x_is_internal_load_balancer__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_internal_load_balancer__mutmut['x_is_internal_load_balancer__mutmut_3'] = x_is_internal_load_balancer__mutmut_3 # type: ignore # mutmut generated
