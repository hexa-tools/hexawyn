from __future__ import annotations


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_is_allowlisted__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_allowlisted__mutmut)
def is_allowlisted(name: str, allowlist: tuple[str, ...]) -> bool:
    return name in allowlist


def x_is_allowlisted__mutmut_orig(name: str, allowlist: tuple[str, ...]) -> bool:
    return name in allowlist


def x_is_allowlisted__mutmut_1(name: str, allowlist: tuple[str, ...]) -> bool:
    return name not in allowlist

mutants_x_is_allowlisted__mutmut['_mutmut_orig'] = x_is_allowlisted__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_allowlisted__mutmut['x_is_allowlisted__mutmut_1'] = x_is_allowlisted__mutmut_1 # type: ignore # mutmut generated
