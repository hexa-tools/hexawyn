from __future__ import annotations


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_is_unused__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_unused__mutmut)
def is_unused(referenced_by: list[str]) -> bool:
    return len(referenced_by) == 0


def x_is_unused__mutmut_orig(referenced_by: list[str]) -> bool:
    return len(referenced_by) == 0


def x_is_unused__mutmut_1(referenced_by: list[str]) -> bool:
    return len(referenced_by) != 0


def x_is_unused__mutmut_2(referenced_by: list[str]) -> bool:
    return len(referenced_by) == 1

mutants_x_is_unused__mutmut['_mutmut_orig'] = x_is_unused__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_unused__mutmut['x_is_unused__mutmut_1'] = x_is_unused__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_unused__mutmut['x_is_unused__mutmut_2'] = x_is_unused__mutmut_2 # type: ignore # mutmut generated
mutants_x_deduplicate_references__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_deduplicate_references__mutmut)
def deduplicate_references(referenced_by: list[str]) -> list[str]:
    return sorted(set(referenced_by))


def x_deduplicate_references__mutmut_orig(referenced_by: list[str]) -> list[str]:
    return sorted(set(referenced_by))


def x_deduplicate_references__mutmut_1(referenced_by: list[str]) -> list[str]:
    return sorted(None)


def x_deduplicate_references__mutmut_2(referenced_by: list[str]) -> list[str]:
    return sorted(set(None))

mutants_x_deduplicate_references__mutmut['_mutmut_orig'] = x_deduplicate_references__mutmut_orig # type: ignore # mutmut generated
mutants_x_deduplicate_references__mutmut['x_deduplicate_references__mutmut_1'] = x_deduplicate_references__mutmut_1 # type: ignore # mutmut generated
mutants_x_deduplicate_references__mutmut['x_deduplicate_references__mutmut_2'] = x_deduplicate_references__mutmut_2 # type: ignore # mutmut generated
