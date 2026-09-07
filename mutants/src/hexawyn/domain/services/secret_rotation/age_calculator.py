from __future__ import annotations

from datetime import date


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_calculate_age_days__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_calculate_age_days__mutmut)
def calculate_age_days(last_modified: date, today: date) -> int:
    return (today - last_modified).days


def x_calculate_age_days__mutmut_orig(last_modified: date, today: date) -> int:
    return (today - last_modified).days


def x_calculate_age_days__mutmut_1(last_modified: date, today: date) -> int:
    return (today + last_modified).days

mutants_x_calculate_age_days__mutmut['_mutmut_orig'] = x_calculate_age_days__mutmut_orig # type: ignore # mutmut generated
mutants_x_calculate_age_days__mutmut['x_calculate_age_days__mutmut_1'] = x_calculate_age_days__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_stale__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_stale__mutmut)
def is_stale(age_days: int, threshold_days: int) -> bool:
    return age_days > threshold_days


def x_is_stale__mutmut_orig(age_days: int, threshold_days: int) -> bool:
    return age_days > threshold_days


def x_is_stale__mutmut_1(age_days: int, threshold_days: int) -> bool:
    return age_days >= threshold_days

mutants_x_is_stale__mutmut['_mutmut_orig'] = x_is_stale__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_stale__mutmut['x_is_stale__mutmut_1'] = x_is_stale__mutmut_1 # type: ignore # mutmut generated
