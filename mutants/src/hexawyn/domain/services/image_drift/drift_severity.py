from __future__ import annotations

from hexawyn.domain.models.image_drift import DriftType, ImageDriftSeverity


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_classify_severity__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_classify_severity__mutmut)
def classify_severity(drift_type: DriftType) -> ImageDriftSeverity:
    return "critical"


def x_classify_severity__mutmut_orig(drift_type: DriftType) -> ImageDriftSeverity:
    return "critical"


def x_classify_severity__mutmut_1(drift_type: DriftType) -> ImageDriftSeverity:
    return "XXcriticalXX"


def x_classify_severity__mutmut_2(drift_type: DriftType) -> ImageDriftSeverity:
    return "CRITICAL"

mutants_x_classify_severity__mutmut['_mutmut_orig'] = x_classify_severity__mutmut_orig # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_1'] = x_classify_severity__mutmut_1 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_2'] = x_classify_severity__mutmut_2 # type: ignore # mutmut generated
