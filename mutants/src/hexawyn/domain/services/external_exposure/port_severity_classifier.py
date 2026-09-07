from __future__ import annotations

from hexawyn.domain.models.external_exposure import RiskLevel


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_classify_base_severity__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_classify_base_severity__mutmut)
def classify_base_severity(
    ports: list[int], critical_ports: tuple[int, ...], medium_ports: tuple[int, ...]
) -> RiskLevel:
    if any(port in critical_ports for port in ports):
        return "critical"
    if any(port in medium_ports for port in ports):
        return "medium"
    return "medium"


def x_classify_base_severity__mutmut_orig(
    ports: list[int], critical_ports: tuple[int, ...], medium_ports: tuple[int, ...]
) -> RiskLevel:
    if any(port in critical_ports for port in ports):
        return "critical"
    if any(port in medium_ports for port in ports):
        return "medium"
    return "medium"


def x_classify_base_severity__mutmut_1(
    ports: list[int], critical_ports: tuple[int, ...], medium_ports: tuple[int, ...]
) -> RiskLevel:
    if any(None):
        return "critical"
    if any(port in medium_ports for port in ports):
        return "medium"
    return "medium"


def x_classify_base_severity__mutmut_2(
    ports: list[int], critical_ports: tuple[int, ...], medium_ports: tuple[int, ...]
) -> RiskLevel:
    if any(port not in critical_ports for port in ports):
        return "critical"
    if any(port in medium_ports for port in ports):
        return "medium"
    return "medium"


def x_classify_base_severity__mutmut_3(
    ports: list[int], critical_ports: tuple[int, ...], medium_ports: tuple[int, ...]
) -> RiskLevel:
    if any(port in critical_ports for port in ports):
        return "XXcriticalXX"
    if any(port in medium_ports for port in ports):
        return "medium"
    return "medium"


def x_classify_base_severity__mutmut_4(
    ports: list[int], critical_ports: tuple[int, ...], medium_ports: tuple[int, ...]
) -> RiskLevel:
    if any(port in critical_ports for port in ports):
        return "CRITICAL"
    if any(port in medium_ports for port in ports):
        return "medium"
    return "medium"


def x_classify_base_severity__mutmut_5(
    ports: list[int], critical_ports: tuple[int, ...], medium_ports: tuple[int, ...]
) -> RiskLevel:
    if any(port in critical_ports for port in ports):
        return "critical"
    if any(None):
        return "medium"
    return "medium"


def x_classify_base_severity__mutmut_6(
    ports: list[int], critical_ports: tuple[int, ...], medium_ports: tuple[int, ...]
) -> RiskLevel:
    if any(port in critical_ports for port in ports):
        return "critical"
    if any(port not in medium_ports for port in ports):
        return "medium"
    return "medium"


def x_classify_base_severity__mutmut_7(
    ports: list[int], critical_ports: tuple[int, ...], medium_ports: tuple[int, ...]
) -> RiskLevel:
    if any(port in critical_ports for port in ports):
        return "critical"
    if any(port in medium_ports for port in ports):
        return "XXmediumXX"
    return "medium"


def x_classify_base_severity__mutmut_8(
    ports: list[int], critical_ports: tuple[int, ...], medium_ports: tuple[int, ...]
) -> RiskLevel:
    if any(port in critical_ports for port in ports):
        return "critical"
    if any(port in medium_ports for port in ports):
        return "MEDIUM"
    return "medium"


def x_classify_base_severity__mutmut_9(
    ports: list[int], critical_ports: tuple[int, ...], medium_ports: tuple[int, ...]
) -> RiskLevel:
    if any(port in critical_ports for port in ports):
        return "critical"
    if any(port in medium_ports for port in ports):
        return "medium"
    return "XXmediumXX"


def x_classify_base_severity__mutmut_10(
    ports: list[int], critical_ports: tuple[int, ...], medium_ports: tuple[int, ...]
) -> RiskLevel:
    if any(port in critical_ports for port in ports):
        return "critical"
    if any(port in medium_ports for port in ports):
        return "medium"
    return "MEDIUM"

mutants_x_classify_base_severity__mutmut['_mutmut_orig'] = x_classify_base_severity__mutmut_orig # type: ignore # mutmut generated
mutants_x_classify_base_severity__mutmut['x_classify_base_severity__mutmut_1'] = x_classify_base_severity__mutmut_1 # type: ignore # mutmut generated
mutants_x_classify_base_severity__mutmut['x_classify_base_severity__mutmut_2'] = x_classify_base_severity__mutmut_2 # type: ignore # mutmut generated
mutants_x_classify_base_severity__mutmut['x_classify_base_severity__mutmut_3'] = x_classify_base_severity__mutmut_3 # type: ignore # mutmut generated
mutants_x_classify_base_severity__mutmut['x_classify_base_severity__mutmut_4'] = x_classify_base_severity__mutmut_4 # type: ignore # mutmut generated
mutants_x_classify_base_severity__mutmut['x_classify_base_severity__mutmut_5'] = x_classify_base_severity__mutmut_5 # type: ignore # mutmut generated
mutants_x_classify_base_severity__mutmut['x_classify_base_severity__mutmut_6'] = x_classify_base_severity__mutmut_6 # type: ignore # mutmut generated
mutants_x_classify_base_severity__mutmut['x_classify_base_severity__mutmut_7'] = x_classify_base_severity__mutmut_7 # type: ignore # mutmut generated
mutants_x_classify_base_severity__mutmut['x_classify_base_severity__mutmut_8'] = x_classify_base_severity__mutmut_8 # type: ignore # mutmut generated
mutants_x_classify_base_severity__mutmut['x_classify_base_severity__mutmut_9'] = x_classify_base_severity__mutmut_9 # type: ignore # mutmut generated
mutants_x_classify_base_severity__mutmut['x_classify_base_severity__mutmut_10'] = x_classify_base_severity__mutmut_10 # type: ignore # mutmut generated
