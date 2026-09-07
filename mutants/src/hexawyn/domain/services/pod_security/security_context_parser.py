from __future__ import annotations


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_resolves_to_root__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_resolves_to_root__mutmut)
def resolves_to_root(container_level: bool | None, pod_level: bool | None) -> bool:
    effective = container_level if container_level is not None else pod_level
    return effective is not True


def x_resolves_to_root__mutmut_orig(container_level: bool | None, pod_level: bool | None) -> bool:
    effective = container_level if container_level is not None else pod_level
    return effective is not True


def x_resolves_to_root__mutmut_1(container_level: bool | None, pod_level: bool | None) -> bool:
    effective = None
    return effective is not True


def x_resolves_to_root__mutmut_2(container_level: bool | None, pod_level: bool | None) -> bool:
    effective = container_level if container_level is None else pod_level
    return effective is not True


def x_resolves_to_root__mutmut_3(container_level: bool | None, pod_level: bool | None) -> bool:
    effective = container_level if container_level is not None else pod_level
    return effective is True


def x_resolves_to_root__mutmut_4(container_level: bool | None, pod_level: bool | None) -> bool:
    effective = container_level if container_level is not None else pod_level
    return effective is not False

mutants_x_resolves_to_root__mutmut['_mutmut_orig'] = x_resolves_to_root__mutmut_orig # type: ignore # mutmut generated
mutants_x_resolves_to_root__mutmut['x_resolves_to_root__mutmut_1'] = x_resolves_to_root__mutmut_1 # type: ignore # mutmut generated
mutants_x_resolves_to_root__mutmut['x_resolves_to_root__mutmut_2'] = x_resolves_to_root__mutmut_2 # type: ignore # mutmut generated
mutants_x_resolves_to_root__mutmut['x_resolves_to_root__mutmut_3'] = x_resolves_to_root__mutmut_3 # type: ignore # mutmut generated
mutants_x_resolves_to_root__mutmut['x_resolves_to_root__mutmut_4'] = x_resolves_to_root__mutmut_4 # type: ignore # mutmut generated
mutants_x_allows_privilege_escalation__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_allows_privilege_escalation__mutmut)
def allows_privilege_escalation(value: bool | None) -> bool:
    return value is not False


def x_allows_privilege_escalation__mutmut_orig(value: bool | None) -> bool:
    return value is not False


def x_allows_privilege_escalation__mutmut_1(value: bool | None) -> bool:
    return value is False


def x_allows_privilege_escalation__mutmut_2(value: bool | None) -> bool:
    return value is not True

mutants_x_allows_privilege_escalation__mutmut['_mutmut_orig'] = x_allows_privilege_escalation__mutmut_orig # type: ignore # mutmut generated
mutants_x_allows_privilege_escalation__mutmut['x_allows_privilege_escalation__mutmut_1'] = x_allows_privilege_escalation__mutmut_1 # type: ignore # mutmut generated
mutants_x_allows_privilege_escalation__mutmut['x_allows_privilege_escalation__mutmut_2'] = x_allows_privilege_escalation__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_privileged__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_privileged__mutmut)
def is_privileged(value: bool | None) -> bool:
    return value is True


def x_is_privileged__mutmut_orig(value: bool | None) -> bool:
    return value is True


def x_is_privileged__mutmut_1(value: bool | None) -> bool:
    return value is not True


def x_is_privileged__mutmut_2(value: bool | None) -> bool:
    return value is False

mutants_x_is_privileged__mutmut['_mutmut_orig'] = x_is_privileged__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_privileged__mutmut['x_is_privileged__mutmut_1'] = x_is_privileged__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_privileged__mutmut['x_is_privileged__mutmut_2'] = x_is_privileged__mutmut_2 # type: ignore # mutmut generated
