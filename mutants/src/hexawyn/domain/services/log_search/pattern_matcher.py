from __future__ import annotations

import re
from difflib import SequenceMatcher

from hexawyn.domain.errors import LogPatternError


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compile_pattern__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compile_pattern__mutmut)
def compile_pattern(pattern: str, is_regex: bool) -> re.Pattern[str]:
    """Compiles a search pattern for log-line matching.

    `is_regex=False` (default) escapes the pattern first, so a literal search
    like "version=1.2.3" or "connection refused (postgres)" never misfires as
    regex syntax. `is_regex=True` compiles as-is, raising LogPatternError on
    invalid syntax.
    """
    source = pattern if is_regex else re.escape(pattern)
    try:
        return re.compile(source)
    except re.error as exc:
        raise LogPatternError(pattern, str(exc)) from exc


def x_compile_pattern__mutmut_orig(pattern: str, is_regex: bool) -> re.Pattern[str]:
    """Compiles a search pattern for log-line matching.

    `is_regex=False` (default) escapes the pattern first, so a literal search
    like "version=1.2.3" or "connection refused (postgres)" never misfires as
    regex syntax. `is_regex=True` compiles as-is, raising LogPatternError on
    invalid syntax.
    """
    source = pattern if is_regex else re.escape(pattern)
    try:
        return re.compile(source)
    except re.error as exc:
        raise LogPatternError(pattern, str(exc)) from exc


def x_compile_pattern__mutmut_1(pattern: str, is_regex: bool) -> re.Pattern[str]:
    """Compiles a search pattern for log-line matching.

    `is_regex=False` (default) escapes the pattern first, so a literal search
    like "version=1.2.3" or "connection refused (postgres)" never misfires as
    regex syntax. `is_regex=True` compiles as-is, raising LogPatternError on
    invalid syntax.
    """
    source = None
    try:
        return re.compile(source)
    except re.error as exc:
        raise LogPatternError(pattern, str(exc)) from exc


def x_compile_pattern__mutmut_2(pattern: str, is_regex: bool) -> re.Pattern[str]:
    """Compiles a search pattern for log-line matching.

    `is_regex=False` (default) escapes the pattern first, so a literal search
    like "version=1.2.3" or "connection refused (postgres)" never misfires as
    regex syntax. `is_regex=True` compiles as-is, raising LogPatternError on
    invalid syntax.
    """
    source = pattern if is_regex else re.escape(None)
    try:
        return re.compile(source)
    except re.error as exc:
        raise LogPatternError(pattern, str(exc)) from exc


def x_compile_pattern__mutmut_3(pattern: str, is_regex: bool) -> re.Pattern[str]:
    """Compiles a search pattern for log-line matching.

    `is_regex=False` (default) escapes the pattern first, so a literal search
    like "version=1.2.3" or "connection refused (postgres)" never misfires as
    regex syntax. `is_regex=True` compiles as-is, raising LogPatternError on
    invalid syntax.
    """
    source = pattern if is_regex else re.escape(pattern)
    try:
        return re.compile(None)
    except re.error as exc:
        raise LogPatternError(pattern, str(exc)) from exc


def x_compile_pattern__mutmut_4(pattern: str, is_regex: bool) -> re.Pattern[str]:
    """Compiles a search pattern for log-line matching.

    `is_regex=False` (default) escapes the pattern first, so a literal search
    like "version=1.2.3" or "connection refused (postgres)" never misfires as
    regex syntax. `is_regex=True` compiles as-is, raising LogPatternError on
    invalid syntax.
    """
    source = pattern if is_regex else re.escape(pattern)
    try:
        return re.compile(source)
    except re.error as exc:
        raise LogPatternError(None, str(exc)) from exc


def x_compile_pattern__mutmut_5(pattern: str, is_regex: bool) -> re.Pattern[str]:
    """Compiles a search pattern for log-line matching.

    `is_regex=False` (default) escapes the pattern first, so a literal search
    like "version=1.2.3" or "connection refused (postgres)" never misfires as
    regex syntax. `is_regex=True` compiles as-is, raising LogPatternError on
    invalid syntax.
    """
    source = pattern if is_regex else re.escape(pattern)
    try:
        return re.compile(source)
    except re.error as exc:
        raise LogPatternError(pattern, None) from exc


