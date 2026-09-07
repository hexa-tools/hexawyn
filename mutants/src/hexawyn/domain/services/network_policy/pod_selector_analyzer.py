from __future__ import annotations


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_has_empty_pod_selector__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_has_empty_pod_selector__mutmut)
def has_empty_pod_selector(match_labels: dict[str, str], match_expressions: list[object]) -> bool:
    return not match_labels and not match_expressions


def x_has_empty_pod_selector__mutmut_orig(match_labels: dict[str, str], match_expressions: list[object]) -> bool:
    return not match_labels and not match_expressions


def x_has_empty_pod_selector__mutmut_1(match_labels: dict[str, str], match_expressions: list[object]) -> bool:
    return not match_labels or not match_expressions


def x_has_empty_pod_selector__mutmut_2(match_labels: dict[str, str], match_expressions: list[object]) -> bool:
    return match_labels and not match_expressions


def x_has_empty_pod_selector__mutmut_3(match_labels: dict[str, str], match_expressions: list[object]) -> bool:
    return not match_labels and match_expressions

mutants_x_has_empty_pod_selector__mutmut['_mutmut_orig'] = x_has_empty_pod_selector__mutmut_orig # type: ignore # mutmut generated
mutants_x_has_empty_pod_selector__mutmut['x_has_empty_pod_selector__mutmut_1'] = x_has_empty_pod_selector__mutmut_1 # type: ignore # mutmut generated
mutants_x_has_empty_pod_selector__mutmut['x_has_empty_pod_selector__mutmut_2'] = x_has_empty_pod_selector__mutmut_2 # type: ignore # mutmut generated
mutants_x_has_empty_pod_selector__mutmut['x_has_empty_pod_selector__mutmut_3'] = x_has_empty_pod_selector__mutmut_3 # type: ignore # mutmut generated
