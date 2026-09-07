from __future__ import annotations

from hexawyn.domain.models.external_exposure import RiskLevel, ServiceType

_DOWNGRADE: dict[RiskLevel, RiskLevel] = {
    "critical": "high",
    "high": "medium",
    "medium": "low",
    "low": "low",
}


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_classify_risk_level__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_classify_risk_level__mutmut)
def classify_risk_level(
    base_severity: RiskLevel,
    service_type: ServiceType,
    namespace: str,
    production_namespace: str,
    has_source_ranges: bool,
) -> RiskLevel:
    level = base_severity
    if service_type == "NodePort":
        level = _DOWNGRADE[level]
    elif namespace != production_namespace:
        level = _DOWNGRADE[level]

    if has_source_ranges:
        level = _DOWNGRADE[level]

    return level


def x_classify_risk_level__mutmut_orig(
    base_severity: RiskLevel,
    service_type: ServiceType,
    namespace: str,
    production_namespace: str,
    has_source_ranges: bool,
) -> RiskLevel:
    level = base_severity
    if service_type == "NodePort":
        level = _DOWNGRADE[level]
    elif namespace != production_namespace:
        level = _DOWNGRADE[level]

    if has_source_ranges:
        level = _DOWNGRADE[level]

    return level


def x_classify_risk_level__mutmut_1(
    base_severity: RiskLevel,
    service_type: ServiceType,
    namespace: str,
    production_namespace: str,
    has_source_ranges: bool,
) -> RiskLevel:
    level = None
    if service_type == "NodePort":
        level = _DOWNGRADE[level]
    elif namespace != production_namespace:
        level = _DOWNGRADE[level]

    if has_source_ranges:
        level = _DOWNGRADE[level]

    return level


def x_classify_risk_level__mutmut_2(
    base_severity: RiskLevel,
    service_type: ServiceType,
    namespace: str,
    production_namespace: str,
    has_source_ranges: bool,
) -> RiskLevel:
    level = base_severity
    if service_type != "NodePort":
        level = _DOWNGRADE[level]
    elif namespace != production_namespace:
        level = _DOWNGRADE[level]

    if has_source_ranges:
        level = _DOWNGRADE[level]

    return level


def x_classify_risk_level__mutmut_3(
    base_severity: RiskLevel,
    service_type: ServiceType,
    namespace: str,
    production_namespace: str,
    has_source_ranges: bool,
) -> RiskLevel:
    level = base_severity
    if service_type == "XXNodePortXX":
        level = _DOWNGRADE[level]
    elif namespace != production_namespace:
        level = _DOWNGRADE[level]

    if has_source_ranges:
        level = _DOWNGRADE[level]

    return level


def x_classify_risk_level__mutmut_4(
    base_severity: RiskLevel,
    service_type: ServiceType,
    namespace: str,
    production_namespace: str,
    has_source_ranges: bool,
) -> RiskLevel:
    level = base_severity
    if service_type == "nodeport":
        level = _DOWNGRADE[level]
    elif namespace != production_namespace:
        level = _DOWNGRADE[level]

    if has_source_ranges:
        level = _DOWNGRADE[level]

    return level


def x_classify_risk_level__mutmut_5(
    base_severity: RiskLevel,
    service_type: ServiceType,
    namespace: str,
    production_namespace: str,
    has_source_ranges: bool,
) -> RiskLevel:
    level = base_severity
    if service_type == "NODEPORT":
        level = _DOWNGRADE[level]
    elif namespace != production_namespace:
        level = _DOWNGRADE[level]

    if has_source_ranges:
        level = _DOWNGRADE[level]

    return level


def x_classify_risk_level__mutmut_6(
    base_severity: RiskLevel,
    service_type: ServiceType,
    namespace: str,
    production_namespace: str,
    has_source_ranges: bool,
) -> RiskLevel:
    level = base_severity
    if service_type == "NodePort":
        level = None
    elif namespace != production_namespace:
        level = _DOWNGRADE[level]

    if has_source_ranges:
        level = _DOWNGRADE[level]

    return level


def x_classify_risk_level__mutmut_7(
    base_severity: RiskLevel,
    service_type: ServiceType,
    namespace: str,
    production_namespace: str,
    has_source_ranges: bool,
) -> RiskLevel:
    level = base_severity
    if service_type == "NodePort":
        level = _DOWNGRADE[level]
    elif namespace == production_namespace:
        level = _DOWNGRADE[level]

    if has_source_ranges:
        level = _DOWNGRADE[level]

    return level


def x_classify_risk_level__mutmut_8(
    base_severity: RiskLevel,
    service_type: ServiceType,
    namespace: str,
    production_namespace: str,
    has_source_ranges: bool,
) -> RiskLevel:
    level = base_severity
    if service_type == "NodePort":
        level = _DOWNGRADE[level]
    elif namespace != production_namespace:
        level = None

    if has_source_ranges:
        level = _DOWNGRADE[level]

    return level


def x_classify_risk_level__mutmut_9(
    base_severity: RiskLevel,
    service_type: ServiceType,
    namespace: str,
    production_namespace: str,
    has_source_ranges: bool,
) -> RiskLevel:
    level = base_severity
    if service_type == "NodePort":
        level = _DOWNGRADE[level]
    elif namespace != production_namespace:
        level = _DOWNGRADE[level]

    if has_source_ranges:
        level = None

    return level

mutants_x_classify_risk_level__mutmut['_mutmut_orig'] = x_classify_risk_level__mutmut_orig # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_1'] = x_classify_risk_level__mutmut_1 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_2'] = x_classify_risk_level__mutmut_2 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_3'] = x_classify_risk_level__mutmut_3 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_4'] = x_classify_risk_level__mutmut_4 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_5'] = x_classify_risk_level__mutmut_5 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_6'] = x_classify_risk_level__mutmut_6 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_7'] = x_classify_risk_level__mutmut_7 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_8'] = x_classify_risk_level__mutmut_8 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_9'] = x_classify_risk_level__mutmut_9 # type: ignore # mutmut generated
