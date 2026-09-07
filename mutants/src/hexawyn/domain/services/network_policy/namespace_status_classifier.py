from __future__ import annotations

from hexawyn.domain.models.network_policy import NetworkStatus


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_classify_network_status__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_classify_network_status__mutmut)
def classify_network_status(ingress_policies: int, egress_policies: int) -> NetworkStatus:
    has_ingress = ingress_policies > 0
    has_egress = egress_policies > 0
    if not has_ingress and not has_egress:
        return "open"
    if has_ingress and has_egress:
        return "restricted"
    return "partially_restricted"


def x_classify_network_status__mutmut_orig(ingress_policies: int, egress_policies: int) -> NetworkStatus:
    has_ingress = ingress_policies > 0
    has_egress = egress_policies > 0
    if not has_ingress and not has_egress:
        return "open"
    if has_ingress and has_egress:
        return "restricted"
    return "partially_restricted"


def x_classify_network_status__mutmut_1(ingress_policies: int, egress_policies: int) -> NetworkStatus:
    has_ingress = None
    has_egress = egress_policies > 0
    if not has_ingress and not has_egress:
        return "open"
    if has_ingress and has_egress:
        return "restricted"
    return "partially_restricted"


def x_classify_network_status__mutmut_2(ingress_policies: int, egress_policies: int) -> NetworkStatus:
    has_ingress = ingress_policies >= 0
    has_egress = egress_policies > 0
    if not has_ingress and not has_egress:
        return "open"
    if has_ingress and has_egress:
        return "restricted"
    return "partially_restricted"


def x_classify_network_status__mutmut_3(ingress_policies: int, egress_policies: int) -> NetworkStatus:
    has_ingress = ingress_policies > 1
    has_egress = egress_policies > 0
    if not has_ingress and not has_egress:
        return "open"
    if has_ingress and has_egress:
        return "restricted"
    return "partially_restricted"


def x_classify_network_status__mutmut_4(ingress_policies: int, egress_policies: int) -> NetworkStatus:
    has_ingress = ingress_policies > 0
    has_egress = None
    if not has_ingress and not has_egress:
        return "open"
    if has_ingress and has_egress:
        return "restricted"
    return "partially_restricted"


def x_classify_network_status__mutmut_5(ingress_policies: int, egress_policies: int) -> NetworkStatus:
    has_ingress = ingress_policies > 0
    has_egress = egress_policies >= 0
    if not has_ingress and not has_egress:
        return "open"
    if has_ingress and has_egress:
        return "restricted"
    return "partially_restricted"


def x_classify_network_status__mutmut_6(ingress_policies: int, egress_policies: int) -> NetworkStatus:
    has_ingress = ingress_policies > 0
    has_egress = egress_policies > 1
    if not has_ingress and not has_egress:
        return "open"
    if has_ingress and has_egress:
        return "restricted"
    return "partially_restricted"


def x_classify_network_status__mutmut_7(ingress_policies: int, egress_policies: int) -> NetworkStatus:
    has_ingress = ingress_policies > 0
    has_egress = egress_policies > 0
    if not has_ingress or not has_egress:
        return "open"
    if has_ingress and has_egress:
        return "restricted"
    return "partially_restricted"


def x_classify_network_status__mutmut_8(ingress_policies: int, egress_policies: int) -> NetworkStatus:
    has_ingress = ingress_policies > 0
    has_egress = egress_policies > 0
    if has_ingress and not has_egress:
        return "open"
    if has_ingress and has_egress:
        return "restricted"
    return "partially_restricted"


def x_classify_network_status__mutmut_9(ingress_policies: int, egress_policies: int) -> NetworkStatus:
    has_ingress = ingress_policies > 0
    has_egress = egress_policies > 0
    if not has_ingress and has_egress:
        return "open"
    if has_ingress and has_egress:
        return "restricted"
    return "partially_restricted"


def x_classify_network_status__mutmut_10(ingress_policies: int, egress_policies: int) -> NetworkStatus:
    has_ingress = ingress_policies > 0
    has_egress = egress_policies > 0
    if not has_ingress and not has_egress:
        return "XXopenXX"
    if has_ingress and has_egress:
        return "restricted"
    return "partially_restricted"


def x_classify_network_status__mutmut_11(ingress_policies: int, egress_policies: int) -> NetworkStatus:
    has_ingress = ingress_policies > 0
    has_egress = egress_policies > 0
    if not has_ingress and not has_egress:
        return "OPEN"
    if has_ingress and has_egress:
        return "restricted"
    return "partially_restricted"


