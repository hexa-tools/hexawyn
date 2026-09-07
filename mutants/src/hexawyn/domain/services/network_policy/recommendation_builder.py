from __future__ import annotations

from hexawyn.domain.models.network_policy import NetworkStatus


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_recommendation__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_recommendation__mutmut)
def build_recommendation(
    network_status: NetworkStatus, ingress_policies: int, egress_policies: int
) -> str | None:
    if network_status == "open":
        return "Apply default-deny NetworkPolicy for both ingress and egress"
    if network_status == "partially_restricted":
        if ingress_policies == 0:
            return "Add default-deny ingress NetworkPolicy"
        return "Add default-deny egress NetworkPolicy"
    return None


def x_build_recommendation__mutmut_orig(
    network_status: NetworkStatus, ingress_policies: int, egress_policies: int
) -> str | None:
    if network_status == "open":
        return "Apply default-deny NetworkPolicy for both ingress and egress"
    if network_status == "partially_restricted":
        if ingress_policies == 0:
            return "Add default-deny ingress NetworkPolicy"
        return "Add default-deny egress NetworkPolicy"
    return None


def x_build_recommendation__mutmut_1(
    network_status: NetworkStatus, ingress_policies: int, egress_policies: int
) -> str | None:
    if network_status != "open":
        return "Apply default-deny NetworkPolicy for both ingress and egress"
    if network_status == "partially_restricted":
        if ingress_policies == 0:
            return "Add default-deny ingress NetworkPolicy"
        return "Add default-deny egress NetworkPolicy"
    return None


def x_build_recommendation__mutmut_2(
    network_status: NetworkStatus, ingress_policies: int, egress_policies: int
) -> str | None:
    if network_status == "XXopenXX":
        return "Apply default-deny NetworkPolicy for both ingress and egress"
    if network_status == "partially_restricted":
        if ingress_policies == 0:
            return "Add default-deny ingress NetworkPolicy"
        return "Add default-deny egress NetworkPolicy"
    return None


def x_build_recommendation__mutmut_3(
    network_status: NetworkStatus, ingress_policies: int, egress_policies: int
) -> str | None:
    if network_status == "OPEN":
        return "Apply default-deny NetworkPolicy for both ingress and egress"
    if network_status == "partially_restricted":
        if ingress_policies == 0:
            return "Add default-deny ingress NetworkPolicy"
        return "Add default-deny egress NetworkPolicy"
    return None


def x_build_recommendation__mutmut_4(
    network_status: NetworkStatus, ingress_policies: int, egress_policies: int
) -> str | None:
    if network_status == "open":
        return "XXApply default-deny NetworkPolicy for both ingress and egressXX"
    if network_status == "partially_restricted":
        if ingress_policies == 0:
            return "Add default-deny ingress NetworkPolicy"
        return "Add default-deny egress NetworkPolicy"
    return None


def x_build_recommendation__mutmut_5(
    network_status: NetworkStatus, ingress_policies: int, egress_policies: int
) -> str | None:
    if network_status == "open":
        return "apply default-deny networkpolicy for both ingress and egress"
    if network_status == "partially_restricted":
        if ingress_policies == 0:
            return "Add default-deny ingress NetworkPolicy"
        return "Add default-deny egress NetworkPolicy"
    return None


def x_build_recommendation__mutmut_6(
    network_status: NetworkStatus, ingress_policies: int, egress_policies: int
) -> str | None:
    if network_status == "open":
        return "APPLY DEFAULT-DENY NETWORKPOLICY FOR BOTH INGRESS AND EGRESS"
    if network_status == "partially_restricted":
        if ingress_policies == 0:
            return "Add default-deny ingress NetworkPolicy"
        return "Add default-deny egress NetworkPolicy"
    return None


def x_build_recommendation__mutmut_7(
    network_status: NetworkStatus, ingress_policies: int, egress_policies: int
) -> str | None:
    if network_status == "open":
        return "Apply default-deny NetworkPolicy for both ingress and egress"
    if network_status != "partially_restricted":
        if ingress_policies == 0:
            return "Add default-deny ingress NetworkPolicy"
        return "Add default-deny egress NetworkPolicy"
    return None


def x_build_recommendation__mutmut_8(
    network_status: NetworkStatus, ingress_policies: int, egress_policies: int
) -> str | None:
    if network_status == "open":
        return "Apply default-deny NetworkPolicy for both ingress and egress"
    if network_status == "XXpartially_restrictedXX":
        if ingress_policies == 0:
            return "Add default-deny ingress NetworkPolicy"
        return "Add default-deny egress NetworkPolicy"
    return None


