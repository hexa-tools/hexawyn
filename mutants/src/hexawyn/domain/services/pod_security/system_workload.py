from __future__ import annotations

_DAEMONSET_OWNER_KIND = "DaemonSet"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_is_known_system_daemonset__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_known_system_daemonset__mutmut)
def is_known_system_daemonset(
    owner_kind: str | None, pod_name: str, known_name_fragments: tuple[str, ...]
) -> bool:
    if owner_kind != _DAEMONSET_OWNER_KIND:
        return False
    return any(fragment in pod_name for fragment in known_name_fragments)


def x_is_known_system_daemonset__mutmut_orig(
    owner_kind: str | None, pod_name: str, known_name_fragments: tuple[str, ...]
) -> bool:
    if owner_kind != _DAEMONSET_OWNER_KIND:
        return False
    return any(fragment in pod_name for fragment in known_name_fragments)


def x_is_known_system_daemonset__mutmut_1(
    owner_kind: str | None, pod_name: str, known_name_fragments: tuple[str, ...]
) -> bool:
    if owner_kind == _DAEMONSET_OWNER_KIND:
        return False
    return any(fragment in pod_name for fragment in known_name_fragments)


def x_is_known_system_daemonset__mutmut_2(
    owner_kind: str | None, pod_name: str, known_name_fragments: tuple[str, ...]
) -> bool:
    if owner_kind != _DAEMONSET_OWNER_KIND:
        return True
    return any(fragment in pod_name for fragment in known_name_fragments)


def x_is_known_system_daemonset__mutmut_3(
    owner_kind: str | None, pod_name: str, known_name_fragments: tuple[str, ...]
) -> bool:
    if owner_kind != _DAEMONSET_OWNER_KIND:
        return False
    return any(None)


def x_is_known_system_daemonset__mutmut_4(
    owner_kind: str | None, pod_name: str, known_name_fragments: tuple[str, ...]
) -> bool:
    if owner_kind != _DAEMONSET_OWNER_KIND:
        return False
    return any(fragment not in pod_name for fragment in known_name_fragments)

mutants_x_is_known_system_daemonset__mutmut['_mutmut_orig'] = x_is_known_system_daemonset__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_known_system_daemonset__mutmut['x_is_known_system_daemonset__mutmut_1'] = x_is_known_system_daemonset__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_known_system_daemonset__mutmut['x_is_known_system_daemonset__mutmut_2'] = x_is_known_system_daemonset__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_known_system_daemonset__mutmut['x_is_known_system_daemonset__mutmut_3'] = x_is_known_system_daemonset__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_known_system_daemonset__mutmut['x_is_known_system_daemonset__mutmut_4'] = x_is_known_system_daemonset__mutmut_4 # type: ignore # mutmut generated