def x_classify_network_status__mutmut_12(ingress_policies: int, egress_policies: int) -> NetworkStatus:
    has_ingress = ingress_policies > 0
    has_egress = egress_policies > 0
    if not has_ingress and not has_egress:
        return "open"
    if has_ingress or has_egress:
        return "restricted"
    return "partially_restricted"


def x_classify_network_status__mutmut_13(ingress_policies: int, egress_policies: int) -> NetworkStatus:
    has_ingress = ingress_policies > 0
    has_egress = egress_policies > 0
    if not has_ingress and not has_egress:
        return "open"
    if has_ingress and has_egress:
        return "XXrestrictedXX"
    return "partially_restricted"


def x_classify_network_status__mutmut_14(ingress_policies: int, egress_policies: int) -> NetworkStatus:
    has_ingress = ingress_policies > 0
    has_egress = egress_policies > 0
    if not has_ingress and not has_egress:
        return "open"
    if has_ingress and has_egress:
        return "RESTRICTED"
    return "partially_restricted"


def x_classify_network_status__mutmut_15(ingress_policies: int, egress_policies: int) -> NetworkStatus:
    has_ingress = ingress_policies > 0
    has_egress = egress_policies > 0
    if not has_ingress and not has_egress:
        return "open"
    if has_ingress and has_egress:
        return "restricted"
    return "XXpartially_restrictedXX"


def x_classify_network_status__mutmut_16(ingress_policies: int, egress_policies: int) -> NetworkStatus:
    has_ingress = ingress_policies > 0
    has_egress = egress_policies > 0
    if not has_ingress and not has_egress:
        return "open"
    if has_ingress and has_egress:
        return "restricted"
    return "PARTIALLY_RESTRICTED"

mutants_x_classify_network_status__mutmut['_mutmut_orig'] = x_classify_network_status__mutmut_orig # type: ignore # mutmut generated
mutants_x_classify_network_status__mutmut['x_classify_network_status__mutmut_1'] = x_classify_network_status__mutmut_1 # type: ignore # mutmut generated
mutants_x_classify_network_status__mutmut['x_classify_network_status__mutmut_2'] = x_classify_network_status__mutmut_2 # type: ignore # mutmut generated
mutants_x_classify_network_status__mutmut['x_classify_network_status__mutmut_3'] = x_classify_network_status__mutmut_3 # type: ignore # mutmut generated
mutants_x_classify_network_status__mutmut['x_classify_network_status__mutmut_4'] = x_classify_network_status__mutmut_4 # type: ignore # mutmut generated
mutants_x_classify_network_status__mutmut['x_classify_network_status__mutmut_5'] = x_classify_network_status__mutmut_5 # type: ignore # mutmut generated
mutants_x_classify_network_status__mutmut['x_classify_network_status__mutmut_6'] = x_classify_network_status__mutmut_6 # type: ignore # mutmut generated
mutants_x_classify_network_status__mutmut['x_classify_network_status__mutmut_7'] = x_classify_network_status__mutmut_7 # type: ignore # mutmut generated
mutants_x_classify_network_status__mutmut['x_classify_network_status__mutmut_8'] = x_classify_network_status__mutmut_8 # type: ignore # mutmut generated
mutants_x_classify_network_status__mutmut['x_classify_network_status__mutmut_9'] = x_classify_network_status__mutmut_9 # type: ignore # mutmut generated
mutants_x_classify_network_status__mutmut['x_classify_network_status__mutmut_10'] = x_classify_network_status__mutmut_10 # type: ignore # mutmut generated
mutants_x_classify_network_status__mutmut['x_classify_network_status__mutmut_11'] = x_classify_network_status__mutmut_11 # type: ignore # mutmut generated
mutants_x_classify_network_status__mutmut['x_classify_network_status__mutmut_12'] = x_classify_network_status__mutmut_12 # type: ignore # mutmut generated
mutants_x_classify_network_status__mutmut['x_classify_network_status__mutmut_13'] = x_classify_network_status__mutmut_13 # type: ignore # mutmut generated
mutants_x_classify_network_status__mutmut['x_classify_network_status__mutmut_14'] = x_classify_network_status__mutmut_14 # type: ignore # mutmut generated
mutants_x_classify_network_status__mutmut['x_classify_network_status__mutmut_15'] = x_classify_network_status__mutmut_15 # type: ignore # mutmut generated
mutants_x_classify_network_status__mutmut['x_classify_network_status__mutmut_16'] = x_classify_network_status__mutmut_16 # type: ignore # mutmut generated
