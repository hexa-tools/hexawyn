from __future__ import annotations

from hexawyn.domain.models.network_policy import NetworkStatus, RiskLevel

_STATUS_RISK: dict[NetworkStatus, RiskLevel] = {
    "open": "critical",
    "partially_restricted": "medium",
    "restricted": "low",
}


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_classify_risk_level__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_classify_risk_level__mutmut)
def classify_risk_level(network_status: NetworkStatus, pod_count: int) -> RiskLevel:
    if pod_count == 0:
        return "low"
    return _STATUS_RISK[network_status]


def x_classify_risk_level__mutmut_orig(network_status: NetworkStatus, pod_count: int) -> RiskLevel:
    if pod_count == 0:
        return "low"
    return _STATUS_RISK[network_status]


def x_classify_risk_level__mutmut_1(network_status: NetworkStatus, pod_count: int) -> RiskLevel:
    if pod_count != 0:
        return "low"
    return _STATUS_RISK[network_status]


def x_classify_risk_level__mutmut_2(network_status: NetworkStatus, pod_count: int) -> RiskLevel:
    if pod_count == 1:
        return "low"
    return _STATUS_RISK[network_status]


def x_classify_risk_level__mutmut_3(network_status: NetworkStatus, pod_count: int) -> RiskLevel:
    if pod_count == 0:
        return "XXlowXX"
    return _STATUS_RISK[network_status]


def x_classify_risk_level__mutmut_4(network_status: NetworkStatus, pod_count: int) -> RiskLevel:
    if pod_count == 0:
        return "LOW"
    return _STATUS_RISK[network_status]

mutants_x_classify_risk_level__mutmut['_mutmut_orig'] = x_classify_risk_level__mutmut_orig # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_1'] = x_classify_risk_level__mutmut_1 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_2'] = x_classify_risk_level__mutmut_2 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_3'] = x_classify_risk_level__mutmut_3 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_4'] = x_classify_risk_level__mutmut_4 # type: ignore # mutmut generated
