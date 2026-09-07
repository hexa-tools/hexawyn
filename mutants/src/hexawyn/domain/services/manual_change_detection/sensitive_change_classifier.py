from __future__ import annotations

from collections.abc import Sequence

from hexawyn.domain.models.manual_change import ManualChangeSeverity


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_classify_severity__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_classify_severity__mutmut)
def classify_severity(
    kind: str, name: str, sensitive_keywords: Sequence[str]
) -> ManualChangeSeverity:
    if kind == "Secret":
        return "critical"
    lowered_name = name.lower()
    if any(keyword in lowered_name for keyword in sensitive_keywords):
        return "critical"
    return "warning"


def x_classify_severity__mutmut_orig(
    kind: str, name: str, sensitive_keywords: Sequence[str]
) -> ManualChangeSeverity:
    if kind == "Secret":
        return "critical"
    lowered_name = name.lower()
    if any(keyword in lowered_name for keyword in sensitive_keywords):
        return "critical"
    return "warning"


def x_classify_severity__mutmut_1(
    kind: str, name: str, sensitive_keywords: Sequence[str]
) -> ManualChangeSeverity:
    if kind != "Secret":
        return "critical"
    lowered_name = name.lower()
    if any(keyword in lowered_name for keyword in sensitive_keywords):
        return "critical"
    return "warning"


def x_classify_severity__mutmut_2(
    kind: str, name: str, sensitive_keywords: Sequence[str]
) -> ManualChangeSeverity:
    if kind == "XXSecretXX":
        return "critical"
    lowered_name = name.lower()
    if any(keyword in lowered_name for keyword in sensitive_keywords):
        return "critical"
    return "warning"


def x_classify_severity__mutmut_3(
    kind: str, name: str, sensitive_keywords: Sequence[str]
) -> ManualChangeSeverity:
    if kind == "secret":
        return "critical"
    lowered_name = name.lower()
    if any(keyword in lowered_name for keyword in sensitive_keywords):
        return "critical"
    return "warning"


def x_classify_severity__mutmut_4(
    kind: str, name: str, sensitive_keywords: Sequence[str]
) -> ManualChangeSeverity:
    if kind == "SECRET":
        return "critical"
    lowered_name = name.lower()
    if any(keyword in lowered_name for keyword in sensitive_keywords):
        return "critical"
    return "warning"


def x_classify_severity__mutmut_5(
    kind: str, name: str, sensitive_keywords: Sequence[str]
) -> ManualChangeSeverity:
    if kind == "Secret":
        return "XXcriticalXX"
    lowered_name = name.lower()
    if any(keyword in lowered_name for keyword in sensitive_keywords):
        return "critical"
    return "warning"


def x_classify_severity__mutmut_6(
    kind: str, name: str, sensitive_keywords: Sequence[str]
) -> ManualChangeSeverity:
    if kind == "Secret":
        return "CRITICAL"
    lowered_name = name.lower()
    if any(keyword in lowered_name for keyword in sensitive_keywords):
        return "critical"
    return "warning"


def x_classify_severity__mutmut_7(
    kind: str, name: str, sensitive_keywords: Sequence[str]
) -> ManualChangeSeverity:
    if kind == "Secret":
        return "critical"
    lowered_name = None
    if any(keyword in lowered_name for keyword in sensitive_keywords):
        return "critical"
    return "warning"


def x_classify_severity__mutmut_8(
    kind: str, name: str, sensitive_keywords: Sequence[str]
) -> ManualChangeSeverity:
    if kind == "Secret":
        return "critical"
    lowered_name = name.upper()
    if any(keyword in lowered_name for keyword in sensitive_keywords):
        return "critical"
    return "warning"


def x_classify_severity__mutmut_9(
    kind: str, name: str, sensitive_keywords: Sequence[str]
) -> ManualChangeSeverity:
    if kind == "Secret":
        return "critical"
    lowered_name = name.lower()
    if any(None):
        return "critical"
    return "warning"


def x_classify_severity__mutmut_10(
    kind: str, name: str, sensitive_keywords: Sequence[str]
) -> ManualChangeSeverity:
    if kind == "Secret":
        return "critical"
    lowered_name = name.lower()
    if any(keyword not in lowered_name for keyword in sensitive_keywords):
        return "critical"
    return "warning"


def x_classify_severity__mutmut_11(
    kind: str, name: str, sensitive_keywords: Sequence[str]
) -> ManualChangeSeverity:
    if kind == "Secret":
        return "critical"
    lowered_name = name.lower()
    if any(keyword in lowered_name for keyword in sensitive_keywords):
        return "XXcriticalXX"
    return "warning"


def x_classify_severity__mutmut_12(
    kind: str, name: str, sensitive_keywords: Sequence[str]
) -> ManualChangeSeverity:
    if kind == "Secret":
        return "critical"
    lowered_name = name.lower()
    if any(keyword in lowered_name for keyword in sensitive_keywords):
        return "CRITICAL"
    return "warning"


def x_classify_severity__mutmut_13(
    kind: str, name: str, sensitive_keywords: Sequence[str]
) -> ManualChangeSeverity:
    if kind == "Secret":
        return "critical"
    lowered_name = name.lower()
    if any(keyword in lowered_name for keyword in sensitive_keywords):
        return "critical"
    return "XXwarningXX"


def x_classify_severity__mutmut_14(
    kind: str, name: str, sensitive_keywords: Sequence[str]
) -> ManualChangeSeverity:
    if kind == "Secret":
        return "critical"
    lowered_name = name.lower()
    if any(keyword in lowered_name for keyword in sensitive_keywords):
        return "critical"
    return "WARNING"

mutants_x_classify_severity__mutmut['_mutmut_orig'] = x_classify_severity__mutmut_orig # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_1'] = x_classify_severity__mutmut_1 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_2'] = x_classify_severity__mutmut_2 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_3'] = x_classify_severity__mutmut_3 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_4'] = x_classify_severity__mutmut_4 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_5'] = x_classify_severity__mutmut_5 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_6'] = x_classify_severity__mutmut_6 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_7'] = x_classify_severity__mutmut_7 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_8'] = x_classify_severity__mutmut_8 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_9'] = x_classify_severity__mutmut_9 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_10'] = x_classify_severity__mutmut_10 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_11'] = x_classify_severity__mutmut_11 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_12'] = x_classify_severity__mutmut_12 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_13'] = x_classify_severity__mutmut_13 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_14'] = x_classify_severity__mutmut_14 # type: ignore # mutmut generated