def x_compile_pattern__mutmut_6(pattern: str, is_regex: bool) -> re.Pattern[str]:
    """Compiles a search pattern for log-line matching.

    `is_regex=False` (default) escapes the pattern first, so a literal search
    like "version=1.2.3" or "connection refused (postgres)" never misfires as
    regex syntax. `is_regex=True` compiles as-is, raising LogPatternError on
    invalid syntax.
    """
    source = pattern if is_regex else re.escape(pattern)
    try:
        return re.compile(source)
    except re.error as exc:
        raise LogPatternError(str(exc)) from exc


def x_compile_pattern__mutmut_7(pattern: str, is_regex: bool) -> re.Pattern[str]:
    """Compiles a search pattern for log-line matching.

    `is_regex=False` (default) escapes the pattern first, so a literal search
    like "version=1.2.3" or "connection refused (postgres)" never misfires as
    regex syntax. `is_regex=True` compiles as-is, raising LogPatternError on
    invalid syntax.
    """
    source = pattern if is_regex else re.escape(pattern)
    try:
        return re.compile(source)
    except re.error as exc:
        raise LogPatternError(pattern, ) from exc


def x_compile_pattern__mutmut_8(pattern: str, is_regex: bool) -> re.Pattern[str]:
    """Compiles a search pattern for log-line matching.

    `is_regex=False` (default) escapes the pattern first, so a literal search
    like "version=1.2.3" or "connection refused (postgres)" never misfires as
    regex syntax. `is_regex=True` compiles as-is, raising LogPatternError on
    invalid syntax.
    """
    source = pattern if is_regex else re.escape(pattern)
    try:
        return re.compile(source)
    except re.error as exc:
        raise LogPatternError(pattern, str(None)) from exc

mutants_x_compile_pattern__mutmut['_mutmut_orig'] = x_compile_pattern__mutmut_orig # type: ignore # mutmut generated
mutants_x_compile_pattern__mutmut['x_compile_pattern__mutmut_1'] = x_compile_pattern__mutmut_1 # type: ignore # mutmut generated
mutants_x_compile_pattern__mutmut['x_compile_pattern__mutmut_2'] = x_compile_pattern__mutmut_2 # type: ignore # mutmut generated
mutants_x_compile_pattern__mutmut['x_compile_pattern__mutmut_3'] = x_compile_pattern__mutmut_3 # type: ignore # mutmut generated
mutants_x_compile_pattern__mutmut['x_compile_pattern__mutmut_4'] = x_compile_pattern__mutmut_4 # type: ignore # mutmut generated
mutants_x_compile_pattern__mutmut['x_compile_pattern__mutmut_5'] = x_compile_pattern__mutmut_5 # type: ignore # mutmut generated
mutants_x_compile_pattern__mutmut['x_compile_pattern__mutmut_6'] = x_compile_pattern__mutmut_6 # type: ignore # mutmut generated
mutants_x_compile_pattern__mutmut['x_compile_pattern__mutmut_7'] = x_compile_pattern__mutmut_7 # type: ignore # mutmut generated
mutants_x_compile_pattern__mutmut['x_compile_pattern__mutmut_8'] = x_compile_pattern__mutmut_8 # type: ignore # mutmut generated
mutants_x_similarity_score__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_similarity_score__mutmut)
def similarity_score(pattern: str, line: str) -> float:
    """Lightweight, stdlib-only "semantic-ish" similarity — NOT a vector
    embedding. Used only as a fallback when a pod has zero exact matches, to
    surface the closest near-miss line (tagged match_type="semantic")."""
    return SequenceMatcher(None, pattern.lower(), line.lower()).ratio()