def x_build_recommendation__mutmut_9(
    network_status: NetworkStatus, ingress_policies: int, egress_policies: int
) -> str | None:
    if network_status == "open":
        return "Apply default-deny NetworkPolicy for both ingress and egress"
    if network_status == "PARTIALLY_RESTRICTED":
        if ingress_policies == 0:
            return "Add default-deny ingress NetworkPolicy"
        return "Add default-deny egress NetworkPolicy"
    return None


def x_build_recommendation__mutmut_10(
    network_status: NetworkStatus, ingress_policies: int, egress_policies: int
) -> str | None:
    if network_status == "open":
        return "Apply default-deny NetworkPolicy for both ingress and egress"
    if network_status == "partially_restricted":
        if ingress_policies != 0:
            return "Add default-deny ingress NetworkPolicy"
        return "Add default-deny egress NetworkPolicy"
    return None


def x_build_recommendation__mutmut_11(
    network_status: NetworkStatus, ingress_policies: int, egress_policies: int
) -> str | None:
    if network_status == "open":
        return "Apply default-deny NetworkPolicy for both ingress and egress"
    if network_status == "partially_restricted":
        if ingress_policies == 1:
            return "Add default-deny ingress NetworkPolicy"
        return "Add default-deny egress NetworkPolicy"
    return None


def x_build_recommendation__mutmut_12(
    network_status: NetworkStatus, ingress_policies: int, egress_policies: int
) -> str | None:
    if network_status == "open":
        return "Apply default-deny NetworkPolicy for both ingress and egress"
    if network_status == "partially_restricted":
        if ingress_policies == 0:
            return "XXAdd default-deny ingress NetworkPolicyXX"
        return "Add default-deny egress NetworkPolicy"
    return None


def x_build_recommendation__mutmut_13(
    network_status: NetworkStatus, ingress_policies: int, egress_policies: int
) -> str | None:
    if network_status == "open":
        return "Apply default-deny NetworkPolicy for both ingress and egress"
    if network_status == "partially_restricted":
        if ingress_policies == 0:
            return "add default-deny ingress networkpolicy"
        return "Add default-deny egress NetworkPolicy"
    return None


def x_build_recommendation__mutmut_14(
    network_status: NetworkStatus, ingress_policies: int, egress_policies: int
) -> str | None:
    if network_status == "open":
        return "Apply default-deny NetworkPolicy for both ingress and egress"
    if network_status == "partially_restricted":
        if ingress_policies == 0:
            return "ADD DEFAULT-DENY INGRESS NETWORKPOLICY"
        return "Add default-deny egress NetworkPolicy"
    return None


def x_build_recommendation__mutmut_15(
    network_status: NetworkStatus, ingress_policies: int, egress_policies: int
) -> str | None:
    if network_status == "open":
        return "Apply default-deny NetworkPolicy for both ingress and egress"
    if network_status == "partially_restricted":
        if ingress_policies == 0:
            return "Add default-deny ingress NetworkPolicy"
        return "XXAdd default-deny egress NetworkPolicyXX"
    return None


def x_build_recommendation__mutmut_16(
    network_status: NetworkStatus, ingress_policies: int, egress_policies: int
) -> str | None:
    if network_status == "open":
        return "Apply default-deny NetworkPolicy for both ingress and egress"
    if network_status == "partially_restricted":
        if ingress_policies == 0:
            return "Add default-deny ingress NetworkPolicy"
        return "add default-deny egress networkpolicy"
    return None


def x_build_recommendation__mutmut_17(
    network_status: NetworkStatus, ingress_policies: int, egress_policies: int
) -> str | None:
    if network_status == "open":
        return "Apply default-deny NetworkPolicy for both ingress and egress"
    if network_status == "partially_restricted":
        if ingress_policies == 0:
            return "Add default-deny ingress NetworkPolicy"
        return "ADD DEFAULT-DENY EGRESS NETWORKPOLICY"
    return None

mutants_x_build_recommendation__mutmut['_mutmut_orig'] = x_build_recommendation__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_1'] = x_build_recommendation__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_2'] = x_build_recommendation__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_3'] = x_build_recommendation__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_4'] = x_build_recommendation__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_5'] = x_build_recommendation__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_6'] = x_build_recommendation__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_7'] = x_build_recommendation__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_8'] = x_build_recommendation__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_9'] = x_build_recommendation__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_10'] = x_build_recommendation__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_11'] = x_build_recommendation__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_12'] = x_build_recommendation__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_13'] = x_build_recommendation__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_14'] = x_build_recommendation__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_15'] = x_build_recommendation__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_16'] = x_build_recommendation__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_recommendation__mutmut['x_build_recommendation__mutmut_17'] = x_build_recommendation__mutmut_17 # type: ignore # mutmut generated
