from __future__ import annotations

_EXTERNALLY_EXPOSED_TYPES = frozenset({"LoadBalancer", "NodePort"})


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_is_externally_exposed_type__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_externally_exposed_type__mutmut)
def is_externally_exposed_type(service_type: str) -> bool:
    return service_type in _EXTERNALLY_EXPOSED_TYPES


def x_is_externally_exposed_type__mutmut_orig(service_type: str) -> bool:
    return service_type in _EXTERNALLY_EXPOSED_TYPES


def x_is_externally_exposed_type__mutmut_1(service_type: str) -> bool:
    return service_type not in _EXTERNALLY_EXPOSED_TYPES

mutants_x_is_externally_exposed_type__mutmut['_mutmut_orig'] = x_is_externally_exposed_type__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_externally_exposed_type__mutmut['x_is_externally_exposed_type__mutmut_1'] = x_is_externally_exposed_type__mutmut_1 # type: ignore # mutmut generated
