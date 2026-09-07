from __future__ import annotations

from hexawyn.domain.models.secret_rotation import RiskLevel, StaleSecretFinding

_RISK_BASE_SCORE: dict[RiskLevel, int] = {"critical": 50, "medium": 30, "low": 10}
_AGE_DIVISOR = 4
_MAX_SCORE = 100
_MIN_SCORE = 0


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compute_urgency_score__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_urgency_score__mutmut)
def compute_urgency_score(risk_level: RiskLevel, age_days: int) -> int:
    score = _RISK_BASE_SCORE[risk_level] + age_days // _AGE_DIVISOR
    return min(_MAX_SCORE, max(_MIN_SCORE, score))


def x_compute_urgency_score__mutmut_orig(risk_level: RiskLevel, age_days: int) -> int:
    score = _RISK_BASE_SCORE[risk_level] + age_days // _AGE_DIVISOR
    return min(_MAX_SCORE, max(_MIN_SCORE, score))


def x_compute_urgency_score__mutmut_1(risk_level: RiskLevel, age_days: int) -> int:
    score = None
    return min(_MAX_SCORE, max(_MIN_SCORE, score))


def x_compute_urgency_score__mutmut_2(risk_level: RiskLevel, age_days: int) -> int:
    score = _RISK_BASE_SCORE[risk_level] - age_days // _AGE_DIVISOR
    return min(_MAX_SCORE, max(_MIN_SCORE, score))


def x_compute_urgency_score__mutmut_3(risk_level: RiskLevel, age_days: int) -> int:
    score = _RISK_BASE_SCORE[risk_level] + age_days / _AGE_DIVISOR
    return min(_MAX_SCORE, max(_MIN_SCORE, score))


def x_compute_urgency_score__mutmut_4(risk_level: RiskLevel, age_days: int) -> int:
    score = _RISK_BASE_SCORE[risk_level] + age_days // _AGE_DIVISOR
    return min(None, max(_MIN_SCORE, score))


def x_compute_urgency_score__mutmut_5(risk_level: RiskLevel, age_days: int) -> int:
    score = _RISK_BASE_SCORE[risk_level] + age_days // _AGE_DIVISOR
    return min(_MAX_SCORE, None)


def x_compute_urgency_score__mutmut_6(risk_level: RiskLevel, age_days: int) -> int:
    score = _RISK_BASE_SCORE[risk_level] + age_days // _AGE_DIVISOR
    return min(max(_MIN_SCORE, score))


def x_compute_urgency_score__mutmut_7(risk_level: RiskLevel, age_days: int) -> int:
    score = _RISK_BASE_SCORE[risk_level] + age_days // _AGE_DIVISOR
    return min(_MAX_SCORE, )


def x_compute_urgency_score__mutmut_8(risk_level: RiskLevel, age_days: int) -> int:
    score = _RISK_BASE_SCORE[risk_level] + age_days // _AGE_DIVISOR
    return min(_MAX_SCORE, max(None, score))


def x_compute_urgency_score__mutmut_9(risk_level: RiskLevel, age_days: int) -> int:
    score = _RISK_BASE_SCORE[risk_level] + age_days // _AGE_DIVISOR
    return min(_MAX_SCORE, max(_MIN_SCORE, None))


def x_compute_urgency_score__mutmut_10(risk_level: RiskLevel, age_days: int) -> int:
    score = _RISK_BASE_SCORE[risk_level] + age_days // _AGE_DIVISOR
    return min(_MAX_SCORE, max(score))


def x_compute_urgency_score__mutmut_11(risk_level: RiskLevel, age_days: int) -> int:
    score = _RISK_BASE_SCORE[risk_level] + age_days // _AGE_DIVISOR
    return min(_MAX_SCORE, max(_MIN_SCORE, ))