def x_similarity_score__mutmut_orig(pattern: str, line: str) -> float:
    """Lightweight, stdlib-only "semantic-ish" similarity — NOT a vector
    embedding. Used only as a fallback when a pod has zero exact matches, to
    surface the closest near-miss line (tagged match_type="semantic")."""
    return SequenceMatcher(None, pattern.lower(), line.lower()).ratio()


def x_similarity_score__mutmut_1(pattern: str, line: str) -> float:
    """Lightweight, stdlib-only "semantic-ish" similarity — NOT a vector
    embedding. Used only as a fallback when a pod has zero exact matches, to
    surface the closest near-miss line (tagged match_type="semantic")."""
    return SequenceMatcher(None, None, line.lower()).ratio()


def x_similarity_score__mutmut_2(pattern: str, line: str) -> float:
    """Lightweight, stdlib-only "semantic-ish" similarity — NOT a vector
    embedding. Used only as a fallback when a pod has zero exact matches, to
    surface the closest near-miss line (tagged match_type="semantic")."""
    return SequenceMatcher(None, pattern.lower(), None).ratio()


def x_similarity_score__mutmut_3(pattern: str, line: str) -> float:
    """Lightweight, stdlib-only "semantic-ish" similarity — NOT a vector
    embedding. Used only as a fallback when a pod has zero exact matches, to
    surface the closest near-miss line (tagged match_type="semantic")."""
    return SequenceMatcher(pattern.lower(), line.lower()).ratio()


def x_similarity_score__mutmut_4(pattern: str, line: str) -> float:
    """Lightweight, stdlib-only "semantic-ish" similarity — NOT a vector
    embedding. Used only as a fallback when a pod has zero exact matches, to
    surface the closest near-miss line (tagged match_type="semantic")."""
    return SequenceMatcher(None, line.lower()).ratio()


def x_similarity_score__mutmut_5(pattern: str, line: str) -> float:
    """Lightweight, stdlib-only "semantic-ish" similarity — NOT a vector
    embedding. Used only as a fallback when a pod has zero exact matches, to
    surface the closest near-miss line (tagged match_type="semantic")."""
    return SequenceMatcher(None, pattern.lower(), ).ratio()


def x_similarity_score__mutmut_6(pattern: str, line: str) -> float:
    """Lightweight, stdlib-only "semantic-ish" similarity — NOT a vector
    embedding. Used only as a fallback when a pod has zero exact matches, to
    surface the closest near-miss line (tagged match_type="semantic")."""
    return SequenceMatcher(None, pattern.upper(), line.lower()).ratio()


def x_similarity_score__mutmut_7(pattern: str, line: str) -> float:
    """Lightweight, stdlib-only "semantic-ish" similarity — NOT a vector
    embedding. Used only as a fallback when a pod has zero exact matches, to
    surface the closest near-miss line (tagged match_type="semantic")."""
    return SequenceMatcher(None, pattern.lower(), line.upper()).ratio()

mutants_x_similarity_score__mutmut['_mutmut_orig'] = x_similarity_score__mutmut_orig # type: ignore # mutmut generated
mutants_x_similarity_score__mutmut['x_similarity_score__mutmut_1'] = x_similarity_score__mutmut_1 # type: ignore # mutmut generated
mutants_x_similarity_score__mutmut['x_similarity_score__mutmut_2'] = x_similarity_score__mutmut_2 # type: ignore # mutmut generated
mutants_x_similarity_score__mutmut['x_similarity_score__mutmut_3'] = x_similarity_score__mutmut_3 # type: ignore # mutmut generated
mutants_x_similarity_score__mutmut['x_similarity_score__mutmut_4'] = x_similarity_score__mutmut_4 # type: ignore # mutmut generated
mutants_x_similarity_score__mutmut['x_similarity_score__mutmut_5'] = x_similarity_score__mutmut_5 # type: ignore # mutmut generated
mutants_x_similarity_score__mutmut['x_similarity_score__mutmut_6'] = x_similarity_score__mutmut_6 # type: ignore # mutmut generated
mutants_x_similarity_score__mutmut['x_similarity_score__mutmut_7'] = x_similarity_score__mutmut_7 # type: ignore # mutmut generated