mutants_x_compute_urgency_score__mutmut['_mutmut_orig'] = x_compute_urgency_score__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_urgency_score__mutmut['x_compute_urgency_score__mutmut_1'] = x_compute_urgency_score__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_urgency_score__mutmut['x_compute_urgency_score__mutmut_2'] = x_compute_urgency_score__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_urgency_score__mutmut['x_compute_urgency_score__mutmut_3'] = x_compute_urgency_score__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_urgency_score__mutmut['x_compute_urgency_score__mutmut_4'] = x_compute_urgency_score__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_urgency_score__mutmut['x_compute_urgency_score__mutmut_5'] = x_compute_urgency_score__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_urgency_score__mutmut['x_compute_urgency_score__mutmut_6'] = x_compute_urgency_score__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_urgency_score__mutmut['x_compute_urgency_score__mutmut_7'] = x_compute_urgency_score__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_urgency_score__mutmut['x_compute_urgency_score__mutmut_8'] = x_compute_urgency_score__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_urgency_score__mutmut['x_compute_urgency_score__mutmut_9'] = x_compute_urgency_score__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_urgency_score__mutmut['x_compute_urgency_score__mutmut_10'] = x_compute_urgency_score__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_urgency_score__mutmut['x_compute_urgency_score__mutmut_11'] = x_compute_urgency_score__mutmut_11 # type: ignore # mutmut generated
mutants_x_sort_by_urgency__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_sort_by_urgency__mutmut)
def sort_by_urgency(findings: list[StaleSecretFinding]) -> list[StaleSecretFinding]:
    return sorted(findings, key=lambda finding: (-finding.urgency_score, finding.name))


def x_sort_by_urgency__mutmut_orig(findings: list[StaleSecretFinding]) -> list[StaleSecretFinding]:
    return sorted(findings, key=lambda finding: (-finding.urgency_score, finding.name))


def x_sort_by_urgency__mutmut_1(findings: list[StaleSecretFinding]) -> list[StaleSecretFinding]:
    return sorted(None, key=lambda finding: (-finding.urgency_score, finding.name))


def x_sort_by_urgency__mutmut_2(findings: list[StaleSecretFinding]) -> list[StaleSecretFinding]:
    return sorted(findings, key=None)


def x_sort_by_urgency__mutmut_3(findings: list[StaleSecretFinding]) -> list[StaleSecretFinding]:
    return sorted(key=lambda finding: (-finding.urgency_score, finding.name))


def x_sort_by_urgency__mutmut_4(findings: list[StaleSecretFinding]) -> list[StaleSecretFinding]:
    return sorted(findings, )


def x_sort_by_urgency__mutmut_5(findings: list[StaleSecretFinding]) -> list[StaleSecretFinding]:
    return sorted(findings, key=lambda finding: None)


def x_sort_by_urgency__mutmut_6(findings: list[StaleSecretFinding]) -> list[StaleSecretFinding]:
    return sorted(findings, key=lambda finding: (+finding.urgency_score, finding.name))

mutants_x_sort_by_urgency__mutmut['_mutmut_orig'] = x_sort_by_urgency__mutmut_orig # type: ignore # mutmut generated
mutants_x_sort_by_urgency__mutmut['x_sort_by_urgency__mutmut_1'] = x_sort_by_urgency__mutmut_1 # type: ignore # mutmut generated
mutants_x_sort_by_urgency__mutmut['x_sort_by_urgency__mutmut_2'] = x_sort_by_urgency__mutmut_2 # type: ignore # mutmut generated
mutants_x_sort_by_urgency__mutmut['x_sort_by_urgency__mutmut_3'] = x_sort_by_urgency__mutmut_3 # type: ignore # mutmut generated
mutants_x_sort_by_urgency__mutmut['x_sort_by_urgency__mutmut_4'] = x_sort_by_urgency__mutmut_4 # type: ignore # mutmut generated
mutants_x_sort_by_urgency__mutmut['x_sort_by_urgency__mutmut_5'] = x_sort_by_urgency__mutmut_5 # type: ignore # mutmut generated
mutants_x_sort_by_urgency__mutmut['x_sort_by_urgency__mutmut_6'] = x_sort_by_urgency__mutmut_6 # type: ignore # mutmut generated
